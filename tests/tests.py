from unittest import TestCase

from py_flask_hello import hello, constants


class TestApp(TestCase):
    def setUp(self):
        self.client = hello.app.test_client()

    def test_get_index(self):
        test_resp = self.client.get("/")
        self.assertEqual(test_resp.status_code, 200)
        self.assertEqual(test_resp.data, constants.SUCCESS_MESSAGE.encode("utf-8"))

    def test_post_index(self):
        test_resp = self.client.post("/")
        self.assertEqual(test_resp.status_code, 405)

    def test_get_arbitrary_path(self):
        test_resp = self.client.get("/foo")
        self.assertEqual(test_resp.status_code, 404)

