import conftest
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self):
        self.browser = conftest.browser

    def login(self, username, password):
        self.browser.find_element(By.NAME, "username").send_keys(username) 
        self.browser.find_element(By.NAME, "password").send_keys(password) 
        self.browser.find_element(By.ID, "btnLogin").click() 