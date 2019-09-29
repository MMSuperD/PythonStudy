
import socket

def main():
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定本地信息
    tcp_socket.bind(("10.2.204.193", 5566))

    # 3.监听端口
    tcp_socket.listen(128)  # 这里监听128 暂时固定死

    # 4.接收消息
    new_socket, client_address = tcp_socket.accept()  #这里是等待客户端来链接

    # 4.1接收到客户端发过来的消息
    client_msg = new_socket.recv(1024)  # 这里是客户端发送过来的消息
    print(client_msg.decode("utf-8"))
    # 5.发送消息
    new_socket.send(b"Hello, I am sever")

    # 6.关闭套接字
    new_socket.close()
    tcp_socket.close()

if __name__ == '__main__':
    main()