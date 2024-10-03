"""
Short version of desc.

Detailed description...

authour: Maryia Antoshkina
"""

# IMPORTS
import socket
import sys
import os


# FUNCTIONS
"""
Purpose:
Parameters:
Returns:
"""
def client():
    # Get the serverName from the user
    serverName = input('Enter the host name or IP: ') # localhost = '127.0.0.1' 

    # Server Information
    serverPort = 13000

    # Create client socket 
    try: 
        # Client Socket is using IPv4 and TCP
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as e:
        print('Error in client socket creation: ', e)
        sys.exit(1)
    
    
    try:
        # Client connect with server
        clientSocket.connect((serverName, serverPort))

         # Start Communication
        #--------------------------------------------------------
        
        while True:
            # Message Length First
            messageLen = int(clientSocket.recv(4).decode('ascii'))

            # Accept a message with that message length
            message = clientSocket.recv(messageLen).decode('ascii')

            # The server has been terminated, disconnect
            if message == 'exit':
                print("Connection is Terminated")
                break

            if message == 'incorrectUserName':
                print("Incorrect username. Connection Terminated.")
                break

            else:
                # User decides something based on the message from server
                userChoice = input(message)

                # Send userchoice to the server
                clientSocket.send(userChoice.encode('ascii'))

                # Check if user wanted to upload a file, if so go to upload menu
                if userChoice.strip() == '2':
                    upload(clientSocket)

        # Stop Communication - Terminate connection with server
        #--------------------------------------------------------
        clientSocket.close()
        
    except socket.error as e:
        print("An error occured:", e)
        clientSocket.close()
        sys.close(1)
    


# Helper Functions

"""
Purpose:
Parameters:
Returns:
"""
def upload(clientSocket):
    # Message Length First
    messageLen = int(clientSocket.recv(4).decode('ascii'))

    # Accept a message with that message length
    message = clientSocket.recv(messageLen).decode('ascii')

    # User enters the filename to upload
    userChoice = input(message)

    # Try to find the file
    try:
        # Get size in bytes of the file based on the user choice
        sizeBytes = os.path.getsize(userChoice)

        fileInfo = f"{userChoice}  :::  {sizeBytes}"

        # Send userchoice + size of file to the server
        clientSocket.send(fileInfo.encode('ascii'))

        # Recieve the OK size message & print for user
        messageLen = int(clientSocket.recv(4).decode('ascii'))
        message = clientSocket.recv(messageLen).decode('ascii')
        print(message)

        # Open the file in binary mode to send the data
        with open(userChoice, 'rb') as file:
            # Loop to send the file data in chunks
            while True:
                # Read file data in chunks (1024 bytes at a time)
                fileData = file.read(1024)

                # If no more data is read, break out of the loop
                if not fileData:
                    break

                # Send the chunk of file data to the server
                clientSocket.send(fileData)
            
        # Receive the confirmation message
        length = int(clientSocket.recv(4).decode('ascii'))
        message = clientSocket.recv(length).decode('ascii')
        print(message)

    # Issues with the file
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")

    except Exception as e:
        print(f"An error occurred: {e}")





## Call the client function when program is run
if __name__ == '__main__':
    client()