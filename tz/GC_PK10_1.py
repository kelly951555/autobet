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

env = input("1→內測 2→外測 3→2015 4→生產 ： ")
username = input('username：')
for k,v in pk10.items():
    print (k +' → '+v )
lotteryid = input('請輸入lotteryid：')
clist = input('輸入預設開獎號 EX:01,02,03,04,05,06,07,08,09,10：')
while len(clist.split(',')) != 10:
    clist = input('請重新輸入開獎號：')

# dxds = '1234'
def dxds(c):
    if int(c) > 5:
        dx = '1'
    else:
        dx = '2'
    if int(c)%2 != 0:
        ds = '3'
    else:
        ds = '4'
    return dx+ds

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

if driver.find_element_by_class_name("gr_user-area__user-name").is_displayed():
    print('login success')
else:
    print('login failed')

i = 1
driver.get('{}GamePlayer/'.format(domain) + lotteryid)
#需等待js完整產出原始碼
try:
    waitlottery = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div[2]/div[6]/div[5]/button[2]')))
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
    driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[7]/div[1]/div/button[2]").click()
    time.sleep(1) #需等待，否則只會抓到0秒
    time.sleep(waittime(driver))
    # 清除機選
    driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[7]/div[1]/div/button[1]").click()
    # 添加投注項
    add_order = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[6]/div[5]/button[2]")
    # 前一-------------------------------
    play1d = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[2]/ul/li[1]")
    play_n = play1d.text
    play1d.click()  
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div/div[2]/ul/li[{}]'.format(int(clist.split(',')[0]))).click()
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 前二-------------------------------
    play2d = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[2]/ul/li[2]")
    play2d.click()
    # 前二复式    
    play2d_f = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div/span[1]/span")
    play2d_f.click()
    play_n = play2d_f.text
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[1]/div[2]/ul/li[{}]'.format(int(clist.split(',')[0]))).click()
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[2]/div[2]/ul/li[{}]'.format(int(clist.split(',')[1]))).click()
    # driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[3]/div[2]/ul/li[{}]'.format(int(clist.split(',')[2]))).click()
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 前二单式
    play2d_d = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div/span[2]/span")
    play2d_d.click()
    play_n = play2d_d.text
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[2]/textarea').send_keys(clist[0:5].replace(',',' '))
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 前三-------------------------------    
    play3d = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[2]/ul/li[3]")
    play3d.click()
    # 前三复式
    play3d_f = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div/span[1]/span")
    play3d_f.click()
    play_n = play3d_f.text
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[1]/div[2]/ul/li[{}]'.format(int(clist.split(',')[0]))).click()
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[2]/div[2]/ul/li[{}]'.format(int(clist.split(',')[1]))).click()
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[3]/div[2]/ul/li[{}]'.format(int(clist.split(',')[2]))).click()
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 前三单式
    play3d_d = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div/span[2]/span")
    play3d_d.click()
    play_n = play3d_d.text
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[2]/textarea').send_keys(clist[0:8].replace(',',' '))
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 定位胆------------------------------
    playdwd = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[2]/ul/li[4]")
    playdwd.click()
    # 冠军~第5名    
    playdwd_1to5 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div/span[1]/span")
    playdwd_1to5.click()
    play_n = playdwd.text + playdwd_1to5.text
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[1]/div[2]/ul/li[{}]'.format(int(clist.split(',')[0]))).click()
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[2]/div[2]/ul/li[{}]'.format(int(clist.split(',')[1]))).click()
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[3]/div[2]/ul/li[{}]'.format(int(clist.split(',')[2]))).click()
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[4]/div[2]/ul/li[{}]'.format(int(clist.split(',')[3]))).click()
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[5]/div[2]/ul/li[{}]'.format(int(clist.split(',')[4]))).click()
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 第6~10名
    playdwd_6to10 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[3]/div/span[2]/span")
    playdwd_6to10.click()
    play_n = playdwd.text + playdwd_6to10.text
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[1]/div[2]/ul/li[{}]'.format(int(clist.split(',')[5]))).click()
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[2]/div[2]/ul/li[{}]'.format(int(clist.split(',')[6]))).click()
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[3]/div[2]/ul/li[{}]'.format(int(clist.split(',')[7]))).click()
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[4]/div[2]/ul/li[{}]'.format(int(clist.split(',')[8]))).click()
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[5]/div[2]/ul/li[{}]'.format(int(clist.split(',')[9]))).click()
    add_order.click()
    time.sleep(waittime(driver))
    # send_project(play_n)
    # 大小單雙-------------------------------    
    playdxds = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[2]/ul/li[5]")
    playdxds.click()
    play_n = playdxds.text
    i = 1
    for c in clist.split(','):
        dd = dxds(c)
        driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[{}]/div[2]/ul/li[{}]'.format(i,int(dd[0]))).click()
        driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[5]/div/div[{}]/div[2]/ul/li[{}]'.format(i,int(dd[1]))).click()
        i+=1
    add_order.click()
    time.sleep(waittime(driver))
    send_project(play_n)
    tEnd = time.time()
    print(lottery+" 投注時間花費 %f sec" % (tEnd - tStart)) 
except:
    print ('page notfound')          
    # i = i+1   