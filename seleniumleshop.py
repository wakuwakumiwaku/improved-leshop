import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "S:\Leshop\\"}
chromeOptions.add_experimental_option("prefs",prefs)
#chromedriver = "E:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_options=chromeOptions)


#URLS
LOGIN_URL= 'https://login.migros.ch/login'
orders_url= 'https://shop.migros.ch/en/supermarket/home(bm:customer/orders)'
pdf_url= 'https://shop.migros.ch/customer/public/v1/api/users/self/reporting/INVOICE/en/orders/1111111'
testurl= 'https://shop.migros.ch/en/shoppingList/lastOrder/11111111'
shop_url= 'https://shop.migros.ch'



#driver= Chrome(chrome_options=chromeOptions)
driver.get('https://login.migros.ch/login')

#login
user = driver.find_element_by_id('username')
user.send_keys('URUSR')

passwd = driver.find_element_by_id('password')
passwd.send_keys('URPSW')
passwd.submit()



i = 0
while i < 1:
 try:
  i = i + 1
  driver.get(orders_url)
  time.sleep(2)
  second = driver.find_element_by_name('password')
  second.send_keys('URPSW')
  second.submit()
  time.sleep(2)
 except:
  i = i + 1
  continue

driver.get(shop_url)
time.sleep(2)

driver.get(orders_url)
time.sleep(2)
#orders = driver.find_element_by_xpath('Orders')
#orders.click()
invoices = driver.find_element_by_xpath("//a[normalize-space()='Invoice (PDF)']")
invoices.click()
i=0
while i < 10:
 try:
  time.sleep(1)
  allorders = driver.find_element_by_xpath("//span[normalize-space()='Show more orders']")
  driver.execute_script("arguments[0].scrollIntoView();", allorders)
  allorders.click()
  i=i+1
 except:
  i=10
  continue
oldies = driver.find_elements_by_class_name("download-pdf")
#print(oldies)
length = len(oldies)
print(length)
print(oldies[1])
i=0
while i < len(oldies):
 try:
  time.sleep(0.1)
  oldies = driver.find_elements_by_class_name("download-pdf")
  driver.execute_script("arguments[0].scrollIntoView();", oldies[i])
  time.sleep(0.1)
  oldies[i].click()
  time.sleep(0.1)
  i=i+1
  print(i)
  print(oldies[i])
 except:
  i=i+1
  print('Fuck You')
  continue
print(length)