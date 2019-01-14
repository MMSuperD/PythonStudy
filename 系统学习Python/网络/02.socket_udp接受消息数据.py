
import socket

import sys
# #sys.reload(sys)
# sys.setdefaultencoding( "utf-8" )

def main():
	#1.创建套接字
	upd_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	print("recive data start:")
	#2.绑定本地信息
	localaddr = ("",7778)
	upd_socket.bind(localaddr)

	while True:
		 #3.接受数据
		 recv_data = upd_socket.recvfrom(1024)
		 recv_msg = recv_data[0] #存储接受的数据
		 send_addr = recv_data[1] #存储发送方的地址信息
		 #4.打印接受数据
		 print(recv_data)
		 print("%s:%s" % (str(send_addr),recv_msg.decode("utf-8")))
	


	#5.关闭套接字
	upd_socket.close()


if __name__ == '__main__':
	main()