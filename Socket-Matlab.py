#####################################################################
# Aldo Vargas
# 
#
# Purpose:
#	Matlab sends n signals via UDP to the Raspberry pie... 
#	RPI receives the data, unpacks it and prints it.
#	- This is just for testing the best methodology between Matlab-rpi
#	This methos uses sockets
#
########################################################################


import socket
import struct
import time

#Raspberry pie IP address
#UDP_IP = "172.30.144.154"
#Mac IP address
UDP_IP = "192.168.0.103"
#UDP_IP = "localhost"
UDP_PORT = 51001
message = ""
udp_mess = ""
timestamp = 0

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

print "System ready on "+str(UDP_IP)

while True:
	timestamp = time.time()
	data, addr = sock.recvfrom(2048)
	numOfValues = len(data) / 8
	mess=struct.unpack('>' + 'd' * numOfValues, data)
	for x in range(0, numOfValues):
 		udp_mess = udp_mess+" "+str(mess[x])
 	diff = time.time() - timestamp
 	print str(diff)+udp_mess
 	udp_mess=""
