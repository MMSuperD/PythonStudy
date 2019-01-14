import	socket

import sys


def main():
	 #创建套接字
	 udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	 #绑定端口地址
	 address_port = ("",9998)
	 udp_socket.bind(address_port)

	 #请用户输入ip 地址
	 dest_ip = input("input ip: ")
	 dest_port = int(input("input port: "))

	 while True:
	 	 #请输入要发送的消息
	 	 send_msg = input("input message: ")

	 	 #发送消息
	 	 udp_socket.sendto(send_msg.encode("utf-8"),(dest_ip,dest_port))

	 	 #接收消息

	 	 recv_data = udp_socket.recvfrom(1024)

	 	 #处理接收到的消息
	 	 print(recv_data)

	 udp_socket.close()


main()

