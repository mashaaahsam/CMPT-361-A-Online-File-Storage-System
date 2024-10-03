"""
Short version of desc.

Detailed description...

authour: Maryia Antoshkina
"""

# IMPORTS
import socket
import sys
import json


# FUNCTIONS
"""
Purpose:
Parameters:
Returns:
"""
def server():
    # Server Port
    serverPort = 13000

    # Create the same server socket as the client
    try:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Error in server socket creation:", e)
        sys.exit(1)
    
    # Associate 13000 port number to the server socket
    try:
        serverSocket.bind(('', serverPort))
    except socket.error as e:
        print('Error in server socket binding: ', e)
        sys.exit(1)

    ## One Client Now Communicating With Server
    serverSocket.listen(1)

    while 1:
        try:
            #Server Accepts Client Connection
            connectionSocket, addr = serverSocket.accept()
            # print('\n**Debugging:',addr, '   ', connectionSocket, 'DELETE!!\n') # prints the successful connection for the server side to see

            # Start Communication
            #--------------------------------------------------------
            
            #Check user & close connection if user != user1
            IsValid = checkUser(connectionSocket)

            # User is approved - Enter menu
            serverMessage = ("\n\nPlease select the operation:\n"
                       "1) View uploaded files' information\n2) Upload a file"
                       "\n3) Terminate the connection\nChoice: ")
            
            # If the username is valid the server menu will show up
            while IsValid:
                # Get length of message with 4-figure 0 padding
                length = str(len(serverMessage)).zfill(4)
                connectionSocket.send(length.encode('ascii'))
                # Send message
                connectionSocket.send(serverMessage.encode('ascii'))

                userChoice = (connectionSocket.recv(2048).decode('ascii')).strip()

                if userChoice == '1':
                    pass
                
                # File Upload
                if userChoice == '2':
                    upload(connectionSocket)
                    
                # Termination
                if userChoice == '3':
                    exitMessage = 'exit'
                    connectionSocket.send('0004'.encode('ascii')) # Send length of message
                    connectionSocket.send(exitMessage.encode('ascii')) # Send exit message
                    connectionSocket.close()
                    break


            # Stop Communication
            #--------------------------------------------------------

        # Issues with the connection
        except socket.error as e:
            print('An error occured: ', e)
            sys.exit(1)
        except:
            print('Goodbye')
            sys.exit(0)
    
    


# Helper Functions

"""
Purpose:
Parameters:
Returns:
"""
def checkUser(connectionSocket):
    # Prepare message and send to user
    checkMessage = "\nWelcome to our system.\nEnter your username: "
    length = str(len(checkMessage)).zfill(4)
    connectionSocket.send(length.encode('ascii'))
    connectionSocket.send(checkMessage.encode('ascii'))

    # Receive a reply
    userInput = connectionSocket.recv(2048).decode('ascii').strip()

    if userInput == 'user1':
        return True
    else:
        exitMessage = 'incorrectUserName'
        connectionSocket.send('0017'.encode('ascii')) # Send length of message
        connectionSocket.send(exitMessage.encode('ascii')) # Send exit message
        connectionSocket.close() # close connection for that user
        return False


"""
Purpose:
Parameters:
Returns:
"""
def upload(connectionSocket):
    try:
        uploadMessage = "Please provide the file name: "
        length = str(len(uploadMessage)).zfill(4)
        # Send the length and upload message
        connectionSocket.send(length.encode('ascii'))
        connectionSocket.send(uploadMessage.encode('ascii'))

        # Get file name and size
        fileInfo = connectionSocket.recv(2048).decode('ascii')

        # Split the fileName and size
        fileName, fileSize = fileInfo.split('  :::  ')
        fileSize = int(fileSize)

        #!DEBUGGING
        # print(f'FileName: {fileName}, fileSize: {fileSize}')

        # Send OK size message
        okMessage = f'OK{fileSize}'
        length = str(len(okMessage)).zfill(4)
        connectionSocket.send(length.encode('ascii'))
        connectionSocket.send(okMessage.encode('ascii'))

        bytesLeft = fileSize
        receivedData = b'' # Store all the received as binary data and not as a string

        while bytesLeft > 0:
            # Get a chunk
            # If bytes left is smaller than 1024 recv it, else receive upto 1024
            chunk = connectionSocket.recv(min(1024, bytesLeft))

            # Add chunk to the binary string & decrement the bytesLeft by its length
            receivedData += chunk
            bytesLeft -= len(chunk)

        # Done receiving -> wb into a json file
        # Check that it's not empty
        if receivedData:
            newName = f'{fileName} - NEW'
            # Save the file to the server's directory
            with open(newName, 'wb') as file:
                file.write(receivedData)

            # Send confirmation message
            receivedMessage = "Upload Process Successful"
            length = str(len(receivedMessage)).zfill(4)
            connectionSocket.send(length.encode('ascii'))
            connectionSocket.send(receivedMessage.encode('ascii'))  

            # Update the json file
            update()

        else:
            # send failure message
            failedMessage = "File Failed to Send"
            length = str(len(failedMessage)).zfill(4)
            connectionSocket.send(length.encode('ascii'))
            connectionSocket.send(failedMessage.encode('ascii'))

    # Failed somewhere in the upload
    except Exception as e:
        failedMessage = f"An error occurred: {e}"
        length = str(len(failedMessage)).zfill(4)
        connectionSocket.send(length.encode('ascii'))
        connectionSocket.send(failedMessage.encode('ascii'))


"""
Purpose:
Parameters:
Returns:
"""
def update():
    pass

"""
Purpose:
Parameters:
Returns:
"""



## Call the server function when program is run
if __name__ == '__main__':
    server()