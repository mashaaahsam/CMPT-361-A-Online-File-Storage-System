# Makefile for CMPT 361 Assignment 1

# Target to remove the PDF file
reset:
	rm -f 'CMPT 361 Assignment 1.pdf - NEW'

# Target to run the client program
client:
	python3 client.py

# Target to run the server program
server:
	python3 server.py
