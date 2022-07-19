from lib2to3.pgen2 import driver
from turtle import title
import unittest
from selenium import webdriver

class Testtrue(unittest.TestCase):
    def testName(self):

        driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")
        driver.get("https://glowroot.org/")

        titleOfWebPage = driver.title

        self.assertTrue(titleOfWebPage == "Glowroot")



        #self.assertFalse(titleOfWebPage == "Glowroot")
        

if __name__ == '__main__':
     unittest.main()