# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:03:41 2022

@author: Grupo 3
"""

# Import Module
import ftplib

# Fill Required Information
HOSTNAME = "0.0.0.0"
USERNAME = "grupo3"
PASSWORD = "grupo3"

# Connect FTP Server
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

# force UTF-8 encoding
ftp_server.encoding = "utf-8"

# Enter File Name with Extension
filename = "gfg.txt"

# Write file in binary mode
with open(filename, "wb") as file:
	# Command for Downloading the file "RETR filename"
	ftp_server.retrbinary(f"RETR {filename}", file.write)

# Get list of files
ftp_server.dir()

# Display the content of downloaded file
file= open(filename, "r")
print('File Content:', file.read())

# Close the Connection
ftp_server.quit()

