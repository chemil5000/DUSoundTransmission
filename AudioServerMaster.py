### Python master module for nonverbal communication ###
### designed to be impemented on a Nao Robot         ###
### David Chan - April 3, 2016                       ###

##
# Global Vars
##
connected_to_sender = False
sender_sock = None
sender_ip = 'localhost'
sender_port = 13000

connected_to_receiver = False
recv_sock = None
recv_ip = 'localhost'
recv_port = 14000

##
# Imports
##

import socket
import numpy as np
import pickle
import sys
import AudioHandlerMaster

##
# Parse command line arguments
##
if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '-help' or sys.argv[1] == '--help':
	print 'Usage: AudioServerMaster.py [sender robot ip] [receiver robot ip]'
	exit()

sender_ip = sys.argv[1]
recv_ip = sys.argv[2]

##
# Connect to the sender robot
##
try:
	sender_sock = socket.socket()
	sender_sock.connect((sender_ip,sender_port))
except:
	print 'Couldn\'t connect to sender robot at',sender_ip
	exit()

##
# Connect to the receiver robot
##
try:
	recv_sock = socket.socket()
	recv_sock.connect((recv_ip,recv_port))
except:
	print 'Couldn\'t connect to receiver robot at',sender_ip
	sender_sock.close()
	exit()

##
# Parse input in a shell like interface
##
while True:
	i = raw_input('>> ')
	tokens = i.split()
	if not AudioHandlerMaster.handle_command(sender_sock,recv_sock,tokens):
		sender_sock.close()
		recv_sock.close()
		break