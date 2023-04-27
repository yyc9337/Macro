from selenium import webdriver
from selenium.webdriver.common.by import By

class config :
    URL = "https://www.dfmc.kr:8443/course/sports/fmcs/49"
    ID = 'yyc9337'
    PW = 'goyu9337!!'
    DATE = 20230504

driver = webdriver.Chrome()
driver.get(config.URL)
driver.implicitly_wait(2)

driver.find_element(By.ID, 'user_id').send_keys(config.ID) # ID
driver.find_element(By.ID, 'user_password').send_keys(config.PW) # Password
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/section/div/article/div/form/div/div/ul/li/div[1]/span/a').click() ##로그인 버튼
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/button[1]/span').click() 

for i in range(2) :
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/header/div/nav/div/div[1]/a').click() ## 사이드바에서 선택
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/header/div/nav/div/div[4]/ul/li[2]/a').click()## 사이드바에서 선택
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/header/div/nav/div/div[4]/ul/li[2]/div/ul/li[1]/a').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/section/div/article/div[1]/form/div/ul/li[3]/div/ul/li[3]').click()
    if i == 0 :
        driver.find_element(By.XPATH, '//*[@id="search"]/div/ul/li[4]/div/*[@id="place"]/li[2]').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/section/div/article/div[5]/ul/li[1]/div[1]/p/span[2]').click() ## 달력 다음달로 넘기기
        
        ## 넘기는거 가끔 오류먹어서 try, except 걸어야함
        try :
            driver.find_element(By.XPATH, '//*[@id="date-' + str(config.DATE) +'"]/dl').click()
        except :
            driver.refresh()
            driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/section/div/article/div[1]/form/div/ul/li[3]/div/ul/li[3]').click()
            driver.find_element(By.XPATH, '//*[@id="search"]/div/ul/li[4]/div/*[@id="place"]/li[2]').click()
            driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/section/div/article/div[5]/ul/li[1]/div[1]/p/span[2]').click()
            driver.find_element(By.XPATH, '//*[@id="date-' + str(config.DATE) +'"]/dl').click()
        driver.find_element(By.XPATH, '//*[@id="reservationList"]/ul/li[2]/div[2]/table/tbody/tr[4]/td/span').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/section/div/article/div[5]/div/span/a').click()
    elif i == 1 :
        ## 현재 토요일 로직이고 일요일 로직도 개발해야함
        break
        # try :
        # driver.find_element(By.XPATH, '//*[@id="date-' + str(config.DATE+1) +'"]/dl').click()
        # except :
        #     driver.refresh()
        #     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/section/div/article/div[1]/form/div/ul/li[3]/div/ul/li[3]').click()
        #     driver.find_element(By.XPATH, '//*[@id="search"]/div/ul/li[4]/div/*[@id="place"]/li[2]').click()
        #     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/section/div/article/div[5]/ul/li[1]/div[1]/p/span[2]').click()
        #     driver.find_element(By.XPATH, '//*[@id="date-' + str(config.DATE+1) +'"]/dl').click()
    driver.find_element(By.XPATH, '//*[@id="reservationList"]/ul/li[2]/div[2]/table/tbody/tr[4]/td/span').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/section/div/article/div[5]/div/span/a').click()

    driver.find_element(By.ID, 'users').send_keys('6') # 인원수
    driver.find_element(By.XPATH, '//*[@id="contents"]/article/form/div[10]/span').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/section/div/article/form/div[11]/span[2]/a').click()
    ## 1회 예약 완료

    for _ in range(3) :
        config.DATE = config.DATE + 7 

        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/header/div/nav/div/div[1]/a').click() ## 사이드바에서 선택
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/header/div/nav/div/div[4]/ul/li[2]/a').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/header/div/nav/div/div[4]/ul/li[2]/div/ul/li[1]/a').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/section/div/article/div[1]/form/div/ul/li[3]/div/ul/li[3]').click()  ## 시설 - 테니스장
        driver.find_element(By.XPATH, '//*[@id="search"]/div/ul/li[4]/div/*[@id="place"]/li[2]').click()  ## 장소 - 2코트
        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/section/div/article/div[5]/ul/li[1]/div[1]/p/span[2]').click() ## 달력 다음달로 넘기기

        try :
            driver.find_element(By.XPATH, '//*[@id="date-' + str(config.DATE) +'"]/dl').click()
        except :
            driver.refresh()
            driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/section/div/article/div[1]/form/div/ul/li[3]/div/ul/li[3]').click()
            driver.find_element(By.XPATH, '//*[@id="search"]/div/ul/li[4]/div/*[@id="place"]/li[2]').click()
            driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/section/div/article/div[5]/ul/li[1]/div[1]/p/span[2]').click()
            driver.find_element(By.XPATH, '//*[@id="date-' + str(config.DATE) +'"]/dl').click()  ## 날짜 선택

        driver.find_element(By.XPATH, '//*[@id="reservationList"]/ul/li[2]/div[2]/table/tbody/tr[4]/td/span').click() ## 4부 선택
        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/section/div/article/div[5]/div/span/a').click() ## 대관 신청

        driver.find_element(By.ID, 'users').send_keys('6') # 인원수
        driver.find_element(By.XPATH, '//*[@id="contents"]/article/form/div[10]/span').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/section/div/article/form/div[11]/span[2]/a').click()

    print('done')