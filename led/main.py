#Imports modules
import socket
import colors
import time
import ledstrip
import RPi.GPIO as GPIO
import os

from signal import pause

listensocket = socket.socket() #Creates an instance of socket
Port = 8000 #Port to host server on
maxConnections = 999
IP = socket.gethostname() #IP address of local machine

listensocket.bind(('',Port))


while True:
	#Starts server
	listensocket.listen(maxConnections)
	print("Server started at " + IP + " on port " + str(Port))

	#Accepts the incomming connection
	(clientsocket, address) = listensocket.accept()
	print("New connection made!")

	running = True

	strip = ledstrip.LedStrip()
		
	strip.start()

	while running:
		message = clientsocket.recv(1024).decode() #Gets the incomming message
		print(message)
		if not message == "":
			try:
				if message == "exit":
					print(message)
					clientsocket.close()
					strip.transition_to(colors.get("black"), 100)
					running = False
					
				if message is "shutdown":
					os.system("sudo shutdown -h now")
					
				if message.startswith("Color:"):
					s = message.split(":")
					c = eval(s[1])
					print(c)
					strip.transition_to(c, 100)
					
			except ValueError:
				pass
	
