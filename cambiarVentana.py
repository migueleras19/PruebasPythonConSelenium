import unittest
from selenium import webdriver
from selenium.webdriver.common import keys
import time

class usando_unittest(unittest.TestCase):
          
          def setUp(self):
              self.driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")

          def test_cambiar_ventana(self):
                    driver = self.driver
                    driver.get("https://www.google.com")
                    time.sleep(3)
                    driver.execute_script("window.open('');")
                    time.sleep(3)
                    driver.switch_to.window(driver.window_handles[1])
                    time.sleep(3)
                    driver.get("https://stackoverflow.com")
                    time.sleep(3)
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(3)
          
if __name__ == '__main__':
          unittest.main()