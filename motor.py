import socket
import struct


class motor:
	def __init__(self,address='192.168.0.116',port=8004):
	
		self.client_socket = socket.socket()
		self.client_socket.connect((address, port))
	def send_one_message(self,data):
		length = len(data)
		self.client_socket.sendall(struct.pack("!I",length))
		self.client_socketsendall(data.encode("utf-8"))
	def command(self,cmd,speed,duration):
		data=cmd+" "+str(speed)+" "+str(duration)
		self.send_one_message(data)
		
	def stop(self):
		self.client_socket.close()


while True:
	try:
		data = input("command speed duration")
		send_one_message(client_socket,data)
	except KeyboardInterrupt as e:
		print("ERROR: ",e)
		client_socket.close()
		break