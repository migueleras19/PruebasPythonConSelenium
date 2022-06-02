import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")
driver.maximize_window()
driver.get("http://10.16.5.161:8380/WEB3/ingreso.html")
usuario = driver.find_element_by_id("usuario")
usuario.send_keys("admin")
clave = driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
clave.send_keys("hdkjhkjhkhkasda")
clave.send_keys("webdrive" + Keys.ENTER)
time.sleep(3)
trans = driver.find_element_by_xpath("//*[@id='entorno-pt']")
trans.send_keys("042008")
trans.send_keys("webdrive" +Keys.ENTER)
time.sleep(1)
#driver.save_screenshot("Anula0.png")
#identificacion = driver.find_element_by_name ("w2_cidentificacion")
cuenta = driver.find_element_by_id("c_w2_ccuenta_0")
time.sleep(1)
#identificacion.send_keys("1712805157")
cuenta.send_keys("0011778712")
time.sleep(3)
#driver.save_screenshot("Anula1.png")
buscar = ActionChains(driver)
buscar.send_keys(Keys.ENTER).perform()
time.sleep(2)
seleccionar = driver.find_element_by_xpath("//*[@id='c_F4seleccionar_0']").click()
time.sleep(1)
