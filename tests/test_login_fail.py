import csv
from pkgutil import get_data
from selenium.webdriver.common.by import By
import pytest
from pages.invoice_list_page import InvoiceListPage
from pages.login_page import LoginPage
import conftest


def load_incorrect_login_data():
    with open('resources/IncorrectUsers.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader] 

@pytest.mark.usefixtures("setup_and_teardown")
class TestTC002:
    #Get the information provided in the expected CSV file
    @pytest.mark.parametrize("get_data", load_incorrect_login_data())
    def test_login_negative(self, get_data):
        
        #browser = conftest.browser
        login_page = LoginPage ()
        invoice_list_page = InvoiceListPage ()

        #reference the columns from the file
        username = get_data['username']
        password = get_data['password']
    
        login_page.login(username, password)
        invoice_list_page.validate_login_fail()
