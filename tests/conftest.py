import pytest
from selenium import webdriver
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope = "class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Browsers_Selenium\\Chrome\\ChromeDriver.exe")
    elif browser_name == "firefox":
        # firefox driver
        driver = webdriver.Firefox(executable_path="C:\\Browsers_Selenium\\Gecko\\geckodriver.exe")
    elif browser_name == "IE":
        # IE driver
        print('IE printed')

    driver.get("http://demo.testfire.net/index.jsp")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    #driver.close()
