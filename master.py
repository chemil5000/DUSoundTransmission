import socket
import sys
import struct
import binascii
import time
import logging
import payload_type as pt
import recvall as rcv
########################################################################
# Change op code as per final configuration
#LOCATION_PAYLOAD_TYPE = 1
#DATA_PAYLOAD_TYPE = 2


########################################################################


# Create a TCP/IP socket
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server given by the caller
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
portTx = 13000
portRx = 14000
server_addressTx = (sys.argv[1], portTx)
server_addressRx = (sys.argv[2], portRx)
sockTx = None
sockRx = None
is_connected = False
is_connected_recv = False
def listen_over_sockRx():
    logging.debug('Creating socket')
    global sockRx
    global is_connected_recv
    if False == is_connected_recv:
        sockRx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.debug('connecting to {} port {}'.format(
                              server_addressRx, portRx))
        sockTx.connect(server_addressRx)
        is_connected_recv = True
        data = recv.recvall(sockRx)
        print data
        
def send_over_sockTx(data):
    logging.debug('Creating socket')
    global sockTx
    global is_connected
    if False == is_connected:
        sockTx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.debug('connecting to {} port {}'.format(
                              server_addressTx, portTx))
        sockTx.connect(server_addressTx)
        is_connected = True
    sockTx.sendall(data)
    print('message sent')
message_type = 0
while message_type!=-1:
    print(" \nEnter Message type to send to NAO \n"
          "Loction message press::  0 \nPayload message press :: 1"
          " \n To exit:: -1")
    message_type = int(raw_input('Enter the choice'))
    if -1 == message_type:
        sock.close()
        sys.exit(-1)
    elif 0 == message_type:
        x = int(raw_input('Enter the x coordinate'))
        y = int(raw_input('Enter the y coordinate'))
        packer = struct.Struct('B I I')
        values = (pt.LOCATION_PAYLOAD_TYPE, x, y)
        packed_dataTx = packer.pack(*values)
        print('sending hex {}  of {}, {}, {} '.format(
              binascii.hexlify(packed_dataTx),
              pt.LOCATION_PAYLOAD_TYPE, x, y))
        send_over_sockTx(packed_dataTx)
        
        #sock.sendall(packed_data)
    elif 1 == message_type:
        # should test with framented  payload too
        offset = int(raw_input('Enter offset of payload in orignal'
                               ' message'))
        n_bytes = int(raw_input('How may bytes in payload'))
        payload = []
        for i_payload in xrange(n_bytes):
            msg = 'Enter number between 0 and 255 for payload'\
                     'byte {}'.format(i_payload + 1)
            byte_payload = int(raw_input(msg))
            payload.append(byte_payload)
        logging.debug('Payload to send is {}'.format(payload))    
        packer = struct.Struct('B I I')
        values = (pt.DATA_PAYLOAD_TYPE, offset, n_bytes)
        packed_data = packer.pack(*values)
        print('sending hex {}  of {}, {} {} '.format(
              binascii.hexlify(packed_data), pt.DATA_PAYLOAD_TYPE
              , offset, n_bytes))
        send_over_sockTx(packed_data)
        payload_packer = struct.Struct('B '*len(payload))
        payload_packed_data = payload_packer.pack(*payload)            
        send_over_sockTx(payload_packed_data)

        #start listening
        listen_over_sockRx()            
