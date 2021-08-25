from socket import *
port_num=int(input("please insert the server port number:"))
ip=str(input("please insert the server ip address:"))
addr=(ip,port_num)
while True:
    client_socket = socket( AF_INET , SOCK_DGRAM )
#this loop to start the data exchange process
    try:    
        while True:
            user_input = input("Say somthing to the server : ")
            client_socket.sendto( user_input.encode(),addr )
#the termination ofconnection condition 
            if user_input == "Exit":
                break
            server_data, addr = client_socket.recvfrom( 1024 )
            print( server_data.decode() )
    except:
        print("try another add please")      
client_socket.close()
