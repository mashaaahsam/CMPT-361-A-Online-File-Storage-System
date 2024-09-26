"""
Short version of desc.

Detailed description...

authour: Maryia Antoshkina
"""

# IMPORTS
import socket
import sys


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
            print('\n**Debugging:',addr, '   ', connectionSocket, 'DELETE!!\n') # prints the successful connection for the server side to see

            # Start Communication
            #--------------------------------------------------------
            
            #Check user
            IsValid = checkUser(connectionSocket)
            if not IsValid:
                # Send exit message
                exitMessage = 'exit'
                connectionSocket.send('0004'.encode('ascii')) # Send length of message
                connectionSocket.send(exitMessage.encode('ascii')) # Send exit message
                connectionSocket.close() # close connection for that user


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
    checkMessage = "Welcome to our system.\nEnter your username: "
    length = str(len(checkMessage)).zfill(4)
    connectionSocket.send(length.encode('ascii'))
    connectionSocket.send(checkMessage.encode('ascii'))

    # Receive a reply
    userInput = connectionSocket.recv(2048).decode('ascii').strip()

    if userInput == 'user1':
        return True
    else:
        return False


"""
Purpose:
Parameters:
Returns:
"""



## Call the server function when program is run
if __name__ == '__main__':
    server()