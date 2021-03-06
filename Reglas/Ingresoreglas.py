from csv import reader
from distutils.command.clean import clean
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import unittest
import csv
import time


class Testingreso002024(unittest. TestCase):

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

        with open('rules.csv') as File:
            reader = csv.DictReader(File, delimiter=',')
            for fila in reader:

                time.sleep(1)
                x = driver.find_element_by_xpath("//*[@id='c_F1creglabpm_0']")
                time.sleep(1)
                
                x.send_keys(fila["num"])
                time.sleep(1)
                x.send_keys(Keys.ENTER)
                time.sleep(1)                
                
                print('Ingreso de numero de regla...')
                
                y = driver.find_element_by_name("archivo_0")
                #time.sleep(1.5)
                y.send_keys(fila["regla"])
                time.sleep(1.5)

                z = driver.find_element_by_name("f1_hoja_regla")
                time.sleep(1)
                z.send_keys(fila["cal"])
                time.sleep(1)

                teclear = ActionChains(driver)
                teclear.send_keys(Keys.F12).perform()
                time.sleep(5)
                              
                
                print('......Se ingreso la regla......')
                #print({num} and {regla})
                

                teclear = ActionChains(driver)
                teclear.send_keys(Keys.F2).perform()
                time.sleep(1.5)
                refresh = driver.find_element_by_xpath("/html/body/div[13]/div[2]/div/table/tr[2]/td[1]/button").click()
                time.sleep(4)                
                driver.close()
                

if __name__ == '__main__':
    unittest.main()

