from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
#import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.binary_location = "/home/dani-ideas/Documents/Softwers/chrome-linux64/chrome"

driver = webdriver.Chrome(options=options)
driver.get("https://www.mx.avon.com/REPSuite/loginMain.page")

# -add logic for Xpath in DOM dinamic 

#login
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td/div/div[1]/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/input')))\
    .send_keys('01885399')
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td/div/div[1]/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/input')))\
    .send_keys('**********')


WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td/div/div[1]/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr[6]/td/table/tbody/tr/td[3]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/div[1]/div/form/table/tbody/tr[1]/td/table/tbody/tr/td[1]/a/img')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/div/form/div[1]/table/tbody/tr[3]/td/table/tbody/tr/td/p/input')))\
    .click()
#agregar la logica para meter el pedido procesado
driver.close()
