import unittest

import welcome_home


class WelcomePeopleTestCase(unittest.TestCase):
    def setUp(self):
        self.app = welcome_home.app.test_client()
        self.home = self.app.get('/')

    def test_home_status_code(self):
        self.assertEqual(self.home.status_code, 200)

    def test_home_contains_welcome_home_text(self):
        self.assertTrue("Welcome home!!" in self.home.get_data())


if __name__ == '__main__':
    unittest.main()
