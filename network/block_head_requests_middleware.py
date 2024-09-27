from django.http import HttpResponseNotAllowed

class BlockHeadRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'HEAD':
            return HttpResponseNotAllowed(['GET', 'POST'])
        return self.get_response(request)
