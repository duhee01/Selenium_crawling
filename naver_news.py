import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 
from datetime import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

dates = [] #날짜저장
titles = [] #제목저장
contents = [] #본문저장
i = 1 
k = 1
p = 2


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def clean_text(news_text):
    text = re.sub('[-=+,#/\?:^.@*\"※~【▶◀ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', ' ', news_text)
    text = text.replace("\n","",1000)
    return text

def clean_date(date_text):
    date = datetime.strptime(date_text, '%Y.%m.%d')
    date = date.strftime('%Y-%m-%d')
    return date

driver=set_chrome_driver()

driver.implicitly_wait(10)

webpage = driver.get('https://news.naver.com')#네이버창 열기

driver.maximize_window() #창 최대



# header 설정
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
           "Accept-Encoding": "*",
           "Connection": "keep-alive",
           "X-Naver_Client-Id":"0jGhGxgBPvscKc4KztGE",
           "X-Naver-Client-Secret":"7V01treriv"
           }
payload = {'param1': '1', 'param2': '2'}
url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101'
# 요청 
r = requests.get(url, params=payload, headers=headers)

print(r)


#'경제' 기사 크롤링
wait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[3]/a/span'))).click()
#driver.find_element(By.XPATH,'/html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[3]/a/span').click()
for n in range(1000000):
    try:
        page_find = '#paging > a:nth-child('+str(p)+')'
        url =  '//*[@id="section_body"]/ul['+str(i)+"]/li["+str(k)+"]/dl/dt[2]/a"
        if url != '//*[@id="section_body"]/ul['+str(i)+"]/li["+str(k)+"]/dl/dt[2]/a":
            url = '//*[@id="section_body"]/ul['+str(i)+"]/li["+str(k)+"]/dl/dt/a"
            wait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, url))).click()
        else:
            url =  '//*[@id="section_body"]/ul['+str(i)+"]/li["+str(k)+"]/dl/dt[2]/a"
            wait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, url))).click()
        #driver.find_element(By.XPATH, url).click()
        sleep(0.5)
        date_time = driver.find_element(By.XPATH, '//*[@id="ct"]/div[1]/div[3]/div[1]/div/span').text[:10]         
        date = clean_date(date_time)
        dates.append(date)

        title = driver.find_element(By.XPATH, '//*[@id="ct"]/div[1]/div[2]/h2').text[:]
        titles.append(title)

        text = str(driver.find_element(By.XPATH,'//*[@id="dic_area"]').text)
        news_text = clean_text(text)
        contents.append(news_text)
        
        news_df = pd.DataFrame({'title':titles,'date':dates,'content':contents})
        news_df.to_csv('C:\\Users\\user\\OneDrive\\문서\\GitHub\\Selenium_crawling\\news\\NaverNews.csv',index=False,encoding='utf-8-sig')
        sleep(1.5)
        driver.back()
    
        if k < 6:
            k += 1

        if k > 5:
            i += 1
            k = 1

        if i == 5:
            page_find = '#paging > a:nth-child('+str(p)+')'
            #page_click = driver.find_element(By.CSS_SELECTOR, page_find).click()
            wait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, page_find))).click()
            i = 1
            k = 1
            p += 1
            sleep(1)

        if p == 10:
            #driver.find_element(By.CSS_SELECTOR, "#paging > a._paging.next.nclicks\(air\.next\)").click()
            wait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#paging > a._paging.next.nclicks\(air\.next\)"))).click()
            p = 3
            sleep(1)
           

    
    except Exception as error:
        print(error)
        break


  

            
            
        
