import unittest
from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import csv


driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")
driver.get("http://10.16.5.85:8380/WEB3/ingreso.html")
driver.maximize_window()


usuario = driver.find_element_by_id("usuario")
usuario.clear()
time.sleep(2)
usuario.send_keys("BA01001601")
time.sleep(2)
clave = driver.find_element_by_xpath("//input[@type='password']")
clave.clear()
clave.send_keys("BA01001665401")
time.sleep(2)
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(2)

transaccion = driver.find_element_by_id("entorno-pt")
transaccion.clear()
transaccion.send_keys("03-6600")
time.sleep(2)
transaccion.send_keys(Keys.ENTER)
time.sleep(3)