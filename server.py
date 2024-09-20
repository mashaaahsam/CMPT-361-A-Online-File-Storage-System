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
            #! print('\n**Debugging:',addr, '   ', connectionSocket, 'DELETE!!\n') # prints the successful connection for the server side to see

            # Start Communication
            #--------------------------------------------------------


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


## Call the server function when program is run
if __name__ == '__main__':
    server()