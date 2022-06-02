import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")
driver.maximize_window()
driver.get("http://10.16.5.88:9380/WEB3/ingreso.html")
capture_path = ('/media/qacore/data/respaldos/practicasSelenium/pruebas de python con selenium/CAPTURA/')
driver.save_screenshot("ingreso.png")


