import unittest

from splinter import Browser
from flask.ext.testing import LiveServerTestCase

from welcome_home import app


# This test class spawns an app process and handles its cleanup.
class WelcomePeopleTestCase(LiveServerTestCase):
    def create_app(self):
        self.PORT = 5011
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = self.PORT
        return app

    def setUp(self):
        self.browser = Browser()
        self.URL_BASE = "http://localhost:{0}".format(self.PORT)

    def tearDown(self):
        self.browser.quit()

    def test_welcome_text_tag_name(self):
        url = "{0}{1}".format(self.URL_BASE, "/")
        self.browser.visit(url)
        welcome = self.browser.find_by_id("welcome")
        self.assertEqual(welcome.tag_name, "p")


if __name__ == '__main__':
    unittest.main()
