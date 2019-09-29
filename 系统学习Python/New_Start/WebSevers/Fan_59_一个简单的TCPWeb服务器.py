import socket

def serve_client(client_socket):
    """服务用户"""
    # 接收到客户端发送的请求
    request = client_socket.recv(1024)
    print(request)

    # 返回给客户端的http 协议数据 由两部分组成
    # 1.响应头
    response_header = "HTTP/ 1.1 200 OK \r\n"
    response_header += "\r\n"

    # 2.响应体
    response_body = "<h1>I love you</h1>"

    # 3.拼接
    response = response_header + response_body

    # 4.发送给客户端数据
    client_socket.send(response.encode("utf-8"))

    # 5.关闭套接字
    client_socket.close()

    pass


def main():
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 1.1 close 调用两分钟后,端口被占用
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2.绑定端口
    tcp_socket.bind(("", 7788))

    # 3.监听接口
    tcp_socket.listen(128)

    while True:
        # 4.等待新客户端连接
        print("等待新的客户端连接:")
        client_socket, address = tcp_socket.accept()
        print(str(address), "连接成功")

        # 5.为客户服务
        serve_client(client_socket)

    # 6.关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()