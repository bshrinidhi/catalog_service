import unittest
from catalog.service import *
from catalog import catalog_app
from flask import request
class catalogTestCase(unittest.TestCase):
    def setUp(self):
        self.catalog_app = catalog_app.test_client()

    def test_get_catalog(self):
        response = self.catalog_app.get('/catalog')
        self.assertEqual(response.status_code,200)



if __name__ == '__main__':
    unittest.main()
