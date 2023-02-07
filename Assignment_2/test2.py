#from selenium import webdriver

#DRIVER = 'chromedriver'
#driver = webdriver.Chrome(DRIVER)
#driver.get('https://www.aliexpress.com/af/men-wallet.html?spm=a2g0o.best.1000002.0&initiative_id=SB_20230206231430&origin=n&dida=y')
#screenshot = driver.save_screenshot('my_screenshot.png')
#driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(30)

URL = 'https://ui.vision/rpa/x/desktop-automation/screen-scraping'

driver.get(URL)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height'))                                                                                                              
driver.find_element(By.TAG_NAME, 'body').screenshot('web_screenshot.png')

driver.quit()

import test
