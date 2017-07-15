import os
os.chdir('/home/aron/Downloads/NextGame/')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def init_game():
    browser = webdriver.Chrome()
    browser.get('https://next.me')

    time.sleep(3)

    fblogin = browser.find_element_by_class_name('nx-login--button')
    fblogin.click()
    return browser

def make_login(browser):
    elem = browser.find_element_by_name('email')
    elem.send_keys("aron_maciel@hotmail.com")
    elem = browser.find_element_by_name('pass')
    elem.send_keys("Aron9030face")
    elem = browser.find_element_by_name('login')
    elem.click()

def select_level(browser, level):
    link = browser.find_element_by_xpath("//ul[@class='nx-tab-nav--list']/li["+str(level)+"]")
    link.click()

def make_sequence(seq, browser):
    print "Sequence: " + str(seq)
    time.sleep(5)
    item1 = browser.find_element_by_class_name('nx-icon-grid--0')
    item2 = browser.find_element_by_class_name('nx-icon-grid--1')
    item3 = browser.find_element_by_class_name('nx-icon-grid--2')
    item4 = browser.find_element_by_class_name('nx-icon-grid--3')
    item5 = browser.find_element_by_class_name('nx-icon-grid--4')
    item6 = browser.find_element_by_class_name('nx-icon-grid--5')
    item7 = browser.find_element_by_class_name('nx-icon-grid--6')
    item8 = browser.find_element_by_class_name('nx-icon-grid--7')
    item9 = browser.find_element_by_class_name('nx-icon-grid--8')
    item10 = browser.find_element_by_class_name('nx-icon-grid--9')
    item11 = browser.find_element_by_class_name('nx-icon-grid--10')
    item12 = browser.find_element_by_class_name('nx-icon-grid--11')

    for i in seq:
        if(str(i)=="1"):
            item1.click()
        elif(str(i)=="2"):
            item2.click()
        elif(str(i)=="3"):
            item3.click()
        elif(str(i)=="4"):
            item4.click()
        elif(str(i)=="5"):
            item5.click()
        elif(str(i)=="6"):
            item6.click()
        elif(str(i)=="7"):
            item7.click()
        elif(str(i)=="8"):
            item8.click()
        elif(str(i)=="9"):
            item9.click()
        elif(str(i)=="10"):
            item10.click()
        elif(str(i)=="11"):
            item11.click()
        else:
            item12.click()

    time.sleep(3)
    confirmation = browser.find_element_by_class_name('nx-confirmation--ok-button')
    confirmation.click()
    time.sleep(3)
    exit = browser.find_element_by_class_name('nx-feedback--button')
    exit.click()

def run_sequence(seq):
    
    level = len(seq) - 3
    browser = init_game()
    time.sleep(5)

    make_login(browser)
    time.sleep(5)
    select_level(browser, level)
    time.sleep(3)
    make_sequence(seq, browser)

    browser.close()

