from django.http import HttpResponseNotAllowed, HttpResponseForbidden


class HTTPStatusException(Exception):
    pass


class Http403(HTTPStatusException):
    def get_response(self):
        return HttpResponseForbidden()


class Http405(HTTPStatusException):
    def __init__(self, allowed_methods):
        self.allowed_methods = allowed_methods

    def get_response(self):
        return HttpResponseNotAllowed(self.allowed_methods)

