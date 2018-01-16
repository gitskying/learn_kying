import time


def application(environ, start_response):
    status_code = "200 OK"
    response_headers = [("Server", "MyServer"), ("Content-Type", "text")]
    start_response(status_code, response_headers)

    return time.ctime()