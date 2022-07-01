#정규표현식 import re 모듈 이용해서 특수문자 없애기

import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 
from datetime import datetime
import pandas as pd


dates = [] #날짜저장
titles = [] #제목저장
contents = [] #본문저장
i = 1
k = 1
p = 2
#chrome브라우저 열기

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
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

"""
#경제 페이지 개수세기
driver.find_element(By.XPATH,'/html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[3]/a/span').click()
for i in range(1000):
    try:
        page_find = '#paging > a:nth-child('+str(p)+')'
        if p%10 != 0:
            page_find = '#paging > a:nth-child('+str(p)+')'
            driver.find_element(By.CSS_SELECTOR, page_find).click()
            p += 1
            page_number += 1
            sleep(1)
            print(page_number)

        elif p%10 == 0:
            driver.find_element(By.CSS_SELECTOR,"#paging > a._paging.next.nclicks\(air\.next\)").click()
            p = 3
            sleep(1)
        elif page_find == "#paging > strong":
            p += 1

            
    except:
            driver.find_element
            print("페이지 조사 끝")
            break
        #2번째 페이지 부터 2페이지씩 누락됨.
"""

#'경제' 기사 크롤링
driver.find_element(By.XPATH,'/html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[3]/a/span').click()
for n in range(1000):
    try:
        page_find = '#paging > a:nth-child('+str(p)+')'
        url =  '//*[@id="section_body"]/ul['+str(i)+"]/li["+str(k)+"]/dl/dt[2]/a"
        driver.find_element(By.XPATH, url).click()
        #날짜
        date_time = driver.find_element(By.XPATH, '//*[@id="ct"]/div[1]/div[3]/div[1]/div/span').text[:10]
        date = clean_date(date_time)
        dates.append(date)
        #print(dates)
        #제목
        title = driver.find_element(By.XPATH, '//*[@id="ct"]/div[1]/div[2]/h2').text[:]
        titles.append(title)
        #print(titles)
        #본문
        text = str(driver.find_element(By.XPATH,'//*[@id="dic_area"]').text)
        news_text = clean_text(text)
        contents.append(news_text)
        #print(contents)
        sleep(1)
        driver.back()
        
        if k < 6:
            k += 1
            
        if k == 6:
            i += 1
            k = 1
            
        if i == 5:
            page_find = '#paging > a:nth-child('+str(p)+')'
            driver.find_element(By.CSS_SELECTOR, page_find).click()
            i = 1
            k = 1
            p += 1
            sleep(1)

        if p == 10:
            driver.find_element(By.CSS_SELECTOR, "#paging > a._paging.next.nclicks\(air\.next\)").click()
            p = 3
            sleep(1)

            
            
    except:
        print("스크래핑 완료")
        news_df = pd.DataFrame({'title':titles,'date':dates,'content':contents})
        news_df.to_csv('C:\\Users\\user\\OneDrive\\문서\\GitHub\\Beautifulsoup_base\\news\\NaverNews.csv',index=False,encoding='utf-8-sig')
        break
            
            
        
