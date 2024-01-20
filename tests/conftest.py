import logging

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from src.helpers.logger import Logger


def pytest_addoption(parser):
    parser.addoption("--browser", choices=["chrome", "firefox"])
    parser.addoption("--base_url", help="Base request URL")
    parser.addoption("--tolerance", type=int, default=3, help="Timeout value")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--logging_level", default="WARNING")


# browser/driver fixture
@pytest.fixture()
def browser(request, logger):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base_url")
    tolerance = request.config.getoption("--tolerance")

    logger.info(f"Test {request.node.name} started")

    match browser:
        case "chrome":
            browser_options = ChromeOptions()
            browser_options.add_argument("start_maximized")
            browser_options.add_argument("--window-size=1920,1080")
            browser_options.add_argument("--no-sandbox")
            browser_options.add_argument("--disable-dev-shm-size")

            if headless:
                browser_options.add_argument("--headless")

            driver = webdriver.Chrome(options=browser_options)
        case "firefox":
            browser_options = FirefoxOptions()

            if headless:
                browser_options.add_argument("-headless")

            driver = webdriver.Firefox(options=browser_options)
        case _:
            raise NotImplementedError("Not supported browser name")

    @allure.step("Go to {path}")
    def navigate_to(path=""):
        logger.info(f"{request.node.name} Go to {base_url} {path}")
        driver.get(base_url + path)

    driver.open = navigate_to
    driver.tolerance = tolerance
    driver.log_level = logging.getLevelName(logger.level)
    driver.logger = logger
    driver.test_name = request.node.name

    driver.open()

    def finalizer():
        if request.node.rep_call.failed:
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.node.name,
                          attachment_type=allure.attachment_type.PNG)

        driver.close()
        driver.quit()
        logger.info(f"Test {request.node.name} is finished")

    request.addfinalizer(finalizer)

    return driver


@pytest.fixture(scope="session")
def logger(request):
    log_level = request.config.getoption("--logging_level")

    return Logger(request.node.name, log_level).logger


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
