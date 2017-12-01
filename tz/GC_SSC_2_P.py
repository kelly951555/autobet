from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from time import strftime
import random
import sys
import imp
imp.reload(sys)
from waittime import waittime
from env import *
ssc = {'30sSSC':'56' , '1mSSC':'19' , '2mSSC':'18' , '5mSSC':'62' , '重慶SSC':'1'}
env = input("1→內測 2→外測 3→2015 4→生產 ： ")
username = input('username：')
for k,v in ssc.items():
    print (k +' → '+v )
lotteryid = input('請輸入lotteryid：')

domain = env_choose(env)
url = url(domain)+username

SaveDirectory = os.getcwd() #印出目前工作目錄
chromedriver = SaveDirectory+"\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.maximize_window() # 瀏覽器設定全螢幕
driver.get(url)
now_handle = driver.current_window_handle

def send_project(play_n):
    # 投注配置完成----------------------------------------    
    # 確認投注
    driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[7]/div[3]/button").click()
    time.sleep(waittime(driver))
    try:
        # 送出注單
        try:
            waitlottery = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div[2]/div/div[3]/div[2]/button[1]')))
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[3]/div[2]/button[1]").click()
        except:
            driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/button[1]").click()          
        # 繼續投注
        time.sleep(waittime(driver))
        try:
            waitlottery = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[2]/div/div[3]/button[1]')))
            driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/button[1]").click()
        except:
            driver.find_element_by_xpath("/html/body/div/div[4]/div/div[3]/button[1]").click()
        print(play_n+' success'.encode("utf8").decode("cp950", "ignore"))
        time.sleep(1)
    except:        
        print(play_n+' failed'.encode("utf8").decode("cp950", "ignore"))
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/button[1]").click()
        time.sleep(1)

driver.get('{}GamePlayer/{}'.format(domain,lotteryid))
try:
    waitlottery = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div[2]/div[6]/div[5]/button[2]')))
    print('enter success')    
    try:
        if driver.find_element_by_xpath("/html/body/div[2]/div/div[1]").is_displayed():
            time.sleep(3)
        else:
            pass
    except:
        pass
    tStart = time.time()
    # 機選抓時間，防止換獎期中斷
    ran = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[7]/div[1]/div/button[2]")
    ran.click()
    time.sleep(1) #需等待，否則只會抓到0秒
    time.sleep(waittime(driver))
    # 清除機選
    clr = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[7]/div[1]/div/button[1]")
    clr.click()
    # 添加投注項
    add_order = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[6]/div[5]/button[2]")
    # 两面盘-------------------------------
    play3d = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[2]/ul/li[12]")
    play3d.click()
    # 一字
    play3d_1 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div/span[1]/span")
    play3d_1.click()
    play_n = play3d.text + play3d_1.text      
    for j in range(1,6):
        for c in range(1,7):
            driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[{}]/div[2]/ul/li[{}]'.format(j,c)).click()
    
    for c in range(1,5):
        driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[6]/div[2]/ul/li[{}]'.format(c)).click()
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 二字
    play3d_2 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div/span[2]")
    play3d_2.click()
    play_n = play3d.text + play3d_2.text      
    for n in range(1,20,2):
        for c in range(1,3):
            driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[{}]/div[2]/ul/li[{}]'.format(n,c)).click()
    for n in range(2,21,2):
        for c in range(1,5):
            driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[{}]/div[2]/ul/li[{}]'.format(n,c)).click()
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 三字
    play3d_3 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div/span[3]/span")
    play3d_3.click()
    play_n = play3d.text + play3d_3.text      
    for n in range(1,7):
        for c in range(1,5):
            driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div[1]/div[{}]/div[2]/ul/li[{}]'.format(n,c)).click()
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 龙虎和
    play3d_tg = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div/span[4]/span")
    play3d_tg.click()
    play_n = play3d.text + play3d_tg.text      
    for n in range(1,11):
        for c in range(1,4):
            driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[{}]/div[2]/ul/li[{}]'.format(n,c)).click()
    add_order.click()
    time.sleep(waittime(driver))
    send_project(play_n)

    tEnd = time.time()
    print("投注時間花費 %f sec" % (tEnd - tStart)) 
    
except:
    pass  