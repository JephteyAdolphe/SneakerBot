import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\SeleniumWebDriver\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

firstName = "Jeff"
lastName = "Adolphe"
address = "555 Main st"
city = "New York"
state = "NY"
#full_url = "https://www.footlocker.com/category/mens/shoes.html"
full_url = "https://www.footlocker.com/"

product = "nike air force 1 low men"

driver.get(full_url)
search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input_search_query")))


search.send_keys(product)
search.send_keys(Keys.RETURN)

#master_result_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "answer")))
#hidden = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "overflow-hidden")))
#user_id = re.sub('\D', '', hidden.text)


#driver.quit()
