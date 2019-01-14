import socket


def main():
	#1.买一个手机(创建套接字)
	tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	#2.插入手机卡(绑定本地信息 bind)
	tcp_server_socket.bind(("",7891))


	#3.将手机设置为正常的响铃模式(让默认的套接字由主动变为被动 listen)
	tcp_server_socket.listen(128)

	while True:
		#4.等待别人的电话到来(等待客户端的连接(客户端调动connect) accept)
		new_client_socket,client_addr = tcp_server_socket.accept()
		print(client_addr)
		while True:
			#5.收到客户端发过来的请求
			recv_data = new_client_socket.recv(1024)

			#如果recv 解堵塞,那么有两种情况
			#1.第一种是客服端发送过来数据
			#2.第二种是客服端断开连接
			if recv_data:
				print(recv_data)
				#6.回复客户端
				new_client_socket.send("dfsfsada".encode("utf-8"))
			else:
				break
			
		
		#7.关闭套接字
		new_client_socket.close()

	tcp_server_socket.close()



if __name__ == '__main__':
	main()