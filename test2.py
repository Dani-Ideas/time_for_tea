from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = "/home/dani-ideas/Documents/Softwers/chrome-linux64/chrome"

driver = webdriver.Chrome(options=options)
driver.get("https://www.youtube.com/")
driver.close()
