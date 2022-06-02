from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

self.driver = webdriver.Chrome('../chromedriver')
driver.get("http://10.16.5.88:9380/WEB3/ingreso.html")

usuario = driver.find_element_by_id("usuario")
usuario.send_keys("ue01000663")

clave = driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
clave.send_keys("ue01000663")
clave.send_keys("webdrive" + Keys.ENTER)
time.sleep(1)

trans = driver.find_element_by_xpath("//*[@id='entorno-pt']")
trans.send_keys("044001")
new_var = trans.send_keys("webdrive" +Keys.ENTER)
new_var	
time.sleep(1)

ci = driver.find_element_by_xpath("//*[@id='c_w2_cidentificacion_0']")
ci.send_keys('1104638091')
ccuenta = driver.find_element_by_xpath("//*[@id='c_w2_ccuenta_0']")
ccuenta.send_keys('0011778712')
#time.sleep(1)
buscar = ActionChains(driver)
buscar.send_keys(Keys.ENTER).perform()
time.sleep(3)
titular = driver.find_elements_by_xpath("//a[contains(text(),'Titulares/Firmantes')]//parent::li")[0]
titular.click()
time.sleep(3)
condicion = driver.find_elements_by_xpath("//a[contains(text(),'Condiciones De Giro')]//parent::li")[0]
condicion.click()
time.sleep(3)
#tarjeta = driver.find_element_by_xpath("//a[contains(text(),'¡Tarjeta Debito!')]//parent::li")[0]
#tarjeta.click()
time.sleep(3)