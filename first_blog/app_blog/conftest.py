import pytest
from pytest_factoryboy import register
from .factories import CategoryFactory, ReviewFactory
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service_chrome = Service("./chromedriver")
service_firefox = Service("./geckodriver")
register(ReviewFactory)
register(CategoryFactory)


@pytest.fixture
def new_user1(db, review_factory):
    user = review_factory.create()
    return user


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()

