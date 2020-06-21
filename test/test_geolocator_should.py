import unittest
import azure.functions as func

from geolocator.getCoordinates import localize

class GeolocatorShould(unittest.TestCase):
    def test_getCoordinatesFromValidSpot(self):
        req = func.HttpRequest(
            method='GET',
            body=None,
            url='/api/getCoordinates',
            params={'spot': 'firenze'}
        )

        resp = localize(req)

        self.assertEqual(
            resp.get_body(),
            b'["firenze", 43.7698712, 11.2555757]',
        )
    
    def test_getCoordinatesFromValidSpotInRequestBody(self):
        req = func.HttpRequest(
            method='GET',
            body=b'{"spot":"firenze"}',
            url='/api/getCoordinates',
            params={}
        )
        
        resp = localize(req)

        self.assertEqual(
            resp.get_body(),
            b'["firenze", 43.7698712, 11.2555757]',
        )
    
    def test_messageErrorFromInvalidSpot(self):
        req = func.HttpRequest(
            method='GET',
            body= None,
            url='/api/getCoordinates',
            params={'spot': 'invalid spot'}
        )

        resp = localize(req)

        self.assertEqual(
            resp.get_body(),
            b'invalid spot not found!',
        )

    def test_messageErrorFromNoParameters(self):
        req = func.HttpRequest(
            method='GET',
            body= b'',
            url='/api/getCoordinates',
            params={}
        )

        resp = localize(req)

        self.assertEqual(
            resp.get_body(),
            b'Please pass a spot on the query string or in the request body',
        )