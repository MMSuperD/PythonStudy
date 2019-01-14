import socket  #这个是网络的库
import threading  #这个是多线程的库
import time  #这个用来延迟,锁等对象创建

def send_msg(udp_socket,input_ip,input_port):
    """发送消息"""
    while True:
        input_msg = input("please input send msg:")
        udp_socket.sendto(input_msg.encode("utf-8"), (input_ip, input_port))


def recv_msg(upd_socket):
    """接受消息"""
    while True:
        recv_data = upd_socket.recvfrom(1024)
        print(recv_data)


def main():
    #1.创建socket UDP
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #2.创建本程序地址并绑定地址
    addr = ("",3333)
    udp_socket.bind(addr)

    #3.输入要发送的地址(ip 和 port)
    input_ip = input("input ip :")
    input_port = int(input("input port :"))

    #3.创建两个线程兑现(其实这里只是一个对象,还没有创建对象,只是关联了响应事件),一个线程用于接受信息展示信息,一个线程用于发送信息
    threading_recv = threading.Thread(target=recv_msg,args=(udp_socket,))
    threading_send = threading.Thread(target=send_msg,args=(udp_socket,input_ip,input_port,))

    #4.在主线程中开启两个子线程
    threading_recv.start()
    threading_send.start()



if __name__ == '__main__':
    main()