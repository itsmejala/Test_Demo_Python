import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )




@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == 'chrome':
        driver = webdriver.Chrome(executable_path=r"E:\\DataSciencePython\\Pycharm\\pythonProject\\python_selenium_19_30\\chromedriver_win32\\chromedriver.exe")
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(
        executable_path=r"E:\\DataSciencePython\\Pycharm\\pythonProject\\python_session_14_00\\selenium_practie\\geckodriver-v0.29.0-win64\\geckodriver.exe")
    else:
        driver = webdriver.Ie()

    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver =  driver

    yield

    driver.close()


def getData():
    return [('jala','itsmejala@gmail.com','1234424','Female')]


@pytest.fixture(params=getData())
def data(request):
    return request.param