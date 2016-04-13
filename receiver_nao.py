import socket
import sys
import struct
from thread import start_new_thread 
import logging
import RXModTest as rxls
import startRecordWavNao as strtrwn
import stopRecordWavNao as stprwn
import toneRX as t_rx


def masterHandler(sock):
    """
    This function handles messages from master controller
    """
    while True:
        strtrwn.startRecordWav()
        time.sleep(5.0)
        #@TODO have an end signal to stop recording
        stprwn.stopRecordWav()
        #data = rx.rxDecode("outRecX.wav")
        t_rx.toneDecode()
        #@TODO send data to master
        print "IN", data
        sock.sendall(data)

# Create a TCP/IP socket
#logging.basicConfig(filename='sender_nao.log',level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 14000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)

while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        logging.debug('client connected:{}'.format(client_address))
        start_new_thread(masterHandler , (connection,))
    except:
        print('Unexpected error '.format(sys.exc_info()[0]))
        connection.close()
sock.close()
