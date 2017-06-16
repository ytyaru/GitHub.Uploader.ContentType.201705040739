import unittest
from Response import Response
class TestResponse_TDD(unittest.TestCase):
    def test_HasAttribute(self):
        self.assertTrue(hasattr(Response, 'Get'))
        self.assertTrue(hasattr(Response, 'Headers'))
        
