
# upd 网络编程
import socket

def main():
    """测试函数"""
    # 1.创建套接字(upd)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.创建发送数据参数  两个参数 第一个 是ip  第二个 :端口
    send_address = ("10.2.204.193", 8080)

    flag = True  # 这个用来停止发送数据

    while flag:
        # 2.1 发送内容
        send_text = input("请输入要发送的内容(输入q结束发送):")

        if send_text == "q":
            flag = False
            break
        # 3.发送数据 # 必须这样编码否者不能够成功
        udp_socket.sendto(send_text.encode("utf-8"), send_address)

    # 4.关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
