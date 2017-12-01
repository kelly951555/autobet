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

def get_keys(d, value):
    return [k for k,v in d.items() if v == value]

def send_project(play_n):
    #投注配置完成----------------------------------------    
    # 確認投注
    driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[7]/div[3]/button").click()
    time.sleep(waittime(driver))
    try:
        # 送出注單
        try:
            waitlottery = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[2]/div/div[3]/div[2]/button[1]')))
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[3]/div[2]/button[1]").click()
        except:
            try:
                waitlottery = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[2]/div/div[3]/div[2]/button[1]')))
                driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[3]/div[2]/button[1]").click()
            except:
                driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[2]/button[1]").click()

        # 繼續投注
        time.sleep(waittime(driver))
        try:
            waitlottery = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[3]/button[1]')))
            driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/button[1]").click()
        except:
            driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/button[1]").click()
        print(play_n+' success'.encode("utf8").decode("cp950", "ignore"))
        time.sleep(1)
    except:        
        print(play_n+' failed'.encode("utf8").decode("cp950", "ignore"))
        driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/button[1]").click()
        time.sleep(1)
# lotteryid
JS3D = {'30秒3D':'108' , '1分3D':'52' , '2分3D':'109' ,'5分3D':'110' ,'福彩3D':'11' , '体彩P3':'12'}

env = input("1→內測 2→外測 3→2015 4→生產 ： ")
username = input('username：')
for k,v in JS3D.items():
    print (k +' → '+v )
lotteryid = input('請輸入lotteryid：')

clist = input('輸入預設開獎號 EX:012：')
while len(clist) != 3:
    clist = input('請重新輸入開獎號：')

domain=env_choose(env)
url = url(domain)+username

#啟用Chrom瀏覽器登入網站------------
SaveDirectory = os.getcwd();#印出目前工作目錄
chromedriver = SaveDirectory+"\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

driver.maximize_window() # 瀏覽器設定全螢幕
driver.get(url)
now_handle = driver.current_window_handle

if driver.find_element_by_class_name("gr_user-area__user-name").is_displayed():
    print('login success')
else:
    print('login failed')
driver.get('{}GamePlayer/'.format(domain) + lotteryid)
lottery = get_keys(JS3D,lotteryid)[0]
#需等待js完整產出原始碼
try:
    waitlottery = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div[2]/div[6]/div[5]/button[2]')))
    print(lottery + ' enter success')
    tStart = time.time()
    # 機選抓時間，防止換獎期中斷
    driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[7]/div[1]/div/button[2]").click()
    time.sleep(1) #需等待，否則只會抓到0秒
    time.sleep(waittime(driver))
    # 清除機選
    driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[7]/div[1]/div/button[1]").click()
    # 添加投注項
    add_order = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[6]/div[5]/button[2]")
    # 分
    driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[6]/div[3]/label[3]/span").click()
    # 三星-------------------------------
    play3d = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[2]/ul/li[1]")
    play3d.click()
    # 三星直選
    play3d_zs = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div[1]/span[1]")
    play3d_zs.click()
    play_n = play3d.text + play3d_zs.text
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[1]/div[2]/ul/li[{}]'.format(int(clist[0])+1)).click() # str要轉int才能取值
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[2]/div[2]/ul/li[{}]'.format(int(clist[1])+1)).click()
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[3]/div[2]/ul/li[{}]'.format(int(clist[2])+1)).click()
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 直选单式
    play3d_zs_d = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div[1]/span[2]/span")
    play3d_zs_d.click()
    play_n = play3d.text + play3d_zs_d.text
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[2]/textarea').send_keys(clist)
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 組三
    play3d_z3 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div[2]/span[1]")
    play3d_z3.click()
    play_n = play3d.text + play3d_z3.text
    for c in clist:
        driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div/div[2]/ul/li[{}]'.format(int(c)+1)).click() # str要轉int才能取值
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 組6
    play3d_z6 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div[2]/span[2]")
    play3d_z6.click()
    play_n = play3d.text + play3d_z6.text
    for c in clist:
        driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div/div[2]/ul/li[{}]'.format(int(c)+1)).click() # str要轉int才能取值
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 二星-------------------------------
    play2d = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[2]/ul/li[2]")
    play2d.click()
    # 前二直选    
    play2d_cz2 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div/span[1]")
    play2d_cz2.click()
    play_n = play2d_cz2.text
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[1]/div[2]/ul/li[{}]'.format(int(clist[0])+1)).click() # str要轉int才能取值
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[2]/div[2]/ul/li[{}]'.format(int(clist[1])+1)).click()
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 前二直选单式
    play2d_cz2_d = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div/span[2]")
    play2d_cz2_d.click()
    play_n = play2d_cz2_d.text
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[2]/textarea').send_keys(clist[0:2])
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 后二直选    
    play2d_hz2 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div/span[3]/span")
    play2d_hz2.click()
    play_n = play2d_hz2.text
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[1]/div[2]/ul/li[{}]'.format(int(clist[1])+1)).click() # str要轉int才能取值
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[2]/div[2]/ul/li[{}]'.format(int(clist[2])+1)).click()
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 后二直选单式
    play2d_hz2_d = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div/span[4]/span")
    play2d_hz2_d.click()
    play_n = play2d_hz2_d.text
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[2]/textarea').send_keys(clist[1:3])
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 前二组选
    play2d_cj2 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div/span[5]/span")
    play2d_cj2.click()
    play_n = play2d_cj2.text
    for c in clist[0:2]:
        driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div/div[2]/ul/li[{}]'.format(int(c)+1)).click() # str要轉int才能取值
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 前二组选单式
    play2d_cj2_d = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div/span[6]/span")
    play2d_cj2_d.click()
    play_n = play2d_cj2_d.text
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[2]/textarea').send_keys(clist[0:2])
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 后二组选
    play2d_hj2 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div/span[7]/span")
    play2d_hj2.click()
    play_n = play2d_hj2.text
    for c in clist[1:3]:
        driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div/div[2]/ul/li[{}]'.format(int(c)+1)).click() # str要轉int才能取值
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 后二组选单式
    play2d_hj2_d = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div/span[8]/span")
    play2d_hj2_d.click()
    play_n = play2d_hj2_d.text
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[2]/textarea').send_keys(clist[1:3])
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 定位胆
    play3d_dwd = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[2]/ul/li[3]")
    play3d_dwd.click()
    play_n = play3d_dwd.text
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[1]/div[2]/ul/li[{}]'.format(int(clist[0])+1)).click() # str要轉int才能取值
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[2]/div[2]/ul/li[{}]'.format(int(clist[1])+1)).click()
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[3]/div[2]/ul/li[{}]'.format(int(clist[2])+1)).click()
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 不定位
    play2d_bdw = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[2]/ul/li[4]")
    play2d_bdw.click()
    play_n = play2d_bdw.text
    for c in clist:
        driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div/div[2]/ul/li[{}]'.format(int(c)+1)).click() # str要轉int才能取值
    add_order.click()    
    time.sleep(waittime(driver))
    send_project(play_n)
    # 投注配置完成----------------------------------------
    tEnd = time.time()
    print(lottery+" 投注時間花費 %f sec" % (tEnd - tStart))
except:
    print (lottery + ' page notfound')
    pass