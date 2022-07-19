from csv import reader
from distutils.command.clean import clean
from sqlite3 import DateFromTicks
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import unittest
import csv
import time


class Ingreso002024(unittest. TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")
        
    def test(self):
        driver = self.driver
        driver.maximize_window()

        driver.get("http://10.16.5.94:8380/WEB3/ingreso.html")
        usuario = driver.find_element_by_id("usuario")
        usuario.send_keys("ue01000663")
        clave = driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
        clave.send_keys("asadasadsasd" + Keys.ENTER)
        time.sleep(1.5)

        print('Bienvenido', self)


        transaccion = driver.find_element_by_id("entorno-pt")
        transaccion.send_keys('002024' + Keys.ENTER)
        time.sleep(1.5)

        with open('rules.csv')