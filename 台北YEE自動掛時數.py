import pyautogui as pu
import random
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver
from chrome_helper import check_browser_driver_available

scheduler = BlockingScheduler(timezone="Asia/Taipei")
check_browser_driver_available()
path = 'config.txt'
txt = []
with open(path,"r",encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        s = line.split(' ')
        txt.append(s[0])
id = txt[0]
email2 = txt[1]
password2 = txt[2]
n = random.randint(3,5)
def job1():
     driver = webdriver.Chrome()
     time.sleep(1+n)
     driver.close
     time.sleep(1+n)
     url = 'https://elearning.taipei/'
     driver.get(url)
     time.sleep(1+n)
     for i in range(6):
      pu.press('Tab')
     pu.press('Enter')
     time.sleep(3+n)
     driver.find_element('xpath', '/html/body/main/div[1]/div[2]/div[1]/a').click()                     
     time.sleep(3+n)
     email = driver.find_element('id', "account")
     password = driver.find_element('xpath', '//*[@id="pass"]')
     time.sleep(1+n)
     email.send_keys(email2)
     password.send_keys(password2)
     time.sleep(1+n)
     pu.press('Enter')  
     time.sleep(5+n)
     url2= 'http://elearning.taipei/elearn/course/view.php?id=' + id
     driver.get(url2)
     time.sleep(5+n)
     driver.find_element('xpath', '//span[text()="1. 志願服務法規之認識"]').click()
     time.sleep(1740)
     for i in range(3):
      pu.press('Tab')
     pu.press('Enter')
     

job1()
time.sleep(1)
scheduler.add_job(job1, 'interval', minutes=30)
scheduler.start()
