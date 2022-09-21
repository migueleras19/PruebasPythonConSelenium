from lib2to3.pgen2 import driver
from os import sep
from turtle import clear
import unittest, time
from xml.etree.ElementPath import find
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class Testplan (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver")
    def test(self):
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        
        driver.get("http://10.16.5.84:8380/WEB3/ingreso.html")
        user = driver.find_element_by_id("usuario")
        user.send_keys("ue01000663")
        contr =  driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
        contr.send_keys("123456789" + Keys.ENTER)
    
        trans = driver.find_element_by_id("entorno-pt")
        trans.send_keys("122006" + Keys.ENTER)
        time.sleep(1.5)

        with open("plan.txt", "r+") as file:
            for lineas in file:
                usuario = (lineas)
                sep = ','
                dividir = lineas.split(sep)
                try:
                    gotdata = dividir[1]
                    sb = dividir[0]
                    tr = dividir[1]
                    pl = dividir[2]
                    te = dividir[3]
                   

                except IndexError:
                    gotdata = 'null'

    
                print(sb, tr, pl, te)

                driver.find_element_by_id("c_C1Csubsistema_0").send_keys(sb)
                time.sleep(2)
                driver.find_element_by_id("c_C5Ctransaccion_0").send_keys(tr)
                trans.send_keys(Keys.TAB)
                time.sleep(1.5)
                driver.find_element_by_name("plantilla_0").send_keys(pl)
                time.sleep(1.5)
                driver.find_element_by_id("c_f5tipo_0").send_keys(te)
                time.sleep(1.5)

                act = ActionChains(driver)
                act.send_keys(Keys.F12).perform()
                time.sleep(4)

                trans = driver.find_element_by_id("entorno-pt")
                trans.clear()
                trans.send_keys("122006" + Keys.ENTER)
                time.sleep(2)
                
                
    
    def tearDown(self):
        self.driver.close()
                 
if __name__ == '__main__':
    unittest.main()