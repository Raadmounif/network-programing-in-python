#........................the client socket initialaizing
from socket import *
client_socket = socket()
port_num=int(input("please insert the server port number:"))
ip=str(input("please insert the server ip address:"))
addr=(ip,port_num)
#........................starting the transmit/recive process between server and client
try:
    client_socket.connect(addr)
    while True:   
        client_input = input("Say somthing to the server: ")
        client_socket.send( client_input.encode() )
        if client_input == "Exit":        
            break
        server_data= client_socket.recv( 1024 ).decode()
        print( "the server say :" , server_data )
    print(" conection has finished ")
    client_socket.close()
except:
    print("try another add please ")
