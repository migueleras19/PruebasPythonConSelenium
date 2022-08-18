from argparse import Action
from csv import reader
from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from turtle import clear
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import unittest, time, csv, re


class Testmiguel(unittest. TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver")

    def test(self):
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("https://www.demoblaze.com/")
        
        
        
    #Selecionar el logIn
        driver.find_element_by_id('login2').click()
        time.sleep(2)
    #Ingreso de User y passord
        user = driver.find_element_by_xpath("//*[@id='loginusername']")
        user.send_keys("pruebamiguel")
        contra = driver.find_element_by_id("loginpassword")
        contra.send_keys("12345")
        time.sleep(2)
        driver.save_screenshot(r'.\evidencia\ingreso.png')
        boton = driver.find_element_by_xpath("//*[@id='logInModal']/div/div/div[3]/button[2]")
        boton.click()
        time.sleep(2)
    #Selecion del primer producto
        cel = driver.find_element_by_id("itemc").click()
        time.sleep(2)
        cel = driver.find_element_by_link_text("Nexus 6").click()
        time.sleep(2)
        cel = driver.find_element_by_xpath("//*[@id='tbodyid']/div[2]/div/a").click()
        time.sleep(2)
        aler = driver.switch_to.alert
        aler.accept()
        time.sleep(2)
        driver.save_screenshot(r'.\evidencia\producto1.png')
        home = driver.find_element_by_css_selector("#navbarExample > ul > li.nav-item.active > a").click()
        time.sleep(2)

    #seleccionar segundo producto
        lap = driver.find_element_by_link_text("Laptops").click()
        time.sleep(2)
        lap = driver.find_element_by_link_text("MacBook air").click()
        time.sleep(2)
        lap = driver.find_element_by_link_text("Add to cart").click()
        time.sleep(2)
        aler = driver.switch_to.alert
        aler.accept()
        time.sleep(2)
        driver.save_screenshot(r'.\evidencia\producto2.png')

    #Aceptar la compra
        cart = driver.find_element_by_link_text("Cart").click()
        time.sleep(2)
        driver.save_screenshot(r'.\evidencia\carrito.png')
        cart = driver.find_element_by_css_selector("#page-wrapper > div > div.col-lg-1 > button").click()
        time.sleep(2)

    #Ingresar datos para realizar el pedido, en esta ocuacion utilizare un archivo csv pra llenar los datos que solicita.

        with open('Datos.csv') as File:
            reader = csv.DictReader(File, delimiter=',')

            for fila in reader:
                
                accion = ActionChains(self.driver)
                accion.key_down(Keys.TAB)
                
                nombre =  driver.find_element_by_id("name")
                nombre.clear()
                nombre.send_keys(fila['nombre'])
                time.sleep(1)

                pais = driver.find_element_by_id("country")
                pais.clear()
                pais.send_keys(fila['pais'])
                time.sleep(1)

                cuidad = driver.find_element_by_id("city")
                cuidad.clear()
                cuidad.send_keys(fila['cuidad'])
                time.sleep(1)

                tc = driver.find_element_by_id("card")
                tc.clear()
                tc.send_keys(fila['tc'])
                time.sleep(1)

                month = driver.find_element_by_id("month")
                month.clear()
                month.send_keys(fila['month'])
                time.sleep(1)

                year = driver.find_element_by_id("year")
                year.clear()
                year.send_keys(fila['year'])
                time.sleep(1)
                driver.save_screenshot(r'.\evidencia\datosperosonales.png')

                #Finalizar compra

                comprar = driver .find_element_by_css_selector("#orderModal > div > div > div.modal-footer > button.btn.btn-primary").click()
                time.sleep(2)
                driver.save_screenshot(r'.\evidencia\compra.png')
                comp = driver.find_element_by_css_selector("body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > div > button").click()
                time.sleep(2)


                          
                
if __name__ == "__main__":
    unittest.main()

    
    