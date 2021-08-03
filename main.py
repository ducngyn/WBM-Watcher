from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from helper import *
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(executable_path='C:/Users/nnguyen/Environment/chromedriver.exe', options=options)
browser.get('https://www.wbm.de/wohnungen-berlin/angebote/')
mainWindow = browser.current_window_handle

# Accept cookies
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cdk-overlay-0"]/div[2]/div[2]/div[2]/button[1]'))).click()

apartments = browser.find_elements_by_class_name('openimmo-search-list-item')

if apartments:
    for entry in apartments:
        roomCount = float(entry.find_element(By.XPATH, './div[2]/article/div/ul[1]/li[3]/div[2]').text)
        flatSize = entry.find_element(By.XPATH, './div[2]/article/div/ul[1]/li[2]/div[2]').text
        flatSize = float(flatSize[:4].replace(',','.'))

        if (roomCount > 1) and (flatSize > 20):
            # Open apartment in new tab 
            # fill out the form and close the tab afterwards
            entry.find_element(By.XPATH, './div[2]/article/div/p[3]/a').send_keys(Keys.CONTROL + Keys.RETURN)
            browser.switch_to.window(browser.window_handles[-1])
            fillForm(browser)
            browser.close()

            browser.switch_to.window(mainWindow)

