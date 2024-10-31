import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get("https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/")
browser.implicitly_wait(8) 
browser.maximize_window()
 
browser.find_element(By.NAME, "username").send_keys("demouser") 
browser.find_element(By.NAME, "password").send_keys("abc123") 
browser.find_element(By.ID, "btnLogin").click() 

assert browser.current_url == "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/account"

if browser.current_url == "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/account":
    print ("Login success")
else:
    print ("Error: Login failed")

browser.find_element(By.XPATH, "/html/body/section/div/div[2]/div[5]/a").click()

# change tab 
handles = browser.window_handles
browser.switch_to.window(handles[-1])

#============================= Hotel Name =============================

hotelNameInfo = WebDriverWait(browser, 5).until(
     EC.presence_of_element_located((By.XPATH, "//h4[@class='mt-5']"))) #tried first //h4[@class='mt-5'] - correct but failing
hotelName = hotelNameInfo.text
print (hotelName)

#============================= Invoice Date =============================

invoiceDateInfo = browser.find_element(By.XPATH, "//span[contains(text(), 'Invoice Date:')]")
# gets the father element to get the whole text
parentElement = invoiceDateInfo.find_element(By.XPATH, "..")
# to get the text after the <span> that has "Invoice Date:", split and remove spaces
invoiceDateText = parentElement.text.split("Invoice Date:")[1].strip()
print (invoiceDateText)

#============================= Due Date =============================

dueDateInfo = browser.find_element(By.XPATH, "//span[text()='Due Date:']")
# gets the father element to get the whole text
parentElement = dueDateInfo.find_element(By.XPATH, "..")
# to get the text after the <span> that has "Due Date:", split and remove spaces
dueDateText = parentElement.text.split("Due Date:")[1].strip()
print (dueDateText)

#============================= Invoice Number =============================

invoiceNumber = browser.find_element(By.XPATH, "//h6[@class='mt-2']")
invoiceNumberText = invoiceNumber.text
print (invoiceNumberText)

#============================= Booking Code =============================

bookingCodeInfo = browser.find_element(By.XPATH, "//td[contains(text(), 'Booking Code')]")
# gets the father element to get the whole text
parentElement = bookingCodeInfo.find_element(By.XPATH, "..")
# to get the text after the <span> that has "Due Date:", split and remove spaces
bookingCodeText = parentElement.text.split("Booking Code")[1].strip()
print (bookingCodeText)

#============================= Room =============================

roomInfo = browser.find_element(By.XPATH, "//td[contains(text(), 'Room')]")
# gets the father element to get the whole text
parentElement = roomInfo.find_element(By.XPATH, "..")
# to get the text after the <span> that has "Due Date:", split and remove spaces
roomText = parentElement.text.split("Room")[1].strip()
print (roomText)

#============================= Total Stay Count =============================

totalStayCountInfo = browser.find_element(By.XPATH, "//td[contains(text(), 'Total Stay Count')]")
# gets the father element to get the whole text
parentElement = totalStayCountInfo.find_element(By.XPATH, "..")
# to get the text after the <span> that has "Due Date:", split and remove spaces
totalStayCountText = parentElement.text.split("Total Stay Count")[1].strip()
print (totalStayCountText)

#============================= Total Stay Amount =============================

totalStayAmountInfo = browser.find_element(By.XPATH, "//td[contains(text(), 'Total Stay Amount')]")
# gets the father element to get the whole text
parentElement = totalStayAmountInfo.find_element(By.XPATH, "..")
# to get the text after the <span> that has "Due Date:", split and remove spaces
totalStayAmountText = parentElement.text.split("Total Stay Amount")[1].strip()
print (totalStayAmountText)

#============================= Check-in =============================

checkInInfo = browser.find_element(By.XPATH, "//td[contains(text(), 'Check-In')]")
# gets the father element to get the whole text
parentElement = checkInInfo.find_element(By.XPATH, "..")
# to get the text after the <span> that has "Due Date:", split and remove spaces
checkInText = parentElement.text.split("Check-In")[1].strip()
print (checkInText)

#============================= Check-Out =============================

checkOutInfo = browser.find_element(By.XPATH, "//td[contains(text(), 'Check-Out')]")
# gets the father element to get the whole text
parentElement = checkOutInfo.find_element(By.XPATH, "..")
# to get the text after the <span> that has "Due Date:", split and remove spaces
checkOutText = parentElement.text.split("Check-Out")[1].strip()
print (checkOutText)

#============================= Customer Details =============================

customerDetailstInfo = browser.find_element(By.XPATH, "//section/div[@class='container']/div")
customerDetailsText = customerDetailstInfo.text
print (customerDetailsText)

#============================= Deposit Now =============================

depositNowInfo = browser.find_element(By.XPATH, "/html/body/section/div/table[2]/tbody/tr/td[1]")
depositNowText = depositNowInfo.text
print (depositNowText)

#============================= Tax & VAT =============================

taxAndVatInfo = browser.find_element(By.XPATH, "/html/body/section/div/table[2]/tbody/tr/td[2]")
taxAndVatText = taxAndVatInfo.text
print (taxAndVatText)

#============================= Total Amount =============================

totalAmounttInfo = browser.find_element(By.XPATH, "/html/body/section/div/table[2]/tbody/tr/td[3]")
totalAmountText = totalAmounttInfo.text
print (totalAmountText)


time.sleep(8)