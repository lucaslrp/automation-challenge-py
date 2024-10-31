import pytest
from selenium import webdriver


#define browser variable globally.
browser: webdriver.Remote

@pytest.fixture
def setup_and_teardown():
    #setup
    global browser
    browser = webdriver.Chrome()
    browser.implicitly_wait(5) 
    browser.maximize_window()
    browser.get("https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/")

    #execute test
    yield

    #teardown
    browser.quit()