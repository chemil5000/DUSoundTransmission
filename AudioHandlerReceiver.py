### Python handler module for nonverbal communication ###
### designed to be impemented on a Nao Robot when     ### 
### receiving info                                    ###
### David Chan - April 3, 2016                        ###

##
# Imports
##

import numpy as np
import pickle
import socket
import time

##
# General data handling
##

def handle_connection(connection, address, port):
	while True:
		# Do something here.... we probably want to use this to take the opportunity
		# to read from the air and send info back to the robot
		time.sleep(5)
		connection.send('tick')
