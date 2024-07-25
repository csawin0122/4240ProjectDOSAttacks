import socket
import time

# initializing list of sockets and number of successful connections
sockets = []
numConnectSuccess = 0

# looping 1000 times to create 1000 connections (ADJUST AS NEEDED)
for i in range(1000):
	try:
		# creating socket and connecting to loopback address port 80
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(('127.0.0.1', 80))
		print("CONNECTION ESTABLISHED")
		
		# adding socket to list of sockets and incrementing number of successful connections
		sockets.append(sock)
		numConnectSuccess = numConnectSuccess + 1
		
	# catching errors when creating socket or connecting to address and port
	except Exception as e:
		print("CONNECTION FAILED")
		
# printing that all connections have been made and to press CTRL C to exit the program and close connections
print("\n", numConnectSuccess, "CONNECTIONS MADE\n")
print("\nLEAVING CONNECTIONS OPEN UNTIL CTRL C IS PRESSED\n")

# sleeping until CTRL C is pressed
try:
	while True:
		time.sleep(1)
		
#When CTRL C is pressed, close all sockets
except KeyboardInterrupt:
	for sock in sockets:
		sock.close()
	print("\nCONNECTIONS CLOSED")

