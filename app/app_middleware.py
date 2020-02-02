class AppMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('middleware init!')

    def __call__(self, request):
        print('middleware call!')
        response = self.get_response(request)
        return response