from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



#chrome브라우저 열기
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver
driver=set_chrome_driver()
driver.implicitly_wait(5)
driver.get('https://news.naver.com')#네이버창 열기
driver.maximize_window() #창 최대

driver.find_element(By.XPATH,'')
