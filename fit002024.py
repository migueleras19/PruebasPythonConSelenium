import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class Ingreso002024(unittest. TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")
    def testreglas(self):
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
        trans.send_keys("002024")
        time.sleep(1)
        trans.send_keys("webdrive" + Keys.ENTER)
        time.sleep(1.5)
        subsistema = driver.find_element_by_id("c_F1creglabpm_0")
        subsistema.send_keys("174")
        time.sleep(1)
        regla = driver.find_element_by_name("archivo_0").send_keys("/home/qacore/Escritorio/SectorPublico/reglas/174_HOMOLOGACION_IRP.xls")
        time.sleep(2)
        cal = driver.find_element_by_name("f1_hoja_regla")
        cal.send_keys("A")
        print('Ingreso de Regla')
        time.sleep(4)
        #button = driver.find_element_by_id("c_fboton_0")
        teclear = ActionChains(driver)
        teclear.send_keys(Keys.F12).perform()
        time.sleep(5)
        driver.close()
    def testSubirregla(self):
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
        trans.send_keys("002024")
        time.sleep(1)
        trans.send_keys("webdrive" + Keys.ENTER)
        time.sleep(1.5)
        subsistema = driver.find_element_by_id("c_F1creglabpm_0")
        subsistema.send_keys("325")
        time.sleep(1)
        regla = driver.find_element_by_name("archivo_0").send_keys("/home/qacore/Escritorio/SectorPublico/reglas/325-AREAS_Y_CENTRO_DE_COSTOS.xls")
        time.sleep(2)
        cal = driver.find_element_by_name("f1_hoja_regla")
        cal.send_keys("A")
        time.sleep(5)
        print('Ingreso de regla')
        teclear = ActionChains(driver)
        teclear.send_keys(Keys.F12).perform()
        time.sleep(5)
        driver.close()

if __name__ == '__main__':
     unittest.main()