#정규표현식 import re 모듈 이용해서 특수문자 없애기

import re

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from time import sleep 

f = open("./news/news_text.txt","w")

 

#chrome브라우저 열기

def set_chrome_driver():

    chrome_options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return driver

driver=set_chrome_driver()

driver.implicitly_wait(10)

webpage = driver.get('https://news.naver.com')#네이버창 열기

driver.maximize_window() #창 최대

"""
#경제 페이지 개수세기

driver.find_element(By.XPATH,'/html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[3]/a/span').click()

while(1):
    driver.find_element_by_css_selector("#paging > a._paging.next.nclicks\(air\.next\)").click()
    sleep(2)
"""   
 
#'경제' 기사들어가기

driver.find_element(By.XPATH,'/html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[3]/a/span').click()

driver.find_element(By.XPATH,'//*[@id="section_body"]/ul[1]/li[2]/dl/dt[2]/a').click() #첫번재 묶음에서 기사 1번 제목클릭

text = str(driver.find_element(By.XPATH,'//*[@id="dic_area"]').text)

print(text)


 

def clean_text(news_text):

  text = re.sub('[-=+,#/\?:^.@*\"※~【▶◀ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', ' ', news_text)

  text = text.replace("\n","",1000)

  return text


news_text = clean_text(text)

#print(news_text)

#텍스트파일에 쓰기

f.write(news_text)

f.close()

 


 

"""

txt파일로 저장해서

news목록 만들기

"""

 

"""

기사들이 6개로 4묶음으로 구성되어있음 - 고정되어있는 헤드라인 뉴스 제외하고 한페이지 당 24개 뉴스기사가 있음.

//*[@id="section_body"]/ul[1]/li[1] -> ul[1]에서 "1"은 4묶음중 첫번째 묶음

 

//*[@id="section_body"]/ul[2]/li[1]  ->2번째 묶음

 

 

페이지가 변해도 위의 xpath 태그는 위와같이 같았음.

 

//*[@id="section_body"]/ul[1]/li[1]/dl/dt[2]/a  ->첫번째 묶음에서 기사1번 제목클릭 

 

//*[@id="section_body"]/ul[1]/li[2]/dl/dt[2]/a   ->첫번재 묶음에서 기사 2번 제목 클릭

 

"""
