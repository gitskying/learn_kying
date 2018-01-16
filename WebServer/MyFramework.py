import time

HTML_ROOT_DIR = "./html"


class Application(object):
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        path = environ["PATH_INFO"]
        if path.startswith("/static"):
            file_path = path[7:]

            if file_path == "/":
                file_path = "/index.html"

            try:
                file = open(HTML_ROOT_DIR + file_path, "rb")
            except IOError:

                status_code = "404 Not Found"
                response_headers = [("Server", "MyServer"), ("Content-Type", "text")]
                start_response(status_code, response_headers)
                return b"file not exist"
            else:
                file_data = file.read()
                file.close()

                status_code = "200 OK"
                response_headers = [("Server", "MyServer"), ("Content-Type", "text/html")]
                start_response(status_code, response_headers)
                return file_data
        else:
            for view_path, view_fun in self.urls:
                if view_path == path:
                    response_body = view_fun(environ, start_response)
                    return response_body.encode()
            status_code = "404 Not Found"
            response_headers = [("Server", "MyServer"), ("Content-Type", "text")]
            start_response(status_code, response_headers)
            return b"program not exist"


def say_ctime(environ, start_response):

    status_code = "200 OK"
    response_headers = [("Server", "MyServer"), ("Content-Type", "text")]
    start_response(status_code, response_headers)
    return time.ctime()


def say_hello(environ, start_response):

    status_code = "200 OK"
    response_headers = [("Server", "MyServer"), ("Content-Type", "text")]
    start_response(status_code, response_headers)

    return "hello " + str(time.time())


urls = [("/say_ctime", say_ctime), ("/hello", say_hello)]

app = Application(urls)
