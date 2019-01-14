
import socket

def main():
	
	#1.创建套接字
	socket_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	#2.绑定本地端口
	address = ("",8813)
	socket_tcp.bind(address)

	#3.获取服务器地址
	address_ip = input("please input ip: ")
	address_port = int(input("please input port: "))

	#4.连接服务器
	socket_tcp.connect((address_ip,address_port))

	#4.1获取下载的文件名字
	download_filename = input("please input download file name: ")
	#5.将要下载的数据文件名字发给服务器
	socket_tcp.send(download_filename.encode("utf-8"))
	
	#6.接收服务器数据
	recv_data = socket_tcp.recv(1024)

	if recv_data:
		print(recv_data)
		print(download_filename)
		#7.保存接收到的数据到文件中去
		with open("new_" + download_filename,"wb") as f:
			f.write(recv_data)

	print("close")
	#8.关闭套接字
	socket_tcp.close()

if __name__ == '__main__':
	main()