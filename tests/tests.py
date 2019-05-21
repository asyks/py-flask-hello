
from unittest import TestCase

from py_flask_hello import hello, constants


class TestApp(TestCase):

    def setUp(self):
        self.client = hello.app.test_client()

    def test_index(self):
        test_resp = self.client.get("/")
        self.assertEqual(
            test_resp.data, constants.SUCCESS_MESSAGE.encode("utf-8")
        )
