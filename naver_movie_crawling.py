import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("./chromedriver.exe")




url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&tg=0&date=20200609"


driver.get(url)

# 로그인 준내 빨리하고 원래 페이지로 돌아오기(안하면 청불영화 정보 못긁어옴)
time.sleep(10)

url2 = driver.current_url

T = []
S = []
A = []
C = []
R = []
show = []
M = []
Act = []
Rat = []
I = []
Con = []
H = []

for num in range(1, 41):
    url = url2 + "&page={num}".format(num=num)
    driver.get(url)
    
    detail_list = []
    movie_detail = driver.find_elements_by_css_selector('.tit5 a')
    for detail in movie_detail:
        detail_list.append(detail.get_attribute("href"))
        
    for detail_url in detail_list:
        driver.get(detail_url)
        
        try:
            title = driver.find_elements_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > h3 > a')[0].text
            summary = driver.find_elements_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1)')[0].text
            Audience_score = driver.find_elements_by_css_selector('#actualPointPersentBasic > div > span > span')[0].text
            
            Audience_score = Audience_score[7:11]
            
            if Audience_score == "없음":
                Audience_score = 0
            else:
                Audience_score = float(Audience_score)
            
            country = driver.find_elements_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(2) > a')[0].text
            Release_date = driver.find_elements_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(4)')[0].text
            Showtimes = driver.find_elements_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3)')[0].text
            movie_director = driver.find_elements_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a')[0].text
            Actors_list = driver.find_elements_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(6) > p > a')
            Actors = ''
            for i in range(len(Actors_list)):
                if i != (len(Actors_list)-1):
                    Actors += Actors_list[i].text + ', '
                else:
                    Actors += Actors_list[i].text

            Rating = driver.find_elements_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(8) > p > a:nth-child(1)')[0].text
            
            code = detail_url[-6:]
            if code[0] == '=':
                code = code.replace('=','')

            imgUrl = 'https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode={}'.format(code)
            
            content = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/div/div[1]/p').text
            heart = driver.find_elements_by_css_selector('.u_likeit_module .u_cnt')[1].text
            if ',' in heart:
                heart = heart.replace(',', '')
            
            heart = int(heart)

            T.append(title)
            S.append(summary)
            A.append(Audience_score)
            C.append(country)
            R.append(Release_date)
            show.append(Showtimes)
            M.append(movie_director)
            Act.append(Actors)
            Rat.append(Rating)
            I.append(imgUrl)
            Con.append(content)
            H.append(heart)

        except:
            continue

df_movie = pd.DataFrame(data = {"title": T, "summary": S, "Audience_score": A, "country": C,
                             "Release_date": R, "Showtimes": show, "movie_director": M, "Actors": Act,
                             "Rating": R, "imgUrl": I, "content": Con, "heart": H})

df_movie.to_csv("movie_data_none_index.csv", encoding = "UTF-8-sig", index=False)