import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class Carga(unittest. TestCase):
    
    
    def setUp(self):
         self.driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")
    def testSubirformularios(self):
         driver = self.driver
         driver.maximize_window()
         driver.get("https://mdbootstrap.com/docs/standard/plugins/file-upload/")
         carga =  driver.find_element_by_css_selector("file-upload-input")
         carga.send_keys("/home/qacore/Documentos/wallpaperbetter.jpg")
         time.sleep(2)

if __name__ == '__main__':
     unittest.main()