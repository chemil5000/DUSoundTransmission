import socket
import sys
import struct
from thread import start_new_thread 
import logging
import payload_type as pt
import TXModTest as tx
import playWavNao as pwn

def masterHandler(sock):
    """
    This function handles messages from master controller
    """
    while True:
        unpacker = struct.Struct('B I I')
        logging.debug('Inside master handler.going to read byte + int + int')
        # @TODO make sure me read unpacker.size
        data = sock.recv(unpacker.size)
        unpacked_data = unpacker.unpack(data)
        intUnpack_data = int(str(unpacked_data[1])+str(unpacked_data[2]))
        binUnpack_data = "{0:b}".format(intUnpack_data)
        print "OUT", binUnpack_data
        """        
        trigger modulation encoding to send the sound
	"""  
        tx.txMod(binUnpack_data)
        """
        play the wav file created
        """
        pwn.playWav('outRecX.wav')
        print "Finished Transmitting..."
    
# Create a TCP/IP socket
#logging.basicConfig(filename='sender_nao.log',level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 13000)
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
