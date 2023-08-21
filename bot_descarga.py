# **Bot de Descarga de Mis Comprobantes en AFIP**
# Autor: Ricardo Fernández
# Data Science-Data Analytics-Developer Python
# LinkedIn: https://www.linkedin.com/in/ricardo-fern%C3%A1ndez00
#
# Descripción:
# Este script automatiza la descarga de Mis Comprobantes en el sitio web de AFIP. Fue desarrollado bajo solicitud
# para empresas Responsables Inscriptos. El script utiliza la biblioteca Selenium para interactuar con la plataforma,
# permitiendo el acceso y descarga de los comprobantes necesarios.
#
# Agradecimientos:
# Se basa en el trabajo del autor Diego Mendizábal (https://github.com/diego-dotcom/bot_descarga).
#
# Advertencia:
# El uso de este bot es responsabilidad del usuario. El autor no se hace responsable por problemas derivados de un uso indebido
# o mala ejecución del mismo.

import random
import pandas as pd
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

encabezado ={
     "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}

def main():
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    archivo_excel = 'claves.xlsx'
    ruta_excel = os.path.join(directorio_actual, archivo_excel)

    df = pd.read_excel(ruta_excel, engine='openpyxl')

    for i in df.index:
        cuit = int(df['cuit'][i])
        clave = str(df['clave'][i])

        options = webdriver.ChromeOptions()
        prefs = {
            "download.default_directory": directorio_actual,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        url = "https://auth.afip.gob.ar/contribuyente_/login.xhtml"
        driver.get(url)

        campo_cuit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "F1:username")))
        campo_cuit.clear()
        campo_cuit.send_keys(cuit)

        boton_cuit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "F1:btnSiguiente")))
        boton_cuit.click()

        campo_clave = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "F1:password")))
        campo_clave.clear()
        campo_clave.send_keys(clave)

        boton_clave = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "F1:btnIngresar")))
        boton_clave.click()

        driver.implicitly_wait(8)

        buscador = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'buscadorInput')))
        buscador.send_keys('Mis Comprobantes')
        mis_servicios = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'search-item')))
        mis_servicios.click()
        time.sleep(2)

        driver.switch_to.window(driver.window_handles[1])

        try:
            driver.find_element(By.XPATH, "/html/body/form/main/div/div/div[2]/div/a").click()
            time.sleep(random.randint(1, 3))
        except:
            pass

        driver.find_element(By.ID, "btnEmitidos").click()
        driver.find_element(By.ID, "fechaEmision").click()
        driver.find_element(By.CSS_SELECTOR, "body > div > div.ranges > ul > li:nth-child(5)").click()
        driver.find_element(By.ID, "buscarComprobantes").click()
        driver.implicitly_wait(8)

        try:
            excel_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-default.buttons-excel.buttons-html5.btn-defaut.btn-sm.sinborde")))
            driver.execute_script("arguments[0].scrollIntoView();", excel_button)
            driver.execute_script("arguments[0].click();", excel_button)
            time.sleep(10)  # Pausa para esperar la descarga (ajusta según sea necesario)
        except Exception as e:
            print("Error al encontrar o hacer clic en el botón Excel:", e)

        driver.back()

        driver.find_element(By.ID, "btnRecibidos").click()
        driver.find_element(By.ID, "fechaEmision").click()
        driver.find_element(By.CSS_SELECTOR, "body > div > div.ranges > ul > li:nth-child(5)").click()
        driver.find_element(By.ID, "buscarComprobantes").click()
        driver.implicitly_wait(8)

        try:
            excel_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-default.buttons-excel.buttons-html5.btn-defaut.btn-sm.sinborde")))
            driver.execute_script("arguments[0].scrollIntoView();", excel_button)
            driver.execute_script("arguments[0].click();", excel_button)
            time.sleep(10)  # Pausa para esperar la descarga (ajusta según sea necesario)
        except Exception as e:
            print("Error al encontrar o hacer clic en el botón Excel:", e)

        driver.quit()

if __name__ == "__main__":
    main()
