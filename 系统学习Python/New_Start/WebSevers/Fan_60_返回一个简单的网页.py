import socket
import re
import os

current_dir = os.getcwd() + "/WebSource"

def serve_client(client_socket):
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


    try:
        path = current_dir + "/百度贴吧——全球最大的中文社区_files/" + source_path
        file = open(path, "r")
        content = file.read()
        # 1.响应头
        response_header = "HTTP/ 1.1 200 OK \r\n"
        response_header += "\r\n"
        # print("file=", file)
        # print("content", content)
    except Exception as result:
        print(result)
        response_header = "HTTP/ 1.1 404 fail \r\n"
        response_header += "\r\n"
        content = "没有找到资源"

    # 2.响应体
    response_body = content

    # 3.拼接
    response = response_header + response_body

    # 4.发送给客户端数据
    client_socket.send(response_header.encode("utf-8"))
    client_socket.send(response_body.encode("utf-8"))

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