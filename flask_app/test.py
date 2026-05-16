#!/usr/bin/env python3
import unittest
import app

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

    def test_hello_hello(self):
        rv = self.app.get('/hello/')
        self.assertEqual(rv.status, '200 OK')

    def test_hello_name(self):
        name = "Simon"
        rv = self.app.get(f'/hello/{name}')
        self.assertIn(name.encode(), rv.data)

    # ✅ Test ajouté en TDD
    def test_new_route(self):
        name = "DevOps"
        rv = self.app.get(f'/feature/{name}')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(b'Feature', rv.data)

if __name__ == '__main__':
    unittest.main()