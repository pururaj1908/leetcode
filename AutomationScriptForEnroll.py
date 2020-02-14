# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:44:55 2019

@author: Puru
"""

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = Chrome("F:\chromedriver.exe")
driver.implicitly_wait(20)
driver.maximize_window()

while(True):
    driver.get("https://mypack.ncsu.edu/")
    
    student_button = driver.find_element_by_xpath("//div[@title='NCSU Faculty/Staff/Students']/a")
    student_button.click()
    
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    
    username.send_keys("pdave2")
    password.send_keys("Nov@2018pjd")
    
    driver.find_element_by_id("formSubmit").click()
    
    
    menu = WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='PTNUI_LAND_WRK_GROUPBOX14$PIMG']")))
    menu.click()
    
    student_page = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "PTNUI_SELLP_DVW_PTNUI_LP_NAME$1")))#driver.find_element_by_id("PTNUI_SELLP_DVW_PTNUI_LP_NAME$1")
    student_page.click()
    
    enrollment_tab = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "win0divPTNUI_LAND_REC_GROUPLET$10")))#driver.find_element_by_id("win0divPTNUI_LAND_REC_GROUPLET$10")
    enrollment_tab.click()
    
    
    time.sleep(10)
    enrollment_wizard = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@class='ps_box-group psc_layout']/section[1]/ul[1]/li[2]")))
    time.sleep(10)

    
    while(True):
        try:
            enrollment_wizard.click()
            time.sleep(2)
            driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
            
            cart_details = WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//li[@id='myShoppingCartTab']/a[1]")))
            cart_details.click()
            
            enroll_btn = WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.ID, "enrollButton")))
            enroll_btn.click()
                
            confirm_btn = WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='ui-dialog-buttonset']/button[1]")))
            confirm_btn.send_keys(Keys.ENTER)
            
            driver.switch_to.default_content()
            time.sleep(5)
        except:
            driver.switch_to.default_content()
            time.sleep(5)
            continue
        
    menu_tile = WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.ID, "PT_ACTION_MENU$PIMG")))
    menu_tile.click()
    
    logout_btn = WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.ID, "PT_LOGOUT_MENU")))
    logout_btn.click()
    time.sleep(5)
        
