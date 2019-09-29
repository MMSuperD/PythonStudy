
import socket

def main():

    # 1.创建套接字
    upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定端口(自己的IP,和端口)
    local_address = ("", 7878)
    upd_socket.bind(local_address)
    # 3.接收数据
    while True:
        data_text = upd_socket.recvfrom(1024)  # 每次最多接收1024个字符
        # 4.解析数据 并输出
        # data_msg = data_text[0].decode("utf-8")  # 如果是windows 来哦数据需要gbk来解析数据
        data_msg = data_text[0].decode("gbk")
        data_address = data_text[1]
        print("%s %s" % (data_address, data_msg))
    # 5.关闭套接字
    upd_socket.close()

if __name__ == '__main__':
    main()