from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

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



def verificar_nuevos_mensajes(driver, archivo):
    messages = driver.find_elements_by_class_name("_1WZqU.PNlAR")
    for message in messages:
        mensaje_texto = message.text
        print(mensaje_texto)
        archivo.write(mensaje_texto + "\n")

if __name__ == "__main__":
    # Inicia el navegador
    driver = webdriver.Chrome(options=options)

    # Abre WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    time.sleep(15)  # Espera a que el usuario escanee el código QR manualmente

    driver.find_element(By.PARTIAL_LINK_TEXT, "Estimado")
    cicle =0
    # Bucle infinito para verificar nuevos mensajes
    while True and cicle<100:
        # Abre un archivo para escribir los mensajes (crea el archivo si no existe)
        try:
            with open("mensajes.txt", "a", encoding="utf-8") as archivo:
                verificar_nuevos_mensajes(driver, archivo)
        except FileNotFoundError:
            with open("mensajes.txt", "w", encoding="utf-8") as archivo:
                pass  # Crea el archivo vacío si no existe

        time.sleep(30)  # Espera 10 segundos antes de volver a verificar los mensajes
        cicle+=1
    # Cierra el navegador
    driver.quit()