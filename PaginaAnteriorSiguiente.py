import unittest
from selenium import webdriver
from selenium.webdriver.common import keys
import time

class usando_unittest(unittest.TestCase):

          def setUp(self):
                    self.driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")

          def test_pagina_anterior(self):
                    driver = self.driver
                    driver.get("https://www.google.com")
                    time.sleep(3)
                    driver.get("https://www.linkedin.com")
                    time.sleep(3)
                    driver.get("https://www.twitter.com")
                    time.sleep(3)
                    driver.back()
                    time.sleep(3)
                    driver.back()
                    time.sleep(3)
                    driver.forward()
                    time.sleep(3)
if __name__ == "__main__":
          unittest.main()
