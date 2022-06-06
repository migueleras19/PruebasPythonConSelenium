import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class Ingreso122006(unittest. TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")
    def testtemplates(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://10.16.5.94:8380/WEB3/ingreso.html")
        usuario = driver.find_element_by_id("usuario")
        usuario.send_keys("ue01000663")
        clave = driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
        clave.send_keys("hdkjhkjhkhkasda")
        clave.send_keys("webdrive" + Keys.ENTER)
        time.sleep(1)
        trans = driver.find_element_by_id("entorno-pt")
        trans.send_keys("122006")
        time.sleep(1)
        trans.send_keys("webdrive" + Keys.ENTER)
        time.sleep(1.5)
        vent = driver.find_element_by_css_selector("#entorno-barra-botones > .boton:nth-child(2) > img").click()
        time.sleep(10)
        driver.close()
if __name__ == '__main__':
     unittest.main()