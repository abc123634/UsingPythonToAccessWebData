import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8000))

#no need to incorporate domain name/port number again in the message
message = 'GET /index.html HTTP/1.0\n\n'

#use encoded message as socket parameter for the remote server to understand the request
s.send(message.encode('utf8'))

while True:
	data = s.recv(512)
	if len(data) < 1:
		break
	print (data)
s.close()