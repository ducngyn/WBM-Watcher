from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import *
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(executable_path='C:/Users/nnguyen/Environment/chromedriver.exe', options=options)
browser.get('https://www.wbm.de/wohnungen-berlin/angebote/')

# Accept cookies
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cdk-overlay-0"]/div[2]/div[2]/div[2]/button[1]'))).click()

apartments = browser.find_elements_by_class_name('openimmo-search-list-item')

if apartments:
    for entry in apartments:
        applyForApartment(browser, entry)
      

