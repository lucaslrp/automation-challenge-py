import csv

import pytest
import conftest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InvoiceDetailsPage:
    def __init__(self):
        self.browser = conftest.browser

    def change_tab(self):
        handles = self.browser.window_handles
        self.browser.switch_to.window(handles[-1])

    def get_hotel_name_info(self, hotel_name):
        InvoiceDetailsPage.change_tab(self)
        hotelNameInfo = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h4[@class='mt-5']"))) #tried first //h4[@class='mt-5'] - correct but failing
        hotelNameText = hotelNameInfo.text
        assert hotelNameText == (hotel_name), "Expected: 'Rendezvous Hotel', Actual: '{hotelNametext}'"

    def get_hotel_invoice_date(self, invoice_date):
        invoiceDateInfo = self.browser.find_element(By.XPATH, "//span[contains(text(), 'Invoice Date:')]")
        # gets the father element to get the whole text
        parentElement = invoiceDateInfo.find_element(By.XPATH, "..")
        # to get the text after the <span> that has "Invoice Date:", split and remove spaces
        invoiceDateText = parentElement.text.split("Invoice Date:")[1].strip()
        assert invoiceDateText == (invoice_date), "Expected: '14/01/2018', Actual: '{invoiceDateText}'"

    def get_hotel_due_date(self, due_date):
        dueDateInfo = self.browser.find_element(By.XPATH, "//span[text()='Due Date:']")
        # gets the father element to get the whole text
        parentElement = dueDateInfo.find_element(By.XPATH, "..")
        # to get the text after the <span> that has "Due Date:", split and remove spaces
        dueDateText = parentElement.text.split("Due Date:")[1].strip()
        assert dueDateText == (due_date), "Expected: '15/01/2018', Actual: '{dueDateText}'"

    def get_invoice_number(self, invoice_number):
        invoiceNumber = self.browser.find_element(By.XPATH, "//h6[@class='mt-2']")
        invoiceNumberText = invoiceNumber.text
        assert invoiceNumberText == (invoice_number)

    def get_booking_code_info(self, booking_code):
        bookingCodeInfo = self.browser.find_element(By.XPATH, "//td[contains(text(), 'Booking Code')]")
        # gets the father element to get the whole text
        parentElement = bookingCodeInfo.find_element(By.XPATH, "..")
        # to get the text after the <span> that has "Due Date:", split and remove spaces
        bookingCodeText = parentElement.text.split("Booking Code")[1].strip()
        assert bookingCodeText == (booking_code)

    def get_room_info (self, room):
        roomInfo = self.browser.find_element(By.XPATH, "//td[contains(text(), 'Room')]")
        # gets the father element to get the whole text
        parentElement = roomInfo.find_element(By.XPATH, "..")
        # to get the text after the <span> that has "Due Date:", split and remove spaces
        roomText = parentElement.text.split("Room")[1].strip()
        assert roomText == (room)

    def get_total_stay_account_info (self, total_stay_count):
        totalStayCountInfo = self.browser.find_element(By.XPATH, "//td[contains(text(), 'Total Stay Count')]")
        # gets the father element to get the whole text
        parentElement = totalStayCountInfo.find_element(By.XPATH, "..")
        # to get the text after the <span> that has "Due Date:", split and remove spaces
        totalStayCountText = parentElement.text.split("Total Stay Count")[1].strip()
        assert totalStayCountText == (total_stay_count)

    def get_total_stay_amount_info (self, total_stay_amount):
        totalStayAmountInfo = self.browser.find_element(By.XPATH, "//td[contains(text(), 'Total Stay Amount')]")
        # gets the father element to get the whole text
        parentElement = totalStayAmountInfo.find_element(By.XPATH, "..")
        # to get the text after the <span> that has "Due Date:", split and remove spaces
        totalStayAmountText = parentElement.text.split("Total Stay Amount")[1].strip()
        assert totalStayAmountText == (total_stay_amount)

    def get_checkin_info(self, check_in):
        checkInInfo = self.browser.find_element(By.XPATH, "//td[contains(text(), 'Check-In')]")
        # gets the father element to get the whole text
        parentElement = checkInInfo.find_element(By.XPATH, "..")
        # to get the text after the <span> that has "Due Date:", split and remove spaces
        checkInText = parentElement.text.split("Check-In")[1].strip()
        assert checkInText == (check_in)

    def get_checkout_info(self, check_out):
        checkOutInfo = self.browser.find_element(By.XPATH, "//td[contains(text(), 'Check-Out')]")
        # gets the father element to get the whole text
        parentElement = checkOutInfo.find_element(By.XPATH, "..")
        # to get the text after the <span> that has "Due Date:", split and remove spaces
        checkOutText = parentElement.text.split("Check-Out")[1].strip()
        assert checkOutText == (check_out)

    def get_customer_details_info(self, customer_details):
        customerDetailstInfo = self.browser.find_element(By.XPATH, "//section/div[@class='container']/div")
        customerDetailsText = customerDetailstInfo.text
        #Divide strings and remove blank spaces
        assert customerDetailsText == (customer_details.replace('\\n', '\n').strip()), f"Expected: '{customer_details}', Actual: '{customerDetailsText}'"

    def get_deposit_now_info(self, deposit_now):
        depositNowInfo = self.browser.find_element(By.XPATH, "/html/body/section/div/table[2]/tbody/tr/td[1]")
        depositNowText = depositNowInfo.text
        assert depositNowText == (deposit_now)

    def get_taxAndVat_info(self, tax_vat):
        taxAndVatInfo = self.browser.find_element(By.XPATH, "/html/body/section/div/table[2]/tbody/tr/td[2]")
        taxAndVatText = taxAndVatInfo.text
        assert taxAndVatText == (tax_vat), f"Expected: '{tax_vat}', Actual: '{taxAndVatText}'"

    def get_total_amount_info(self, total_amount):
        totalAmounttInfo = self.browser.find_element(By.XPATH, "/html/body/section/div/table[2]/tbody/tr/td[3]")
        totalAmountText = totalAmounttInfo.text
        assert totalAmountText == (total_amount)

