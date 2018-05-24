#!/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

def browserSetup():
    print ("setting up browser")
    driver = webdriver.Firefox()
    return driver

def goToSite(driver,site):
    driver.get(site)
    time.sleep(0)
    
    
def enterValue(driver,string):
    time.sleep(1)
    elem = driver.find_element_by_xpath('//*[@id="lst-ib"]')
    elem.send_keys(string)
    elem.send_keys(Keys.RETURN)


def closeBrowser(driver):
    driver.close()


def main():
    site = "https://www.google.com/"
    driver = browserSetup()
    goToSite(driver,site)
    enterValue(driver,sys.argv[1])    
    
if __name__=='__main__':
    main()
