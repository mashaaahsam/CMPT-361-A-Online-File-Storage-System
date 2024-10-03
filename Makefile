# Makefile for CMPT 361 Assignment 1

# Target to remove any files that were sent over (leave the .py and .json)
reset:
	rm -f Server/*.pdf
	rm -f Server/*.txt
	rm -f Server/*.jpeg

# Target to run the client program
client:
	python3 Client/client.py

# Target to run the server program & reset the environment for a new server
server: reset
	python3 Server/server.py
