#!/usr/bin/env python3
import unittest
import app

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_root(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

    def test_hello(self):
        rv = self.app.get('/hello/')
        self.assertEqual(rv.status, '200 OK')

    def test_user(self):
        name = "Simon"
        rv = self.app.get(f'/hello/{name}')
        self.assertIn(name.encode(), rv.data)

if __name__ == '__main__':
    unittest.main()