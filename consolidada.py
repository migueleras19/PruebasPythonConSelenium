import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")
driver.maximize_window()
driver.get("http://10.16.5.84:8380/WEB3/ingreso.html")
usuario = driver.find_element_by_id("usuario")
usuario.send_keys("admin")
clave = driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
clave.send_keys("hdkjhkjhkhkasda")
clave.send_keys("webdrive" + Keys.ENTER)
time.sleep(2)
trans = driver.find_element_by_xpath("//*[@id='entorno-pt']")
trans.send_keys("024100")
trans.send_keys("webdrive" +Keys.ENTER)
time.sleep(3)
#driver.save_screenshot("Anula0.png")
