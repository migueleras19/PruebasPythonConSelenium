from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")
driver.get("https://twitter.com/login")


usuario = driver.find_element_by_name("session[username_or_email]")
usuario.send_keys("miguleras")

clave = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
clave.send_keys("")
clave.send_keys("Keys.ENTER")

time.sleep(5)