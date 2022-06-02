#como accesar a un select y automatizar el proceso de seleccionar y recuperar los datos.

from datetime import time
import unittest
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cv2 #usando opencv
import time

class usando_unittest(unittest.TestCase):
          def setUp(self):
                    self.driver= webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")

          def test_opencv(self):
                    driver = self.driver
                    driver.get("https://www.google.com")
                    driver.save_screenshot("imagen1.png")
                    time.sleep(3)

          def test_imagen(self):
                    img1= cv2.imread('img1.png')
                    img2= cv2.imread('img2.png')
