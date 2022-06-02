
from random import random
import unittest
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


class usando_unittest(unittest. TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")
    def testConsultacuentas3(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://10.16.5.84:8380/WEB3/ingreso.html")
        usuario = driver.find_element_by_id("usuario")
        usuario.send_keys("ue01000663")
        clave = driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
        clave.send_keys("hdkjhkjhkhkasda")
        clave.send_keys("webdrive" + Keys.ENTER)
        time.sleep(1.5)
        trans = driver.find_element_by_id("entorno-pt")
        trans.send_keys("044001")
        trans.send_keys("webdrive" + Keys.ENTER)
        time.sleep(3)

        
        with  open('datos.txt') as file:
            for i,line in enumerate(file):
                    #cuenta = (line)
                    # sep = ","
                    # dividir = cuenta.split(sep)
                    list = [7]
                    for x in range(1):
                        cuenta = (line)
                        sep = ","
                        dividir = cuenta.split(sep)
                        ccuenta = dividir[0]
                        gotdata = dividir[1]
                        try:
                            if(int(ccuenta)>1):
                                print(str(x+1) + " realizado " +(ccuenta))
                            ccuenta = driver.find_element_by_id("c_w2_ccuenta_0").send_keys(ccuenta + Keys.ENTER)
                            time.sleep(5)
                            list.append(ccuenta)
                        except Exception as e:
                                gotdata = 'null'
            #print ('Cuenta procesada',(ccuenta))
            #print(random.randrange(ccuenta))
            #print (random.randint(ccuenta))
        #ccuenta = driver.find_element_by_id("c_w2_ccuenta_0").send_keys(ccuenta + Keys.ENTER)
                
        time.sleep(15)
        #file.closeclose()
        #driver.close()
if __name__ == '__main__':
     unittest.main()