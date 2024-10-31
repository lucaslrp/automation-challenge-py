import csv
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import conftest
from pages.invoice_list_page import InvoiceListPage
from pages.login_page import LoginPage
from pages.invoice_details_page import InvoiceDetailsPage


def load_login_data():
    with open('resources/CorrectUser.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader] 

def load_invoice_data():
    with open('resources/InvoiceData.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
        

@pytest.mark.usefixtures("setup_and_teardown")
class TestTC003:
    #Get the information provided in the expected CSV file
    @pytest.mark.parametrize("get_data", load_login_data())
    @pytest.mark.parametrize("invoice_data", load_invoice_data())
    def test_invoice_details(self, invoice_data, get_data):
        
        browser = conftest.browser
        login_page = LoginPage ()
        invoice_list_page = InvoiceListPage ()
        invoice_details_page = InvoiceDetailsPage ()
        #reference the columns from the file
        username = get_data['username']
        password = get_data['password']

        login_page.login(username, password)
        #reference the columns from the file
        hotel_name = invoice_data['HotelName']
        invoice_date = invoice_data['InvoiceDate']
        due_date = invoice_data['DueDate']
        invoice_number = invoice_data['InvoiceNumber']
        booking_code = invoice_data['BookingCode']
        customer_details = invoice_data['CustomerDetails']
        room = invoice_data['Room']
        check_in = invoice_data['CheckIn']
        check_out = invoice_data['CheckOut']
        total_stay_count = invoice_data['TotalStayCount']
        total_stay_amount = invoice_data['TotalStayAmount']
        deposit_now = invoice_data['DepositNow']
        tax_vat = invoice_data['Tax&VAT']
        total_amount = invoice_data['TotalAmount'] 
        
         #============================= Login =============================

        invoice_list_page.validate_login()
    
        invoice_list_page.open_invoice_details()
    
        #============================= Hotel Name =============================

        invoice_details_page.get_hotel_name_info(hotel_name)

        #============================= Invoice Date =============================

        invoice_details_page.get_hotel_invoice_date(invoice_date)

        #============================= Due Date =============================

        invoice_details_page.get_hotel_due_date(due_date)

        #============================= Invoice Number =============================

        invoice_details_page.get_invoice_number(invoice_number)

        #============================= Booking Code =============================

        invoice_details_page.get_booking_code_info(booking_code)

        #============================= Room =============================

        invoice_details_page.get_room_info(room)

        #============================= Total Stay Count =============================

        invoice_details_page.get_total_stay_account_info(total_stay_count)

        #============================= Total Stay Amount =============================

        invoice_details_page.get_total_stay_amount_info(total_stay_amount)

        #============================= Check-in =============================

        invoice_details_page.get_checkin_info(check_in)

        #============================= Check-Out =============================

        invoice_details_page.get_checkout_info(check_out)

        #============================= Customer Details =============================

        invoice_details_page.get_customer_details_info(customer_details)

        #============================= Deposit Now =============================

        invoice_details_page.get_deposit_now_info(deposit_now)

        #============================= Tax & VAT =============================

        invoice_details_page.get_taxAndVat_info(tax_vat)

        #============================= Total Amount =============================

        invoice_details_page.get_total_amount_info(total_amount)


        time.sleep(8)