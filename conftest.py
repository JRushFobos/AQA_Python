import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver(request):
    headless = request.config.getoption("--headless")
    if headless:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver_service = None
    else:
        driver_service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=driver_service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")
