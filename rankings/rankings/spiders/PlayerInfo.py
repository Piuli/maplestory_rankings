# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 21:31:05 2021

@author: Piuli
"""

import scrapy
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


class PlayerInfo():
    
        def __init__(self):
            PATH = "C:\Program Files (x86)\chromedriver.exe"
            self.driver = webdriver.Chrome(PATH)
            self.driver.maximize_window()
    
            self.url = 'https://maplestory.nexon.net/rankings/job-ranking/shade/shade?rebootIndex=2'
            self.driver.get(self.url)
            
        def get_player_info(self):
            url = self.driver.page_source
            soup = BeautifulSoup(url, 'html.parser')
          
            while True:
                for ign in soup.find_all('div', class_='c-rank-list__table-row')[1:6]:
                    name = ign.find_all('div', class_='c-rank-list__table-cell-text')[2].text
                    level = ign.find_all('div', class_='c-rank-list__table-cell-text')[5].text[0]
                    print(name + ' ' + level)
                try:
                    link = self.driver.find_element_by_class_name('c-rank-list__arrow.c-rank-list__arrow--right ')
                    link.click()
                    time.sleep(2)
                        
                    url = self.driver.page_source
                    soup = BeautifulSoup(url, 'html.parser')
                except Exception:
                    break
                
if __name__ == '__main__':
    p = PlayerInfo()
    p.get_player_info()