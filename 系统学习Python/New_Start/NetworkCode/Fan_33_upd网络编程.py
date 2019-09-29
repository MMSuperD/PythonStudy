
# upd 网络编程
import socket

def main():
    """测试函数"""
    # 1.创建套接字(upd)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.创建发送数据参数  两个参数 第一个 是ip  第二个 :端口
    send_address = ("10.2.204.193", 8080)
    # 3.发送数据
    udp_socket.sendto(b"I love you", send_address)

    # 4.关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()




