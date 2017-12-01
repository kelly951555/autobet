from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import random
import sys
import imp
imp.reload(sys)
from waittime import waittime
from env import *
# lotteryid
pk10 = {'北京PK10':'106' , '30秒PK10':'111', '1分PK10':'107', '2分PK10':'112', '5分PK10':'113'}

def get_keys(d, value):
    return [k for k,v in d.items() if v == value]

def send_project(play_n):
    #投注配置完成----------------------------------------    
    # 確認投注
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[7]/div[3]/button").click()
    time.sleep(waittime(driver))
    try:
        # 送出注單
        try:
            waitlottery = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/button[1]')))
            driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[2]/button[1]").click()
        except:
            driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/button[1]").click()          
        # 繼續投注
        time.sleep(waittime(driver))
        try:
            waitlottery = WebDriverWait(driver, 1.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')))
            driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/button[1]").click()
        except:
            driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/button[1]").click()
        print(play_n+' success'.encode("utf8").decode("cp950", "ignore"))
        time.sleep(1)
    except:        
        print(play_n+' failed'.encode("utf8").decode("cp950", "ignore"))
        driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/button[1]").click()
        time.sleep(1)        

env = input("1→內測 2→外測 3→2015 4→生產 ： ")
username = input('username：')
for k,v in pk10.items():
    print (k +' → '+v )
lotteryid = input('請輸入lotteryid：')
lottery = get_keys(pk10,lotteryid)[0]

clist = input('輸入直選投注號，空格隔開 EX:01 02 03 04 05 06 07 08 09 10：')
while len(clist.split(' ')) < 3:
    clist = input('請重新輸入投注號碼：')

dxds = input('1→大 2→小 3→單 4→雙 EX:1234：')
while (len(dxds) > 4) or (len(dxds) < 1):
    dxds = input('請重新輸入大小單雙投注號碼：')

domain=env_choose(env)
url = url(domain)+username
#啟用Chrom瀏覽器登入網站------------
SaveDirectory = os.getcwd();#印出目前工作目錄
chromedriver = SaveDirectory+"\chromedriver.exe";
driver = webdriver.Chrome(chromedriver);
driver.maximize_window() # 瀏覽器設定全螢幕
driver.get(url)
now_handle = driver.current_window_handle

if driver.find_element_by_class_name("user_name").is_displayed():
    print('login success')
else:
    print('login failed')

i = 1
driver.get('{}GamePlayer/'.format(domain) + lotteryid)
#需等待js完整產出原始碼
try:
    waitlottery = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[6]/div[5]/button[2]')))
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
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[7]/div[1]/div/button[2]").click()
    time.sleep(1) #需等待，否則只會抓到0秒
    time.sleep(waittime(driver))
    # 清除機選
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[7]/div[1]/div/button[1]").click()
    # 添加投注項
    add_order = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[6]/div[5]/button[2]")
    # 前一-------------------------------
    play_n = '前一'
    play1d = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/ul/li[1]").click()    
    for c in clist.split(' '):
        if c == '01':
            driver.find_element_by_xpath("/html/body/div/div/div[2]/div[5]/div/div/div[2]/ul/li[1]").click()
        else:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div/div[2]/ul/li[{}]'.format(int(c))).click()
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 前二-------------------------------
    play_n = '前二'
    play2d = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/ul/li[2]").click()
    for i in range(1,3):
        for c in clist.split(' '):
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[{}]/div[2]/ul/li[{}]'.format(i,int(c))).click()
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 前三-------------------------------
    play_n = '前三'
    play3d = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/ul/li[3]").click()
    for i in range(1,4):
        for c in clist.split(' '):
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[{}]/div[2]/ul/li[{}]'.format(i,int(c))).click()
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 定位胆------------------------------
    playdwd = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/ul/li[4]").click()
    # 冠军~第5名
    play_n = '1~5'
    playdwd_1to5 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div/span[1]/span").click()
    for i in range(1,6):
        for c in clist.split(' '):
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[{}]/div[2]/ul/li[{}]'.format(i,int(c))).click()
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 第6~10名
    play_n = '6~10'
    playdwd_6to10 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div/span[2]/span").click()
    for i in range(1,6):
        for c in clist.split(' '):
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[{}]/div[2]/ul/li[{}]'.format(i,int(c))).click()
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 大小單雙-------------------------------
    play_n = '大小單雙'
    playdxds = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/ul/li[5]").click()
    for i in range(1,11):
        for c in dxds:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[{}]/div[2]/ul/li[{}]'.format(i,int(c))).click()
    add_order.click()
    time.sleep(waittime(driver))
    send_project(play_n)
    tEnd = time.time()
    print(lottery+" 投注時間花費 %f sec" % (tEnd - tStart)) 
except:
    print ('page notfound')          
    # i = i+1   