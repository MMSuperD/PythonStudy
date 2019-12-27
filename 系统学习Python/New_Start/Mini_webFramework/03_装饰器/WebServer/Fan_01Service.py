import socket
import re
import os
import sys
import threading


current_dir = os.getcwd() + "/WebServer"

print(os.getcwd())
print(current_dir)


class Service(object):
    """服务器对象"""

    def __init__(self, port, app):

        # 功能模块函数
        self.app = app

        # 1.创建套接字
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 1.1 close 调用两分钟后,端口被占用
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2.绑定端口
        self.tcp_socket.bind(("", port))

        # 3.监听接口
        self.tcp_socket.listen(128)

    def startService(self):
        """开启服务器"""
        while True:
            # 4.等待新客户端连接
            print("等待新的客户端连接:")
            client_socket, address = self.tcp_socket.accept()
            print(str(address), "连接成功")

            # 5.为客户服务
            p = threading.Thread(target=self.serve_client, args=(client_socket,))
            p.start()

        # 6.关闭套接字
        self.tcp_socket.close()

    def set_response_header(self, status, response_header):
        """设置请求header"""
        # 这两个是实例属性
        self.status = status
        self.response_header = response_header
        pass


    def serve_client(self, client_socket):
        """服务用户"""
        # 1.接收到客户端发送的请求,并解码
        request = client_socket.recv(1024).decode("utf-8")

        # 2.分割字符串

        request_lines = request.splitlines()
        # print(request_lines)
        print(">>>>" * 50)
        # 3.匹配路径
        source_path = re.match(r"[^/]+/([^ ]*)", request_lines[0]).group(1)
        if source_path:
            print("资源路径:", source_path)
            pass
        else:
            source_path = "index.htm"
            pass

        response_header = ""
        content = ""
        eva = dict()  # 创建一个空字典
        eva["source_path"] = source_path
        #调用功能web框架得到相应的资源
        content = self.app(eva, self.set_response_header)

        # 这个是响应头
        response_header = "HTTP/ 1.1 %s \r\n" % self.status

        for temp in self.response_header:
            response_header += "%s:%s\r\n" % (temp[0], temp[1])

        response_header += "\r\n"

        print("response_header" + response_header)

        # 响应体
        response_body = content

        # 3.拼接
        response = response_header + response_body

        # 4.发送给客户端数据
        client_socket.send(response_header.encode("utf-8"))
        client_socket.send(response_body.encode("utf-8"))

        # 5.关闭套接字
        client_socket.close()


def main():
    """程序入口"""
    # 控制一个整体,需要相应的参数才可以运行,这个服务器,否者就不能运行该服务器(比如端口 ,资源文件这些值都不能固定死)
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[1])  # 得到端口号
            frame_app_name = sys.argv[2]  # 得到资源名字,也就是框架名字
        except Exception as ret:
            print("端口输入错误")
            return

    else:
        print("请按照以下方式运行:")
        print("python3 xxxx.py 7788 mini_frame:application")
        return

    print(frame_app_name)
    ret = re.match(r"([^:]+):(.*)", frame_app_name)
    print(ret.group(1))
    if ret:
        frame_name = ret.group(1)  # 得到资源名字
        app_name = ret.group(2)  # 得到application 也就是配置函数的名字(接口名字)

        print(frame_name + " " + app_name)
    else:
        print("请按照以下方式运行:")
        print("python3 xxxx.py 7788 mini_frame:application")
        return

    # 这里就要导入资源
    frame = __import__(frame_name)  # 返回导入的模块
    app   = getattr(frame,app_name)  # 得到这个函数
    print("*" * 50)
    print(frame)
    print("*" * 50)
    print(app)
    print("*" * 50)

    service = Service(port,app)
    service.startService()


if __name__ == '__main__':
    main()
