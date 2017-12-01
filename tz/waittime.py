from selenium import webdriver
from lxml import etree
import time

def waittime(driver):
    pageSource = driver.page_source  # 取得網頁原始碼
    html = etree.HTML(pageSource)
    result = html.xpath('/html/body/div/div[1]/div[1]/div[2]/div[7]/div[3]/button/div[2]/span[2]')[0].text
    # print('剩餘時間：'+result)
    # if result=='00:00:05':
    #     wtime = time.sleep(9)
    # elif result=='00:00:04':
    #     wtime = time.sleep(8)
    # elif result=='00:00:03':
    #     wtime = time.sleep(7)
    # elif result=='00:00:02':
    #     wtime = time.sleep(6)
    # elif result=='00:00:01':
    #     wtime = time.sleep(5)
    # elif result=='00:00:00':
    #     wtime = time.sleep(4)
    # else:
    #     wtime = time.sleep(0)
    if result=='00:00:03':
        wtime = 7
    elif result=='00:00:02':
        wtime = 6
    elif result=='00:00:01':
        wtime = 5
    elif result=='00:00:00':
        wtime = 4
    else:
        wtime = 0
       
    return wtime

def count_div(a):
    c = 0
    if a != 0:
        c = 1
    return c