import socket

def main():
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定本地信息
    tcp_socket.bind(("10.2.204.193", 5566))

    # 3.监听端口
    tcp_socket.listen(128)  # 这里监听128 暂时固定死

    # 4.接收消息
    while True:  #循环服务多个客户

        print("一个新的客户来袭:")
        new_socket, client_address = tcp_socket.accept()  #这里是等待客户端来链接

        while True:  # 这里是循环服务一个客户,可能有多个问题

            # 4.1接收到客户端发过来的消息
            # recv 解堵塞有两种情况
            # 1.客户端端来链接也就是调用close()
            # 2.客户端发送了非空的信息(客户端不能发送空的信息)
            client_msg = new_socket.recv(1024)  # 这里是客户端发送过来的消息
            if client_msg:
                new_socket.send(b"Hello, I am sever")
                print(client_msg.decode("utf-8"))
            else:
                break

        new_socket.close()

    tcp_socket.close()

if __name__ == '__main__':
    main()