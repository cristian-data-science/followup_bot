import time
from datetime import date, timedelta, datetime
import unittest
from time import sleep
from datetime import date, timedelta



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import pandas as pd

import sys
sys.path.append("variables")
from variables import var as v


class funciones_globales():
    
    def __init__(self, driver):
        self.driver = driver

    
    def recolect(self, url_fupbi, user, passw):
        self.driver.get(url_fupbi)
        driver = self.driver
        user = driver.find_element(By.XPATH, value= '//*[@id="user_login"]')
        user.send_keys(v.user)
        passw = driver.find_element(By.XPATH, value= '//*[@id="user_password"]')
        passw.send_keys(v.passw)
        enter_b = driver.find_element(By.XPATH, value= '//*[@id="new_user"]/div[3]/div/input')
        enter_b.click()


        boton_fecha = driver.find_element(By.XPATH, value='//*[@id="main_content"]/div/div/div/div/div/div[1]/div[2]/form/div[1]/div[1]').click()
        #ini = date.today() - timedelta(1460)
        ini = datetime.strptime("2019-01-01", "%Y-%m-%d")
        #ini = "2019-09-01"
        #ini = str(ini)
        fin = datetime.strptime("2022-09-09", "%Y-%m-%d")
        #fin = str(fin)
        df3 = pd.DataFrame()
        df_final = pd.DataFrame()
        
        while ini <= fin:
            # Ingresando fecha de inicio
            #print("### Ingresando fecha de inicio ###")

            ini_box = driver.find_element(By.XPATH, value ='//*[@id="ng-app"]/body/div[3]/div[2]/div[1]/input')
            ini_box.clear()
            ini_box.click()

            #ini = datetime.strptime(ini, "%Y-%m-%d")
            #ini = str(ini.date())
            ini_box.send_keys(str(ini))
            ini_box.send_keys(Keys.ENTER)
            #sleep(1)

            # Ingresando fecha final
            # print("### Ingresando fecha final ###")
            final_box = driver.find_element(By.XPATH, value ='//*[@id="ng-app"]/body/div[3]/div[3]/div[1]/input')
            final_box.clear()
            final_box.click()
            final_box.send_keys(str(ini))
            final_box.send_keys(Keys.ENTER)
            #sleep(1)

            # Click en boton buscar
            #print("### Click en boton buscar ###")
            buscar_b = driver.find_element(By.XPATH, value= '//*[@id="main_content"]/div/div/div/div/div/div[1]/div[2]/form/div[4]/a')
            buscar_b.click()

            #columns = driver.find_elements(By.XPATH, value='//*[@id="main_content"]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[3]/div/div[1]/div/div/div[1]/table/thead/tr')
            #cols = [col.text for col in columns]
            #print(cols)

            #print("Sumando día a la fecha de inicio")
            #ini = datetime.strptime(ini, "%Y-%m-%d")
            #print(ini)
            ini = ini + timedelta(1)
            
            boton_fecha = driver.find_element(By.XPATH, value='//*[@id="main_content"]/div/div/div/div/div/div[1]/div[2]/form/div[1]/div[1]').click()

            sleep(2)

            #datos = driver.find_elements(By.XPATH, value= '//*[@id="main_content"]/div/div/div/div/div/div[*]/div/div/div/div[*]/div[*]/div/div[*]/div/div/div[*]/table/tbody/tr[*]/td[*]')

            #z=1
            datos2 = driver.find_elements(By.XPATH, value= f'//*[@id="main_content"]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[3]/div/div[1]/div/div/div[1]/table/tbody/tr[*]')

            #datos = [ linea.text for linea in datos ]
            
            test2 = []
            for linea in datos2:
                datos2 = driver.find_elements(By.XPATH, value= f'//*[@id="main_content"]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[3]/div/div[1]/div/div/div[1]/table/tbody/tr[*]')
                
                #linea = linea.text
                #sleep(1)
                try:
                    linea = linea.text.replace("\n", " ")
                    linea = linea.replace(",", ".")
                    linea = linea.replace("    ", ",")
                    linea = linea.replace(" ", ",")
                    linea = linea.replace(",,", ",")
                    linea = linea.replace("COSTANERA,CENTER,", "COSTANERA CENTER,").replace("LA,DEHESA,", "LA DEHESA,").replace("%,", "%").replace("PUERTO,VARAS", "PUERTO VARAS")
                    linea = linea.replace("ALTO,LAS,CONDES", "ALTO LAS CONDES")
                    linea = linea.replace(".", "")
                except:
                    print("no se pudo hacer el reemplazo")
                linea = linea.strip()
                linea = linea.split(sep=',')
              
                ini2 = ini 
                ini2 = str(ini2)

                """if linea[0] == ini2:
                    test2.append(linea)
                else:
                    ini = ini - timedelta(1)
                    print("Repitiendo loop de fecha")"""



                test2.append(linea)
                #print(linea)
                #print(test2[0][0])"""

                 #print(linea)
                


                
                
                
              
                #print(df_final)    
                #print(" ############################################################################# ")
            

            # logica para volver a recorrer fecha no insertada en el loop
            zz = ini + timedelta(-1)
            zz = zz.date()
            zz = str(zz)
            
            if test2[0][0] == zz:
                print(f'Fecha en vuelta de df: {test2[0][0]}')     
                df_final = df_final.append(test2)
                df_final = df_final.dropna()
            else:
                
                print("Volviendo a pasar fecha inexistente en df al loop")
                print(f'Fecha corregida al loop {ini + timedelta(-1)}')
                ini = ini + timedelta(-1)

            
            #print(f'Fecha de variable ini: {zz}')

        cols = ['fecha desde','fecha hasta','tienda','entradas','venta','tickets','artículos','ticket promedio','artículos por ticket',"tasa de conversión"]
        df_final.columns = cols
        df_final['entradas'] = df_final['entradas'].astype(int)
        df_v2 = df_final[['fecha desde','tienda','entradas']] 
        df_v2['fecha desde'] = pd.to_datetime(df_v2['fecha desde'])
        pd.to_datetime  
        df_v2.to_excel("entradas_historicas_fup.xlsx", index=False)  
               

