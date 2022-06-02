import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime

class SearchCases(unittest.TestCase):
          def setUp(self):
                    opcionesChrome = Options()
                    opcionesChrome.add_argument("start-maximized")

                    self.driver.find_element_by_id("usuario")
                    self.driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
                    self.keys('UE01000663')
                    self.keys('15S5SD5F')
                    teclear = ActionChains(self.driver)
                    teclear.send_keys(Keys.ENTER).perform()
                    time.sleep(5)

                    self.driver = webdriver.Web("/media/qacore/data/drivers/chromedriver", options=opcionesChrome)
                    self.get = ('http://10.16.5.84:8380/WEB3/ingreso.html')
                    self.driver.implicitly_wait('10')
                    self.driver.find_element_by_xpath("//*[@id='c_f1IdentificacionS_0']")
                    self.driver.find_element_by_xpath("//*[@id='c_ccuenta_0']")
if __name__ == '__main__':
    unittest.main()                  