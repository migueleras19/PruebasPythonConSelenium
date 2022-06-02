from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")
driver.get("https://github.com/login")

usuario = driver.find_element_by_id("login_field")
usuario.send_keys("miguel.eras83@gmail.com")

clave = driver.find_element_by_name("password")
clave.send_keys("miguel151990*")

clave.send_keys("webdrive" + Keys.ENTER)
time.sleep(10)