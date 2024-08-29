## import server library

import socket

# define server parameter
server = socket.socket()
server_name = socket.gethostname()
server_ip = socket.gethostbyname(server_name)
server_port = 8080
print("Ip address: ", server_ip)

#bind ip address and listen for connections
server_bind = server.bind((server_ip, server_port))
print("[+]Binding server ip address sucessfull!")
user = input("[+]Enter your name: ")
server.listen(10)

#accept connections 
acpt, conn = server.accept()
print("[+]Connection recived: ", conn[0])

client = (acpt.recv(1024).decode())
print("[+]client connection established")
acpt.send(user.encode())


# sending and recieving messages

while True:
	msg = input("message: ")
	acpt.send(msg.encode())
	msg = acpt.recv(1024)
	msg = msg.decode()
	print(client, ": ", msg)



