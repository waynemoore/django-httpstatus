from django.test import TestCase
from django.http import *
from httpstatus import Http301, Http302, Http400, Http403, Http405, Http410
from httpstatus.decorators import postonly, getonly
from httpstatus.middleware import HttpStatusErrorsMiddleware

class MockRequest:
    POST = False
    GET = False


class HTTPStatusTests(TestCase):

    def test_Http301(self):
        """Test that a HttpResponsePermanentRedirect response is generated."""
        try:
            raise Http301('http://foo.com')
        except Http301, e:
            self.assertEquals(HttpResponsePermanentRedirect,
                              type(e.get_response()))
        else:
            self.fail()

    def test_Http302(self):
        """Test that a HttpResponseRedirect response is generated."""
        try:
            raise Http302('http://foo.com')
        except Http302, e:
            self.assertEquals(HttpResponseRedirect,
                              type(e.get_response()))
        else:
            self.fail()

    def test_Http400(self):
        """Test that a HttpResponseBadRequest response is generated."""
        try:
            raise Http400()
        except Http400, e:
            self.assertEquals(HttpResponseBadRequest,
                              type(e.get_response()))
        else:
            self.fail()

    def test_Http403(self):
        """Test that a HttpResponseBadRequest response is generated."""
        try:
            raise Http403()
        except Http403, e:
            self.assertEquals(HttpResponseForbidden,
                              type(e.get_response()))
        else:
            self.fail()


    def test_Http405(self):
        """Test that a HttpResponseNotAllowed response is generated."""
        try:
            raise Http405(['GET'])
        except Http405, e:
            self.assertEquals(HttpResponseNotAllowed,
                              type(e.get_response()))
        else:
            self.fail()


class DecoratorTests(TestCase):

    def test_postonly(self):
        req = MockRequest()

        try:
            @postonly
            def foo(request):
                self.fail('Should not have entered foo.')

            foo(req)
        except Http405:
            pass
        else:
            self.fail('Should have raised Http405')

        req = MockRequest()
        req.POST = True
        @postonly
        def foo(request):
            return HttpResponse('handled')
        response = foo(req)
        self.assertEquals(response.content, 'handled')

    def test_getonly(self):
        req = MockRequest()

        try:
            @getonly
            def foo(request):
                self.fail('Should not have entered foo.')

            foo(req)
        except Http405:
            pass
        else:
            self.fail('Should have raised Http405')

        req = MockRequest()
        req.GET = True
        @getonly
        def foo(request):
            return HttpResponse('handled')
        response = foo(req)
        self.assertEquals(response.content, 'handled')


class TestMiddleware(TestCase):
    def test_process_exception(self):
        middleware = HttpStatusErrorsMiddleware()
        exception = None
        try:
            raise Http400
        except Http400, e:
            req = MockRequest()
            response = middleware.process_exception(req, e)
            self.assertEquals(HttpResponseBadRequest, type(response))
        else:
            self.fail('Should not get here.')
