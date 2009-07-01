from httpstatus import Http405

def postonly(func):
    def decorator(request, *args, **kwargs):
        if not request.POST:
            raise Http405(['POST'])
        func(request, *args, **kwargs)
    return decorator

def getonly(func):
    def decorator(request, *args, **kwargs):
        if not request.GET:
            raise Http405(['GET'])
        func(request, *args, **kwargs)
    return decorator
