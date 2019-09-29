import socket


def main(port_address=None):
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    # 2.链接服务器
    ip_address = input("请输入服务器ip地址:")
    port_address = int(input("请输入服务器端口port:"))
    connect_address = (ip_address, port_address)
    tcp_socket.connect(connect_address)

    # 3.发送数据

    send_msg = input("请输入要发送的数据:")
    tcp_socket.send(send_msg.encode("utf-8"))

    # 4.关闭套接字
    tcp_socket.close()
    pass

if __name__ == '__main__':
    main()