from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
#import pandas

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')


driver_path = '/home/dani-ideas/Documents/Softwers/chromedriver.exe'

driver = webdriver.Chrome(driver_path, options=options)

# Inicializamos el navegador
driver.get('https://eltiempo.es')