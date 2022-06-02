from random import random
import unittest
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import csv
import time


class usando_unittest(unittest. TestCase):

    def setUp(self):
        self.driver = webdrive.Chrome('../chromedriver')

    def testPosicionconsolidad(self):
         driver = self.driver
         driver.maximize_window()
         driver.get("http://10.16.5.84:8380/WEB3/ingreso.html")
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
         self = driver.find_element_by_id("c_IDENTIFICACION_0")
         self.send_keys("1104638091" + Keys.ENTER)       
         time.sleep(10)
         #driver.close()

    def testConsultacuentas(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://10.16.5.85:8380/WEB3/ingreso.html")
        usuario = driver.find_element_by_id("usuario")
        usuario.send_keys("ue01000663")
        clave = driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
        clave.send_keys("hdkjhkjhkhkasda")
        clave.send_keys("webdrive" + Keys.ENTER)
        time.sleep(3)
        trans = driver.find_element_by_id("entorcleno-pt")
        trans.send_keys("044004")
        trans.send_keys("webdrive" + Keys.ENTER)
        time.sleep(3)
        with  open('datos.txt') as file:
                for i,line in enumerate(file):
                    cuenta = (line)
                    sep = ","
                    dividir = cuenta.split(sep)
                try:
                    gotdata = dividir[1]
                    ccuenta = dividir[0]
                except IndexError:
                    gotdata = 'null'
                print ('Cuenta procesada',(ccuenta))

        ccuenta = driver.find_element_by_id("c_w2_ccuenta_0").send_keys(ccuenta + Keys.ENTER)
        time.sleep(15)
        #file.closeclose()
        #driver.close()
        # ccuenta = driver.find_element_by_xpath("//*[@id='entorno-teclas']/button[5]/img").F7()
        # ccuenta.send_keys(Keys.ENTER)
        # time.sleep(10)
        #file.closeclose()
        # driver.close()

        # self.send_keys("0011778712" + Keys.ENTER)       
        # time.sleep(20)
        #driver.close()

    # def testPosicionconsolidad2(self):
    #     driver = self.driver
    #     driver.maximize_window()
    #     driver.get("http://10.16.5.88:9380/WEB3/ingreso.html")
    #     usuario = driver.find_element_by_id("usuario")
    #     usuario.send_keys("ue01000663")
    #     clave = driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
    #     clave.send_keys("hdkjhkjhkhkasda")
    #     clave.send_keys("webdrive" + Keys.ENTER)
    #     time.sleep(1.5)
    #     trans = driver.find_element_by_id("entorno-pt")
    #     trans.send_keys("024100")
    #     trans.send_keys("webdrive" + Keys.ENTER)
    #     time.sleep(3)
    #     self = driver.find_element_by_id("c_IDENTIFICACION_0")
    #     self.send_keys("0105046072" + Keys.ENTER)       
    #     time.sleep(20)
    #     driver.close()

    # def testConsultacuentas2(self):
    #     driver = self.driver
    #     driver.maximize_window()
    #     driver.get("http://10.16.5.85:8380/WEB3/ingreso.html")
    #     usuario = driver.find_element_by_id("usuario")
    #     usuario.send_keys("ue01000663")
    #     clave = driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
    #     clave.send_keys("hdkjhkjhkhkasda")
    #     clave.send_keys("webdrive" + Keys.ENTER)
    #     time.sleep(1.5)
    #     trans = driver.find_element_by_id("entorno-pt")
    #     trans.send_keys("044004")
    #     trans.send_keys("webdrive" + Keys.ENTER)
    #     time.sleep(3)
    #     with  open('datos.txt') as file:
    #             for i,line in enumerate(file):
    #                 cuenta = (line)
    #                 sep = ","
    #                 dividir = cuenta.split(sep)
    #             try:
    #                 gotdata = dividir[1]
    #                 ccuenta = dividir[0]
    #                 f12 = dividir[1]
    #             except IndexError:
    #                 gotdata = 'null'
    #             print ('Cuenta procesada',(ccuenta))

    #     ccuenta = driver.find_element_by_id("c_w2_ccuenta_0").send_keys(ccuenta + Keys.ENTER)
    #     time.sleep(15)
    #     #file.closeclose()
    #     driver.close()

    # def testPosicionconsolidad3(self):
    #     driver = self.driver
    #     driver.maximize_window()
    #     driver.get("http://10.16.5.88:9380/WEB3/ingreso.html")
    #     usuario = driver.find_element_by_id("usuario")
    #     usuario.send_keys("ue01000663")
    #     clave = driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
    #     clave.send_keys("hdkjhkjhkhkasda")
    #     clave.send_keys("webdrive" + Keys.ENTER)
    #     time.sleep(1.5)
    #     trans = driver.find_element_by_id("entorno-pt")
    #     trans.send_keys("024100")
    #     trans.send_keys("webdrive" + Keys.ENTER)
    #     time.sleep(3)
    #     self = driver.find_element_by_id("c_IDENTIFICACION_0")
    #     self.send_keys("1104021876" + Keys.ENTER)       
    #     time.sleep(20)
    #     driver.close()

    # def testConsultacuentas3(self):
    #     driver = self.driver
    #     driver.maximize_window()
    #     driver.get("http://10.16.5.88:9380/WEB3/ingreso.html")
    #     usuario = driver.find_element_by_id("usuario")
    #     usuario.send_keys("ue01000663")
    #     clave = driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
    #     clave.send_keys("hdkjhkjhkhkasda")
    #     clave.send_keys("webdrive" + Keys.ENTER)
    #     time.sleep(1.5)
    #     trans = driver.find_element_by_id("entorno-pt")
    #     trans.send_keys("044001")
    #     trans.send_keys("webdrive" + Keys.ENTER)
    #     time.sleep(3)
    #     with  open('datos.txt') as file:
    #             for i,line in enumerate(file):
    #                 cuenta1 = (line)
    #                 sep = ","
    #                 dividir = cuenta1.split(sep)
    #             try:
    #                 ccuenta = dividir[0]
    #                 gotdata = dividir[1]
    #                 f12 = dividir[0]
                    
    #             except IndexError:
    #                 gotdata = 'null'
    #             print ('Cuenta procesada',(ccuenta))

    #     ccuenta = driver.find_element_by_id("c_w2_ccuenta_0").send_keys(ccuenta + Keys.ENTER)
    #     time.sleep(15)
        file.closeclose()
        driver.close()
if __name__ == '__main__':
     unittest.main()