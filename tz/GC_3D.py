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
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[7]/div[3]/button").click()
    time.sleep(waittime(driver))
    try:
        # 送出注單
        try:
            waitlottery = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/button[1]')))
            driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[2]/button[1]").click()
        except:
            try:
                waitlottery = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/button[1]')))
                driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/button[1]").click()
            except:
                driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[2]/button[1]").click()

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
# lotteryid
JS3D = {'30秒3D':'108' , '1分3D':'52' , '2分3D':'109' ,'5分3D':'110' ,'福彩3D':'11' , '体彩P3':'12'}

env = input("1→內測 2→外測 3→2015 4→生產 ： ")
username = input('username：')
for k,v in JS3D.items():
    print (k +' → '+v )
lotteryid = input('請輸入lotteryid：')
print('直選&定位膽取同組號碼；二星值選取前兩組數字')
print('組選若全選，組6會取前9位號碼')
clist = input('輸入直選投注號，一定要3組 EX:01234789,0124578,0123456789：')
while len(clist.split(',')) < 3:
    clist = input('請重新輸入投注號碼：')
z3list = input('輸入組選投注號 EX:0123456789：')
while (len(z3list) > 10) or (len(z3list) < 3):
    z3list = input('請重新輸入組選投注號碼：')
# 組六不可多餘9位數，取組選前9位數
if len(z3list) > 9:
    z6list = z3list[:8]
else:
    z6list = z3list

domain = env_choose(env)
url = url(domain)+username
#啟用Chrom瀏覽器登入網站------------
SaveDirectory = os.getcwd();#印出目前工作目錄
chromedriver = SaveDirectory+"\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

driver.maximize_window() # 瀏覽器設定全螢幕
driver.get(url)
now_handle = driver.current_window_handle

if driver.find_element_by_class_name("user_name").is_displayed():
    print('login success')
else:
    print('login failed')
driver.get('{}GamePlayer/'.format(domain) + lotteryid)
lottery = get_keys(JS3D,lotteryid)[0]
#需等待js完整產出原始碼
try:
    waitlottery = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[6]/div[5]/button[2]')))
    print(lottery + ' enter success')
    tStart = time.time()
    # 機選抓時間，防止換獎期中斷
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[7]/div[1]/div/button[2]").click()
    time.sleep(1) #需等待，否則只會抓到0秒
    time.sleep(waittime(driver))
    # 清除機選
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[7]/div[1]/div/button[1]").click()
    # 添加投注項
    add_order = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[6]/div[5]/button[2]")
    # 三星-------------------------------
    play3d = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/ul/li[1]").click()
    # 三星直選
    play_n = '三星直選'
    play3d_zs = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[1]/span[1]/span").click()
    for c in clist.split(',')[0]:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[1]/div[2]/ul/li[{}]'.format(int(c)+1)).click() # str要轉int才能取值
    for c1 in clist.split(',')[1]:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[2]/div[2]/ul/li[{}]'.format(int(c1)+1)).click()
    for c2 in clist.split(',')[2]:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[3]/div[2]/ul/li[{}]'.format(int(c2)+1)).click()
    add_order.click()
    time.sleep(waittime(driver))
    send_project(play_n)
    # 組三
    play_n = '組3'
    play3d_z3 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[2]/span[1]/span").click()
    for c in z3list:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div/div[2]/ul/li[{}]'.format(int(c)+1)).click() # str要轉int才能取值
    add_order.click()
    time.sleep(waittime(driver))
    send_project(play_n)
    # 組6
    play_n = '組6'
    play3d_z6 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[2]/span[2]/span").click()
    for c in z6list:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div/div[2]/ul/li[{}]'.format(int(c)+1)).click() # str要轉int才能取值
    add_order.click()
    time.sleep(waittime(driver))
    send_project(play_n)
    # 二星-------------------------------
    play2d = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/ul/li[2]").click()
    # 前二直选
    play_n = '前二直選'
    play2d_cz2 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div/span[1]/span").click()
    for c in clist.split(',')[0]:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[1]/div[2]/ul/li[{}]'.format(int(c)+1)).click() # str要轉int才能取值
    for c1 in clist.split(',')[1]:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[2]/div[2]/ul/li[{}]'.format(int(c1)+1)).click()
    add_order.click()
    time.sleep(waittime(driver))
    send_project(play_n)
    # 后二直选
    play_n = '後二直選'
    play2d_hz2 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[3]/div/span[3]").click()
    for c in clist.split(',')[0]:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[1]/div[2]/ul/li[{}]'.format(int(c)+1)).click() # str要轉int才能取值
    for c1 in clist.split(',')[1]:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[2]/div[2]/ul/li[{}]'.format(int(c1)+1)).click()
    add_order.click()
    time.sleep(waittime(driver))
    send_project(play_n)
    # 前二组选
    play_n = '前二組選'
    play2d_cj2 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div/span[5]/span").click()
    for c in z3list:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div/div[2]/ul/li[{}]'.format(int(c)+1)).click() # str要轉int才能取值
    add_order.click()
    time.sleep(waittime(driver))
    send_project(play_n)
    # 后二组选
    play_n = '後二組選'
    play2d_hj2 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div/span[7]/span").click()
    for c in z3list:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div/div[2]/ul/li[{}]'.format(int(c)+1)).click() # str要轉int才能取值
    add_order.click()
    time.sleep(waittime(driver))
    send_project(play_n)
    # 定位胆
    play_n = '定位膽'
    play3d_dwd = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/ul/li[3]").click()
    for c in clist.split(',')[0]:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[1]/div[2]/ul/li[{}]'.format(int(c)+1)).click() # str要轉int才能取值
    for c1 in clist.split(',')[1]:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[2]/div[2]/ul/li[{}]'.format(int(c1)+1)).click()
    for c2 in clist.split(',')[2]:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[3]/div[2]/ul/li[{}]'.format(int(c2)+1)).click()
    add_order.click()
    time.sleep(waittime(driver))
    send_project(play_n)
    # 不定位
    play_n = '不定位'
    play2d_bdw = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/ul/li[4]").click()
    for c in z3list:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div/div[2]/ul/li[{}]'.format(int(c)+1)).click() # str要轉int才能取值
    add_order.click()    
    time.sleep(waittime(driver))
    send_project(play_n)
    # 投注配置完成----------------------------------------
    tEnd = time.time()
    print(lottery+" 投注時間花費 %f sec" % (tEnd - tStart))
except:
    print (lottery + ' page notfound')
    pass