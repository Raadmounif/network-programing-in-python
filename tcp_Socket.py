import socket
import sys
if __name__ == '__main__':
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print("Failed to crate a socket")
        print("Reason: " , err  )
        sys.exit()
    
    print('Socket created')
    target_host = input("Enter the target host name to connect: ")
    target_port = int( input("Enter the target port: "))
    
    try:
        sock.connect((  target_host ,  target_port  ))
        print("Socket Connected to {} on port: {}".format( target_host, target_port ) )
        sock.shutdown(2)
        
    except socket.error as err:
        print("Failed to connect to {} on port: {}".format( target_host, target_port ) )
        print("Reason: " , err )
        sys.exit()









































