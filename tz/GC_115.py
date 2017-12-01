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
n115 = {'30秒11选5':'57' , '1分11选5':'54' , '2分11选5':'20' , '5分11选5':'63' ,  '山东11选5':'5' , '江西11选5':'7' , '广东11选5':'8'}
domain = env_choose(env)
url = url(domain)+username

SaveDirectory = os.getcwd();#印出目前工作目錄
chromedriver = SaveDirectory+"\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.maximize_window() # 瀏覽器設定全螢幕
driver.get(url)
now_handle = driver.current_window_handle
clist = '01,02,03,04,05'
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
            waitlottery = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')))
            driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/button[1]").click()
        except:
            driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/button[1]").click()
        print(play_n+' success'.encode("utf8").decode("cp950", "ignore"))
        time.sleep(1)
    except:        
        print(play_n+' failed'.encode("utf8").decode("cp950", "ignore"))
        driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/button[1]").click()
        time.sleep(1)

driver.get('http://gameclient.100scrop.tech/GamePlayer/63')
try:
    waitlottery = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[6]/div[5]/button[2]')))
    print('enter success')    
    # print(driver.find_element_by_xpath("/html/body/div/div/div[2]/div[3]/div/span[1]/span").text)
    try:
        if driver.find_element_by_xpath("/html/body/div[2]/div/div[1]").is_displayed():
            time.sleep(3)
        else:
            pass
    except:
        pass
    tStart = time.time()
    # 機選抓時間，防止換獎期中斷
    ran = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[7]/div[1]/div/button[2]")
    ran.click()
    # print(ran.text)
    time.sleep(1) #需等待，否則只會抓到0秒
    time.sleep(waittime(driver))
    # 清除機選
    clr = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[7]/div[1]/div/button[1]")
    clr.click()
    # print(clr.text)
    # 添加投注項
    add_order = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[6]/div[5]/button[2]")
    # print(add_order.text)
    # 前三-------------------------------
    play3d = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/ul/li[1]")
    play3d.click()
    # 直选复式
    play3d_zs = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div/span[1]/span")
    play3d_zs.click()
    play_n = play3d.text + play3d_zs.text      
    for j in range(1,4):
        for c in clist.split(' '):
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[{}]/div[2]/ul/li[{}]'.format(j,int(c))).click()
    add_order.click()
    time.sleep(waittime(driver))
    send_project(play_n)
    # 组选复式
    play3d_js = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div/span[3]")
    play3d_js.click()
    play_n = play3d.text + play3d_js.text
    for c in clist.split(' '):
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div/div[2]/ul/li[{}]'.format(int(c))).click()
    add_order.click()
    time.sleep(waittime(driver))
    send_project(play_n)
    # 前二-------------------------------
    play2d = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/ul/li[2]")
    play2d.click()
    # 直选复式
    play2d_zs = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div/span[1]/span")
    play2d_zs.click()
    play_n = play2d.text + play2d_zs.text      
    for j in range(1,3):
        for c in clist.split(' '):
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[{}]/div[2]/ul/li[{}]'.format(j,int(c))).click()
    add_order.click()
    time.sleep(waittime(driver))
    send_project(play_n)
    # 组选复式
    play2d_js = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div/span[3]/span")
    play2d_js.click()
    play_n = play2d.text + play2d_js.text
    for c in clist.split(' '):
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div/div[2]/ul/li[{}]'.format(int(c))).click()
    add_order.click()
    time.sleep(waittime(driver))
    send_project(play_n)
    # 不定位-------------------------------
    playbdw = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/ul/li[3]")
    playbdw.click()
    play_n = playbdw.text
    for c in clist.split(' '):
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div/div[2]/ul/li[{}]'.format(int(c))).click()
    add_order.click()
    time.sleep(waittime(driver))
    send_project(play_n)
    tEnd = time.time()
    print("投注時間花費 %f sec" % (tEnd - tStart)) 
    
except:
    print ('page notfound')  