from csv import reader
import csv
from distutils.command.clean import clean
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class Ingreso122006(unittest. TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver")
    
    def test(self):
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        
        #Logeo al sistema Fitbank
        driver.get("http://10.16.5.88:9380/WEB3/ingreso.html")
        usuario = driver.find_element_by_id("usuario")
        usuario.send_keys("ue01000663")
        clave = driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
        clave.send_keys("hdkjhkjhkhkasda" + Keys.ENTER)
        time.sleep(3)
        transaccion = driver.find_element_by_id("entorno-pt")
        transaccion.send_keys("122006" + Keys.ENTER)
        time.sleep(3)

        with open('templates.csv') as File:
            reader = csv.DictReader(File, delimiter=',')
            for fila in reader:
                
                sub = driver.find_element_by_id('c_C1Csubsistema_0')
                #sub.clear()
                time.sleep(2)
                sub.send_keys(fila["sub"])
                sub.send_keys(Keys.TAB)
                
                trans = driver.find_element_by_id('c_C5Ctransaccion_0')
                trans.clear()
                time.sleep(5)
                trans.send_keys(fila["trans"])
                time.sleep(3)
                trans.send_keys(Keys.ENTER)
                time.sleep(5)

                plan = driver.find_element_by_name("plantilla_0")
                #plan.clear()
                time.sleep(3)
                plan.send_keys(fila["plan"])
                time.sleep(3)

                teje = driver.find_element_by_id("c_f5tipo_0")
                #teje.clear()
                time.sleep(3)
                teje.send_keys(fila["teje"])
                time.sleep(3)

                refe =  driver.find_element_by_name("f6referencia")
                refe.clear()
                time.sleep(3)
                refe.send_keys(fila["refe"])
                time.sleep(3)
                print('Insertando palntilla')

            teclear = ActionChains(driver)
            teclear.send_keys(Keys.F12).perform()
            time.sleep(5)

        transaccion = driver.find_element_by_id("entorno-pt")
        transaccion.clear()
        transaccion.send_keys("122006")
        time.sleep(5)
        transaccion.send_keys(Keys.ENTER)
        time.sleep(5)
        driver.close()

if __name__ == '__main__':
     unittest.main()