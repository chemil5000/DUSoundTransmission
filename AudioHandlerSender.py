### Python handler module for nonverbal communication ###
### designed to be impemented on a Nao Robot when     ### 
### sending info                                      ###
### David Chan - April 3, 2016                        ###

##
# Imports
##

import numpy as np
import pickle
import socket

##
# Handler
##

def handle_location(L):
	print L

def handle_data(L):
	print L

##
# General data handling
##

def handle_connection(connection, address, port):
	while True:
		x = connection.recv(4096)
		if x == '':
			break
		elif x == 'location':
			y = connection.recv(4096)
			L = pickle.loads(y)
			handle_location(L)
		elif x == 'data':
			y = connection.recv(4096)
			L = pickle.loads(y)
			handle_data(L)
