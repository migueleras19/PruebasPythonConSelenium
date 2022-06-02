import unittest
from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import csv


driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")
driver.get("http://10.16.5.94:8380/WEB3/ingreso.html")
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
transaccion.send_keys("03-6401")
time.sleep(2)
transaccion.send_keys(Keys.ENTER)
time.sleep(3)

with open('cargaDatos.csv', 'rb') as File:  
    reader = csv.DictReader(File, delimiter=',')
    for fila in reader:
        
        cuenta = driver.find_element_by_id("c_ccuenta_0")
        cuenta.clear()
        time.sleep(2)
        cuenta.send_keys(fila["cuenta"])
        time.sleep(2)
        cuenta.send_keys(Keys.ENTER)
        time.sleep(5)
        
        
        valor = driver.find_element_by_id("c_vEfectivo_0")
        valor.clear()
        valor.send_keys(fila["valor"])
        time.sleep(3)
        driver.find_element_by_id("c_btnIngresoDesgloseDenominaciones_0").click()
        time.sleep(3)
        
        numDeno = 0
                
        if int(fila["cant100"]) != 0:
            bille1 = driver.find_element_by_id("c_fncDetalleEfectivoValorDenominacion_"+str(numDeno))
            bille1.clear()
            bille1.send_keys("100")
            time.sleep(2)
            cantbille1 = driver.find_element_by_id("c_fncDetalleEfectivoCantidad_"+str(numDeno))
            cantbille1.clear()
            cantbille1.send_keys(fila["cant100"])
            numDeno += 1
            time.sleep(2)
        
        if int(fila["cant50"]) != 0:
            bille2 = driver.find_element_by_id("c_fncDetalleEfectivoValorDenominacion_"+str(numDeno))
            bille2.clear()
            bille2.send_keys("50")
            time.sleep(2)
            cantbille2 = driver.find_element_by_id("c_fncDetalleEfectivoCantidad_"+str(numDeno))
            cantbille2.clear()
            cantbille2.send_keys(fila["cant50"])
            numDeno += 1
            time.sleep(2)
        
        if int(fila["cant20"]) != 0:
            bille3 = driver.find_element_by_id("c_fncDetalleEfectivoValorDenominacion_"+str(numDeno))
            bille3.clear()
            bille3.send_keys("20")
            time.sleep(2)
            cantbille3 = driver.find_element_by_id("c_fncDetalleEfectivoCantidad_"+str(numDeno))
            cantbille3.clear()
            cantbille3.send_keys(fila["cant20"])
            numDeno += 1
            time.sleep(2)
        
        if int(fila["cant10"]) != 0:
            bille4 = driver.find_element_by_id("c_fncDetalleEfectivoValorDenominacion_"+ str(numDeno))
            bille4.clear()
            bille4.send_keys("10")
            time.sleep(2)
            cantbille4 = driver.find_element_by_id("c_fncDetalleEfectivoCantidad_"+str(numDeno))
            cantbille4.clear()
            cantbille4.send_keys(fila["cant10"])
            numDeno += 1
            time.sleep(2)
        
        if int(fila["cant5"]) != 0:
            bille5 = driver.find_element_by_id("c_fncDetalleEfectivoValorDenominacion_"+str(numDeno))
            bille5.clear()
            bille5.send_keys("5")
            time.sleep(2)
            cantbille5 = driver.find_element_by_id("c_fncDetalleEfectivoCantidad_"+str(numDeno))
            cantbille5.clear()
            cantbille5.send_keys(fila["cant5"])
            time.sleep(2)
        
        driver.find_element_by_name("btnAgregarDenominaciones_button").click()
        time.sleep(3)
        
        driver.find_element_by_xpath("//ul[@class=' tab-bar tabs']/li[2]").click()
        time.sleep(3)
        
        cont = 0

        for bille100 in range(int(fila["cant100"])):
            seriebille1 = driver.find_element_by_id("c_f1numeroSerie_"+str(cont))
            cont += 1
            seriebille1.clear()
            seriebille1.send_keys("bille100"+str(bille100))
            time.sleep(2)
            
        for bille50 in range(int(fila["cant50"])):
            seriebille2 = driver.find_element_by_id("c_f1numeroSerie_"+str(cont))
            cont += 1
            seriebille2.clear()
            seriebille2.send_keys("bille50"+str(bille50))
            time.sleep(2)

        driver.find_element_by_xpath("//button[@title='Guardar']").click()      
        time.sleep(15)
        
        
        transaccion = driver.find_element_by_id("entorno-pt")
        transaccion.clear()
        transaccion.send_keys("03-6401")
        time.sleep(2)
        transaccion.send_keys(Keys.ENTER)
        time.sleep(3)
driver.close()
driver.quit()
