from django.test import TestCase
from django.http import HttpResponsePermanentRedirect
from httpstatus import Http301

class HTTPStatusTests(TestCase):

    def test_Http301(self):
        """Test that a HttpResponsePermanentRedirect response is generated."""
        try:
            raise Http301('http://foo.com')
        except Http301 as inst:
            import pdb; pdb.set_trace()
            self.assertEquals(HttpResponsePermanentRedirect,
                              type(inst.get_response()))
