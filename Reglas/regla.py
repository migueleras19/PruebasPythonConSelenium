from lib2to3.pgen2 import driver
from os import sep
#from turtle import clear
import unittest, time
from xml.etree.ElementPath import find
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class TestRegla (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver")
    def test(self):
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        
        driver.get("http://10.16.5.94:8380/WEB3/ingreso.html")
        user = driver.find_element_by_id("usuario")
        user.send_keys("ue01000663")
        contr =  driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
        contr.send_keys("123456789" + Keys.ENTER)
    
        trans = driver.find_element_by_id("entorno-pt")
        trans.send_keys("002024" + Keys.ENTER)
        time.sleep(3)

        with open("regla.txt", "r") as file:
            for lineas in file:
                usuario = (lineas)
                sep = ','
                dividir = lineas.split(sep)
                try:
                    gotdata = dividir[1]
                    re = dividir[0]
                    ar = dividir[1]
                    hc = dividir[2]
                except IndexError:
                    gotdata = 'null'

                print('Regla ingresada', re)

                driver.find_element_by_id("c_F1creglabpm_0").send_keys(re)
                trans.send_keys(Keys.ENTER)
                time.sleep(1.5)
                driver.find_element_by_name("archivo_0").send_keys(ar)
                time.sleep(1.5)
                driver.find_element_by_id('c_f1_hoja_regla_0').send_keys(hc)
                time.sleep(1.5)



    def tearDown(self):
        self.driver.close()
                 
if __name__ == '__main__':
    unittest.main()