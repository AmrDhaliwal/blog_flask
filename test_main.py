import os
import unittest
from main import app, get_all_posts


class TestResponse(unittest.TestCase):
    def test_get_all_posts(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


if __name__ == '__main__':
    unittest.main()
