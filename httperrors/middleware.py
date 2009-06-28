from django.http import HttpResponseNotAllowed
from httperrors import *

class HttpStatusErrorsMiddleware:
    def process_exception(self, request, exception):
        if not isinstance(exception, HTTPStatusException):
            return
        try:
            return exception.get_response()
        except:
            pass
