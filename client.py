# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:34:29 2022

@author: Pedro Sánchez
"""

# Import socket module
import socket			

# Create a socket object
s = socket.socket()		

# Define the port on which you want to connect
port = 21			

# connect to the server on local computer
s.connect(('192.168.31.166', port))

# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
# close the connection
s.close()	
	
