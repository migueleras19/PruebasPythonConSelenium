from os import sep
import unittest
from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import csv


class posicionConsolidad(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")
    def testPosicionconsolidad(self):
            driver = self.driver
            driver.maximize_window()
            driver.get("http://10.16.5.93:8380/WEB3/ingreso.html")
            usuario = driver.find_element_by_id("usuario")
            usuario.send_keys("ue01000663")
            clave = driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
            clave.send_keys("hdkjhkjhkhkasda")
            clave.send_keys("webdrive" + Keys.ENTER)
            time.sleep(1.5)
            trans = driver.find_element_by_id("entorno-pt")
            trans.send_keys("024100")
            trans.send_keys("webdrive" + Keys.ENTER)
            time.sleep(3)
            with open('identificacion.txt', 'r') as file:
                for i, line in enumerate(file):
                    cedula = (line)
                    sep = ","
                    dividir = cedula.split(sep)
                    try:
                        gotdata = dividir[1]
                        cedula = dividir[0]
                    except IndexError:
                        gotdata = 'null'
                    print('CUENTA PROCESADA ' +(cedula))
                    cedula = driver.find_element_by_id("c_IDENTIFICACION_0").send_keys(cedula + Keys.ENTER)
            time.sleep(20)
            file.close()
            #driver.close()
if __name__ == '__main__':
    unittest.main()