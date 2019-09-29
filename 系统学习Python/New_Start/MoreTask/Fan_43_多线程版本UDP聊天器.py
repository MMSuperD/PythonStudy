import socket
import threading

data_address_ip = None
data_address_port = None


def send_message(udp_socket):
    """发送数据"""
    global data_address_port
    global data_address_ip
    while True:
        # 这里是发送数据
        if data_address_port is not None:
            print("", end="\n")
            send_content = input("\n请输入要发送的数据:").encode("utf-8")
            udp_socket.sendto(send_content, (data_address_ip,int(data_address_port)))



def recvf_message(udp_socket):
    """接收数据"""
    global data_address_port
    global data_address_ip
    while True:
        # 3.接收数据,发送数据
        data = udp_socket.recvfrom(1024)  # 接收数据  (b'I love you', ('10.2.150.139', 4555))
        data_content = data[0].decode("utf-8")
        data_address_ip, data_address_port = data[1]
        print("\n收到的数据为:" + data_content, end="\n")



def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定端口
    local_address = ("", 7788)
    udp_socket.bind(local_address)

    # 创建线程1 用来接收数据
    th1 = threading.Thread(target=recvf_message, args=(udp_socket,))
    # 创建线程2 用来发送数据
    th2 = threading.Thread(target=send_message, args=(udp_socket,))

    th1.start()
    th2.start()

    while True:
        pass

    # 4.关闭套接字
    upd_socket.close()


if __name__ == '__main__':
    main()
