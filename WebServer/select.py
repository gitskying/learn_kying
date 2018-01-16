# coding=utf-8
import socket
import select


PORT = 8080

listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

address = ("", PORT)
listen_sock.bind(address)

listen_sock.listen(128)

input_sock_list = [listen_sock]


while 1:
    recv_accept_sock_list, send_sock_list, exception_sock_list = select.select(input_sock_list, [], [])
    for sock in recv_accept_sock_list:
        if sock == listen_sock:
            client_sock, client_addr = sock.accept()
            print("客户端%s 已连接" % (client_addr,))
            input_sock_list.append(client_sock)
        else:
            recv_data = sock.recv(1024)
            if recv_data:
                print("客户端传来了数据: %s" % recv_data.decode())
            else:
                print("客户端关闭了连接")
                sock.close()
                input_sock_list.remove(sock)
