from os import sep
import unittest
from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import csv


class Deposito(unittest. TestCase):
      def setUp(self):
         self.driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")

      def testDeposito(self):
          driver = self.driver
          driver.get("http://10.16.5.88:9380/WEB3/ingreso.html")
          driver.maximize_window()
          usuario = driver.find_element_by_id("usuario")
          usuario.clear()
          time.sleep(3)
          usuario.send_keys("BA01001601")
          clave = driver.find_element_by_xpath("//input[@type='password']")
          clave.send_keys("454545454545" + Keys.ENTER)
          time.sleep(3)
          transaccion = driver.find_element_by_id("entorno-pt")
          transaccion.send_keys("03-6401" + Keys.ENTER)
          time.sleep(3)
          with open('cargaDatos.csv', 'rb') as File:
              reader = csv.DictReader(File, delimiter=',')
              for fila in reader:
        
                  cuenta = driver.find_element_by_id("c_ccuenta_0")
                  cuenta.clear()
                  time.sleep(3.5)
                  cuenta.send_keys(fila["cuenta"])
                  time.sleep(3)
                  cuenta.send_keys(Keys.ENTER)

                  time.sleep(5)
                  valor = driver.find_element_by_id("c_vEfectivo_0")
                  valor.clear()
                  valor.send_keys(fila["valor"])
                  time.sleep(3)
                  driver.find_element_by_id("c_btnIngresoDesgloseDenominaciones_0").click()
                  time.sleep(5)
                
                  numDeno = 0
                  
                
                  if int(fila["cant100"]) != 0:
                      bille1 = driver.find_element_by_id("c_fncDetalleEfectivoValorDenominacion_"+str(numDeno))
                      bille1.clear()
                      bille1.send_keys("100")
                      time.sleep(3)
                      cantbille1 = driver.find_element_by_id("c_fncDetalleEfectivoCantidad_"+str(numDeno))
                      cantbille1.clear()
                      cantbille1.send_keys(fila["cant100"])
                      numDeno += 1
                      time.sleep(3)
    
                  if int(fila["cant50"]) != 0:
                      bille2 = driver.find_element_by_id("c_fncDetalleEfectivoValorDenominacion_"+str(numDeno))
                      bille2.clear()
                      bille2.send_keys("50")
                      time.sleep(3)
                      cantbille2 = driver.find_element_by_id("c_fncDetalleEfectivoCantidad_"+str(numDeno))
                      cantbille2.clear()
                      cantbille2.send_keys(fila["cant50"])
                      numDeno += 1
                      time.sleep(3)
    
                  if int(fila["cant20"]) != 0:
                      bille3 = driver.find_element_by_id("c_fncDetalleEfectivoValorDenominacion_"+str(numDeno))
                      bille3.clear()
                      bille3.send_keys("20")
                      time.sleep(3)
                      cantbille3 = driver.find_element_by_id("c_fncDetalleEfectivoCantidad_"+str(numDeno))
                      cantbille3.clear()
                      cantbille3.send_keys(fila["cant20"])
                      numDeno += 1
                      time.sleep(3)
    
                  if int(fila["cant10"]) != 0:
                      bille4 = driver.find_element_by_id("c_fncDetalleEfectivoValorDenominacion_"+ str(numDeno))
                      bille4.clear()
                      bille4.send_keys("10")
                      time.sleep(3)
                      cantbille4 = driver.find_element_by_id("c_fncDetalleEfectivoCantidad_"+str(numDeno))
                      cantbille4.clear()
                      cantbille4.send_keys(fila["cant10"])
                      numDeno += 1
                      time.sleep(3)
    
                  if int(fila["cant5"]) != 0:
                      bille5 = driver.find_element_by_id("c_fncDetalleEfectivoValorDenominacion_"+str(numDeno))
                      bille5.clear()
                      bille5.send_keys("5")
                      time.sleep(3)
                      cantbille5 = driver.find_element_by_id("c_fncDetalleEfectivoCantidad_"+str(numDeno))
                      cantbille5.clear()
                      cantbille5.send_keys(fila["cant5"])
                      time.sleep(3)
        
                  driver.find_element_by_name("btnAgregarDenominaciones_button").click()
                  time.sleep(5)
    
                  driver.find_element_by_xpath("//ul[@class=' tab-bar tabs']/li[2]").click()
                  time.sleep(5)
        
                  cont = 0

                  for bille100 in range(int(fila["cant100"])):
                      seriebille1 = driver.find_element_by_id("c_f1numeroSerie_"+str(cont))
                      cont += 1
                      seriebille1.clear()
                      seriebille1.send_keys("bille100"+str(bille100))
                      time.sleep(1)
        
                  for bille50 in range(int(fila["cant50"])):
                      seriebille2 = driver.find_element_by_id("c_f1numeroSerie_"+str(cont))
                      cont += 1
                      seriebille2.clear()
                      seriebille2.send_keys("bille50"+str(bille50))
                      time.sleep()
                  driver.find_element_by_xpath("//button[@title='Guardar']").click()      
                  time.sleep(10)
    
        
                  transaccion = driver.find_element_by_id("entorno-pt")
                  transaccion.clear()
                  transaccion.send_keys("03-6401")
                  time.sleep(5)
                  transaccion.send_keys(Keys.ENTER)
                  time.sleep(5)
                  driver.close()
if __name__ == '__main__':
    unittest.main()
                  

