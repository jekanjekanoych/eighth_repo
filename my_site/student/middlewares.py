import time


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        request_method = request.method
        request_path = request.path
        execute_time = str(time.time() - start_time)

        with open("LogMiddleware.txt", "w", newline="") as file:
            file.writelines(f"{request_method}\n")
            file.writelines(f"{request_path}\n")
            file.writelines(f"{execute_time}\n")

        return response
