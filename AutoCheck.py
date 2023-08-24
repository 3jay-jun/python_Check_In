from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import configparser
import os

# 설정 파일에서 정보 가져오기
config = configparser.ConfigParser()
config.read('./conf.ini')


# Webdriver를 Chrome으로 설정 (Chrome.exe파일을 python과 동일한 파일에 넣기)
driver = webdriver.Chrome()

# 홈페이지 열기
driver.get(config['PAGE']['URL'])

# 해당 페이지에서 요소 가져오기
username = driver.find_element(By.NAME, 'EMP_NO')
password = driver.find_element(By.NAME, 'EI_PASSWORD')

# 로그인 정보 입력
username.send_keys(config['USER_INFO']['USER_ID'])
password.send_keys(config['USER_INFO']['USER_PW'])
password.send_keys(Keys.RETURN)
try:
    # 로그인 후 로딩 대기 (열리면 즉시 실행)
    driver.implicitly_wait(10)

    # 토글 버튼
    toggleBtn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li[5]/a')  # 클릭할 버튼 요소 식별자로 변경
    toggleBtn.click()

    # 토글 열리는 시간 대기 (열리면 즉시 실행)
    driver.implicitly_wait(3)

    # 스크립트 삽입 코드 : 스크립트로 checkIn 버튼 찾기
    script_jquery_injection = "document.querySelector('#attbtns > button:first-child').click()"
    driver.execute_script(script_jquery_injection)

except Exception as e:
    print('error')
    print(e)
finally:
    # 실행 확인을 위해 대기 상태로 만들었습니다. 로그를 쌓는 코드를 넣어도 좋을 듯 합니다.
    os.system('pause')
