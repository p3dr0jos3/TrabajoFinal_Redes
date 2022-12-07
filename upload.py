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
filename = "File Name"

# Read file in binary mode
with open(filename, "rb") as file:
	# Command for Uploading the file "STOR filename"
	ftp_server.storbinary(f"STOR {filename}", file)

# Get list of files
ftp_server.dir()

# Close the Connection
ftp_server.quit()
