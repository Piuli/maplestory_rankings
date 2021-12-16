# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:52:42 2021

@author: Piuli
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class Jobs():
    
    def __init__(self):
            PATH = "C:\Program Files (x86)\chromedriver.exe"
            self.driver = webdriver.Chrome(PATH)
            self.driver.maximize_window()
            
            self.url = 'https://maplestory.nexon.net/rankings/job-ranking/explorer/warrior'     # start at first job
            self.driver.get(self.url)
            
    def get_jobs(self):
        url = self.driver.page_source
        soup = BeautifulSoup(url, 'html.parser')
        
        
        
    def job_dropdown(self):
        try:
            job = self.driver.find_elements_by_class_name('c-filter-dd__current-filtered-item')[2]
            job.click()
            time.sleep(1)          
        except Exception:
            print('No category job found')
            
    
    
if __name__ == '__main__':
    j = Jobs()
    j.job_dropdown()
    
    