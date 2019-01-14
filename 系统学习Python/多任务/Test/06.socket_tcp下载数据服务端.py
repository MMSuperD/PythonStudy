
import socket


def main():
	 #1.创建套接字
	 socket_tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	 #2.绑定本地信息
	 add = ("",3005)
	 socket_tcp_server.bind(add)

	 #3.socket 由主动变为被动(listen)
	 socket_tcp_server.listen()

	 while True:
	 	print("witing...")
	 	#4.等待客户端连接 accpet
	 	new_client_socket,client_addr = socket_tcp_server.accept()

	 	print(client_addr)
	 	print("witing sent data give server")
	 	recv_data = new_client_socket.recv(1024)

	 	if recv_data:
	 		new_client_socket.send("I love you".encode("utf-8"))
	 	else:
	 		break

	 	new_client_socket.close()
	 	print("once time finish")

		# new_client_socket.close()
		# print("once time finshi")

	 socket_tcp_server.close()






if __name__ == '__main__':
	main()