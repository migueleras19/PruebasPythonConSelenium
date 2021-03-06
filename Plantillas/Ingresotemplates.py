import unittest, csv, time
from selenium import webdriver
from distutils.command.clean import clean
from csv import reader
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class Testingreso122006(unittest. TestCase):

    def setUp(self ):
        self.driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")
    
    def test(self):
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        
        #Logeo al sistema Fitbank
        driver.get("http://10.16.5.88:9380/WEB3/ingreso.html")
        usuario = driver.find_element_by_id("usuario")
        usuario.send_keys("ue01000663")
        clave = driver.find_element_by_xpath("//*[@id='ingreso']/input[2]")
        clave.send_keys("hdkjhkjhkhkasda" + Keys.ENTER)
        time.sleep(1.5)

        print('Bienvenido', self )
        
        #ingreso a la transacion a subir los templates...
        transaccion = driver.find_element_by_id("entorno-pt")
        transaccion.send_keys("122006" + Keys.ENTER)
        time.sleep(1.5)

        #Con el siguiente archivo es donde localiza las plantillas a subir... 
        with open('templates.csv') as File:
            reader = csv.DictReader(File, delimiter=',')
            for fila in reader:
                print(fila)
                
               # Ingreso al subsitema y transacion...
                #sub.clear()
                time.sleep(1.5)
                sub = driver.find_element_by_id('c_C1Csubsistema_0')
                time.sleep(1.5)
                sub.send_keys(fila["sub"])
                time.sleep(1.5)
                sub.send_keys(Keys.TAB)  
                trans = driver.find_element_by_id('c_C5Ctransaccion_0')
                time.sleep(1.5)
                trans.send_keys(fila["trans"])
                time.sleep(1.5)
                trans.send_keys(Keys.ENTER)
                time.sleep(1.5)

                #Carga de la plantilla...
                print('Espere mientras se carga el plantilla...')

                plan = driver.find_element_by_name("plantilla_0")
                time.sleep(2)
                plan.send_keys(fila["plan"])
                time.sleep(2)


                teje = driver.find_element_by_id("c_f5tipo_0")
                
                time.sleep(1.5)
                teje.send_keys(fila["teje"])
                time.sleep(1.5)

                
                refe =  driver.find_element_by_name("f6referencia")
                refe.clear()
                time.sleep(1.5)
                refe.send_keys(fila["refe"])
                time.sleep(1.5)
                print(sub)
                
                teclear = ActionChains(driver)
                teclear.send_keys(Keys.F12).perform()
                time.sleep(4)

                print({sub, trans, plan})
                
                teclear = ActionChains(driver)
                teclear.send_keys(Keys.F2).perform()
                time.sleep(2)
                driver.find_element_by_xpath("/html/body/div[13]/div[2]/div/table/tr[2]/td[1]/button").click()
                time.sleep(2)
                driver.close()

if __name__ == '__main__':
     unittest.main()