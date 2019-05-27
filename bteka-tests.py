from main import app

import unittest


class BooksTests(unittest.TestCase):
    def test_get_books(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/books", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'"test"\n')


if __name__ == "__main__":
    unittest.main()
