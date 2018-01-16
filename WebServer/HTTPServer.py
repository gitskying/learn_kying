import socket
import re
import MyFramework

from multiprocessing import Process


class HTTPServer(object):
    def __init__(self, app):
        self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.app = app

    def bind(self, port):
        address = ("", port)
        self.listen_sock.bind(address)

    def start_response(self, status_code, response_headers):
        resp_start_line = "HTTP/1.0 " + status_code + "\r\n"  # 起始行
        # 遍历处理response_headers,形成响应头
        resp_headers = ""
        for header_name, header_value in response_headers:
            resp_headers += (header_name + ": " + header_value + "\r\n")
        # 将拼接好的响应报文前半部分保存
        self.resp_start_line_headers = resp_start_line + resp_headers

    def handle_client(self, c_sock, c_addr):
        http_req_data = c_sock.recv(1024)
        print("客户端 %s 发送的HTTP请求报文:\n %s" % (c_addr, http_req_data.decode()))

        http_req_data_str = http_req_data.decode()
        req_start_line = http_req_data_str.split("\r\n")[0]

        match_result = re.match(r"(\w+) +(/\S*) +", req_start_line)
        req_method = match_result.group(1)
        file_path = match_result.group(2)
        environ = {
            "PATH_INFO": file_path,
            "REQUEST_METHOD": req_method
        }
        respones_body = self.app(environ, self.start_response)
        resp_data = (self.resp_start_line_headers + "\r\n").encode() + respones_body
        c_sock.send(resp_data)
        c_sock.close()

    def start(self):
        self.listen_sock.listen(128)
        while True:
            client_sock, client_addr = self.listen_sock.accept()
            print("客户端%s已连接" % (client_addr,))
            p = Process(target=self.handle_client, args=(client_sock, client_addr))
            p.start()
            # 释放client_sock
            client_sock.close()


if __name__ == '__main__':
    http_server = HTTPServer(MyFramework.app)
    http_server.bind(8080)
    http_server.start()
