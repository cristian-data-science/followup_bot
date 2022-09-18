import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from funciones.func import funciones_globales
from selenium.webdriver.chrome.options import Options
import pandas as pd

#import sys
#sys.path.append("variables")
from variables import var as v

chrome_options = Options()
#chrome_options.headless = True
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--log-level=3")



class base_test(unittest.TestCase):

    def setUp(self):
 
        # Descomentar linea siguiente para ejecución en windows
        self.driver = webdriver.Chrome(executable_path= r'C:\chrome_driver\chromedriver.exe',options=chrome_options)
        
        # Descomentar linea siguiente para ejecución en linux        
        #self.driver = webdriver.Chrome(options=chrome_options)        
        
        #driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
        driver = self.driver
        # este implicity contrala el time out de la función scann multipaginas
        driver.implicitly_wait(5)
        driver.maximize_window()
        #driver.get("https://patagonia-testpos.sandbox.operations.dynamics.com/")        

    def test1(self):
        driver = self.driver
        f = funciones_globales(driver)
        f.recolect(v.url_fupbi, v.user, v.passw)



    def tearDown(self):
        driver = self.driver
        driver.close()
        

if __name__ == '__main__':
    unittest.main()
