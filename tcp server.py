
#........................the server socket initialaizing
from socket import *
#building the object from socket
server_socket = socket()
#our server adress
server_socket.bind( ( 'localhost',1000) )
#five client socket in queue
server_socket.listen(5)
while True :
        print("server is waiting for aclient ....")
        (client_socket , client_addr)=server_socket.accept()
        print("client is connected from address",client_addr)
#........................starting the transmit/recive process between server and client
        while True :
                print("server is waiting for a message....")
                client_data= client_socket.recv(1024).decode()
        #the conition for exiting from current session and the server back the waiting state
                if client_data =="Exit":
                    print("\n connection has finished with the current client" ,client_addr ,"\n")
                    client_socket.close()
                    break
                print("client",client_addr," say:" , client_data )
        #the echo process
                client_data_back = client_data.encode()
                client_socket.send( client_data_back )


