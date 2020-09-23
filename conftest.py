from pytest import fixture
from selenium import webdriver
from config import Config


@fixture()
def email_password():
    password = "test_Email"
    return password


@fixture()
def email_name():
    name = "test_pytest"
    return name


@fixture()
def email_test_code():
    code = "glum"
    return code


@fixture(scope="session", params=[webdriver.Chrome, webdriver.Edge, webdriver.Firefox])
def web_driver(request):
    driver = request.param
    drvr = driver()
    drvr.implicitly_wait(10)
    drvr.maximize_window()
    return drvr
