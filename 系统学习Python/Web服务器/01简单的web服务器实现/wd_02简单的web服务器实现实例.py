import socket
import  re

def service_client(new_socket,count):
    """服务客户端发过来的请求"""
    #1.这个是客户端发过来的请求
    request = new_socket.recv(1024).decode("utf-8")
    # print(request)
    #1.1 分割字符串得到我们想要的 GET / HTTP/1.1
    request_line = request.splitlines()
    print("")
    print(">"*20)
   # print(request_line)
    #1.2 通过正则表达式得到我们想要的请求路径
    ret = re.match(r"[^/]+(/[^ ]*)",request_line[0])

    if ret:
        print(ret.group(1))
    else:
        print("没有匹配到相应的路径")


    #2.服务器这边根据客户端发过来的请求做相应处理事情
    #2.1 拼接请求头 header
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"  #这句话是为了换行,客户端那可边根据这个换行来得到响应体body
    #2.2 拼接请求体 body

    #2.3 这里准备发送给浏览器的数据 body
    #response += "<h1>Hello Python world!</h1>"
    f = open("/Users/sh-lx/Desktop/Github/PythonBase/系统学习Python/HTMLE_Source/Taobao.html","rb")
    html_content = f.read()
    f.close()



    #3. 发送数据到客户端(浏览器)
    #3.1 将请求头发送给客户端
    new_socket.send(response.encode("utf-8"))
    #3.2 将请求体(内容发送给客户端)
    new_socket.send(html_content)

    #4. 关闭套接字
    new_socket.close()

    #print("第 %d 请求" % count)

def main():
    """用来完成整体的控制"""
    #1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #防止服务器关闭,绑定端口问题
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    #2.绑定端口
    tcp_server_socket.bind(("",3456))

    #3.把套接字变为监听套接字
    tcp_server_socket.listen(128)

    count = 0

    while True:
        print("等待 客户端发送链接:")
        #4.等待客户端连接
        new_socket,client_add = tcp_server_socket.accept()
        count += 1
        #5.为客户端服务
        service_client(new_socket,count)

    # 6.关闭监听套套接字
    tcp_server_socket.close()

if __name__ == '__main__':
    main()