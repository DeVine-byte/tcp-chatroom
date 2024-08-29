import socket

# create client parameter

client = socket.socket()
client_name = socket.gethostname()
client_ip = socket.gethostbyname(client_name)
port = 8080
print("IP address: ", client_ip)

# connect to server
user = input("[+] Enter your name: ")
server_con = input("[+]Enter server IP: ")
client.connect((server_con, port))

client.send(user.encode())
server_name = client.recv(1024)
server_name.decode()
print(server_name, "connected")

#send and receive message
while True:
	msg = (client.recv(1024).decode())
	print(server_name, ": ", msg)
	msg = input("message: ")
	client.send(msg.encode())
