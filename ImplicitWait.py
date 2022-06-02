import unittest
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class usando_unittest(unittest.TestCase):
          def setUp(self):
                    self.driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")

          def test_implicit_wait(self):
                    driver = self.driver
                    driver.implicitly_wait(5)#segundos
                    driver.get("https://www.google.com")
                    myDynamicElement = driver.find_element_by_name("q")#componente dinamico
if __name__ == '__main__':
          unittest.main()

