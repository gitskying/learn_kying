import socket
import select


PORT = 8080

listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

address = ("", PORT)
listen_sock.bind(address)
listen_sock.listen(128)

epoll = select.epoll()
epoll.register(listen_sock.fileno(), select.EPOLLIN)
sock_dict = {}

while 1:
    socket_fd_list = epoll.poll()
    # socket_fd_list == [(socket文件编号, 发生的行为epollin还是epollout 事件), (), ()]
    for sock_fd, event in socket_fd_list:
        if sock_fd == listen_sock.fileno():
            client_sock, client_addr = listen_sock.accept()
            print("客户端%s已连接" % (client_addr, ))
            sock_dict[client_sock.fileno()] = client_sock
            epoll.register(client_sock.fileno(), select.EPOLLIN)
        else:
            sock = sock_dict[sock_fd]
            recv_data = sock.recv(1024)
            if recv_data:
                print("客户端传来的数据: %s" % recv_data.decode())
            else:
                print("客户端已经关闭了连接")
                sock.close()
                epoll.unregister(sock_fd)
                del sock_dict[sock_fd]