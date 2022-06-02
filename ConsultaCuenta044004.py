import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")
driver.maximize_window()
driver.get("http://10.16.5.88:9380/WEB3/ingreso.html")
capture_path = ('/media/qacore/data/respaldos/practicasSelenium/pruebas de python con selenium/CAPTURA/')
driver.save_screenshot("imagen0.png")



usuario = driver.find_element_by_id("usuario")
usuario.send_keys("ue01000663")
clave = driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
clave.send_keys("ue01000663")
clave.send_keys("webdrive" + Keys.ENTER)
time.sleep(3)

trans = driver.find_element_by_xpath("//*[@id='entorno-pt']")
trans.send_keys("044004")
trans.send_keys("webdrive" +Keys.ENTER)
time.sleep(5)
driver.save_screenshot("imagen1.png")

ci = driver.find_element_by_xpath("//*[@id='c_w2_cidentificacion_0']")
ci.send_keys('1104638091')
ccuenta = driver.find_element_by_xpath("//*[@id='c_w2_ccuenta_0']")
ccuenta.send_keys('0011778712')
time.sleep(3)
buscar = ActionChains(driver)
buscar.send_keys(Keys.ENTER).perform()
time.sleep(25)
driver.save_screenshot("imagen2.png")
driver.close()