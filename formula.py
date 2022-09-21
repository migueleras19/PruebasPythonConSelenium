import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class Testingreso01002(unittest. TestCase):


    def setUp(self):
         self.driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")
    def testSubirformularios(self):
         driver = self.driver
         driver.maximize_window()
         driver.get("http://10.16.5.94:8380/WEB3/ingreso.html")
         usuario = driver.find_element_by_id("usuario")
         usuario.send_keys("ue01000663")
         clave = driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
         clave.send_keys("hdkjhkjhkhkasda")
         clave.send_keys("webdrive" + Keys.ENTER)
         time.sleep(0.5)
         trans = driver.find_element_by_id("entorno-pt")
         trans.send_keys("01002")
         trans.send_keys("webdrive" + Keys.ENTER)
         time.sleep(2)
         form = driver.find_element_by_name("archivo_0").send_keys("/home/qacore/Escritorio/PAQUETE_UNO/forms/FORMS.zip")
         time.sleep(2)
         print ("Formulario Ingresado")
         button = driver.find_element_by_id("c_fboton_0")
         button.send_keys("webdrive" + Keys.ENTER)
         time.sleep(7)
         driver.close()
         
    def testSubirreportes(self):
         driver = self.driver
         driver.maximize_window()
         driver.get("http://10.16.5.94:8380/WEB3/ingreso.html")
         usuario = driver.find_element_by_id("usuario")
         usuario.send_keys("ue01000663")
         clave = driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
         clave.send_keys("hdkjhkjhkhkasda")
         clave.send_keys("webdrive" + Keys.ENTER)
         time.sleep(1.5)
         trans = driver.find_element_by_id("entorno-pt")
         trans.send_keys("01002")
         trans.send_keys("webdrive" + Keys.ENTER)
         time.sleep(3)
         reports = driver.find_element_by_name("archivo_0").send_keys("/home/qacore/Escritorio/PAQUETE_UNO/reports/REPORTS.zip")
         time.sleep(2)
         print ('Reporte Ingresado')
         button = driver.find_element_by_id("c_fboton_0")
         button.send_keys("webdrive" + Keys.ENTER)
         time.sleep(7)
         driver.close()
     
         

        
if __name__ == '__main__':
     unittest.main()