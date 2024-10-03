# Makefile for CMPT 361 Assignment 1

# Target to remove the PDF file
reset:
	rm -f 'Server/file.pdf' 

# Target to run the client program
client:
	python3 Client/client.py

# Target to run the server program & reset the environment for a new server
server: reset
	python3 Server/server.py
