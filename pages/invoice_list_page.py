import conftest
from selenium.webdriver.common.by import By


class InvoiceListPage:
    def __init__(self):
        self.browser = conftest.browser

    def validate_login(self):
        #self.browser.find_element()
        assert self.browser.current_url == "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/account"

    def validate_login_fail(self):
        #self.browser.find_element()
        loginFailAlert = self.browser.find_element(By.XPATH, "//div[@role='alert' and contains(text(), 'Wrong username or password')]")
        loginFailMsg = loginFailAlert.text
        assert loginFailMsg == "Wrong username or password.", f"Actual: '{loginFailMsg}', Expected: 'Wrong username or password.'"
    
        #assert not self.browser.current_url == "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/account"

        #MUDAR VALIDAÇÃO

    def open_invoice_details(self):
        self.browser.find_element(By.XPATH, "/html/body/section/div/div[2]/div[5]/a").click()
        handles = self.browser.window_handles
        self.browser.switch_to.window(handles[-1])
        assert self.browser.current_url == "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/invoice/0"