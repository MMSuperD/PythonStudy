import socket

def main():

	#创建一个udp 套接字
	#第一个参数表示ipv4,第二个参数表示 UDP
	upd_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	#可以使用套接字收发数据
	upd_socket.sendto(b"hahahahahah",("10.167.153.38",8888))

	print("032323")
	#关闭套接字
	upd_socket.close()

	print("032323")

	print("hah")

	if "":
		print("I love you")
	else:
		print("Thank you very much")


main()