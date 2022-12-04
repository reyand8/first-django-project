import pytest
from django.test import LiveServerTestCase
from selenium import webdriver


@pytest.mark.usefixtures("driver_init")
class Test_URL_Chrome:
    def test_open_url(self, live_server):
        self.driver.get(("%s%s" % (live_server.url, "/about/")))
        assert "About us" in self.driver.title
