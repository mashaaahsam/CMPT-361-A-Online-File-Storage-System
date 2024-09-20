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
def client():
    # Get the serverName from the user
    serverName = input('Enter the server name or IP address: ') # localhost = '127.0.0.1' 

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



## Call the client function when program is run
if __name__ == '__main__':
    client()