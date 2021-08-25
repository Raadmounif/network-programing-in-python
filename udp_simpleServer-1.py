from socket import *
server_socket = socket( AF_INET , SOCK_DGRAM )
server_socket.bind( ( 'localhost',1000) )
#this loop to keep server in waiting mode
while True :
    print("server is waiting for new client")
#this loop to start the data exchange process 
    while True :
        print("server is waiting for message")    
        client_data , addr  = server_socket.recvfrom(1024)
#the termination ofconnection condition 
        if client_data.decode() == "Exit":
            break
        print("client say:" , client_data.decode() )
        server_socket.sendto( client_data , addr)



