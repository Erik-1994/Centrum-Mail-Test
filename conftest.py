from pytest import fixture
from selenium import webdriver
from config import Config

# env settings -----------------------------------------------------------------------------------------


def pytest_addoption(parser):
    parser.addoption("--env", action="store",
                     help="Environment to run tests against. (dev,qa)")


@fixture(scope='session')
def env(request):
    return request.config.getoption('--env')


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg


# mark fixtures -----------------------------------------------------------------------------------------
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
def chrome_driver(request):
    driver = request.param
    drvr = driver()
    drvr.implicitly_wait(10)
    drvr.maximize_window()
    return drvr
