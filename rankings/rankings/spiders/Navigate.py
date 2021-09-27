# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 01:26:20 2021

@author: Piuli
"""
import scrapy
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

class Navigate():
    
    def __init__(self):
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)
        self.driver.maximize_window()

        self.url = 'https://maplestory.nexon.net/landing'
        self.driver.get(self.url)

    def main_site(self):  
        try:
            link = self.driver.find_element_by_link_text('Go to Main Site')
            link.click()
            time.sleep(2)
        except Exception:
            self.driver.quit()
    
    def hover_community(self):
        try:
            community_hover = self.driver.find_element_by_class_name('ga-community ')
            hover = ActionChains(self.driver).move_to_element(community_hover)
            hover.perform()
            time.sleep(2)
        except Exception:
            print("Can't find button\n")
    
    def click_player_rankings(self):
        try:
            rankings = self.driver.find_element_by_class_name('ga-community-playerrankings ')
            rankings.click()
            time.sleep(2) 
        except Exception:
            print('Can\'t find rankings button')

    def ranking_type_dropdown(self):
        try:
            rank_type = self.driver.find_elements_by_class_name('c-filter-dd__current-filtered-item ')[0]
            rank_type.click()
            time.sleep(1)
        except Exception:
            print('No rank type found')
            
    def job_dropdown(self):
        try:
            job = self.driver.find_element_by_class_name('c-filter-dd__filterable-item.c-filter-dd__filterable-item--job ')
            job.click()
            time.sleep(1)          
        except Exception:
            print('No category job found')
            
    def class_dropdown(self):
        try:
            class_menu= self.driver.find_elements_by_class_name('c-filter-dd__current-filtered-item ')[1]
            class_menu.click()
            time.sleep(1)
        except Exception:
            print('No class dropdown found')
            
    def click_shade(self):
        try:
            shade = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/main/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[17]')
            shade.click()
            time.sleep(1)
        except Exception:
            print('Shade option not found')
            
    def click_non_reboot(self):
        try: 
            non_reboot = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/main/div/div/div/div[2]/div[2]/div[2]')
            non_reboot.click()
            time.sleep(1)
        except Exception:
             print('Can\'t find non-reboot button')
    
    def get_ign(self):
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
          
    def get_page_url(self):
        source = self.driver.current_url
        return source
    
    def order(self):
        self.main_site()
        self.hover_community()
        self.click_player_rankings()
        self.ranking_type_dropdown()
        self.job_dropdown()
        self.class_dropdown()
        self.click_shade()
        self.click_non_reboot()
        self.get_ign()
        # source = self.get_page_url()
        # return source
            
   
if __name__ == '__main__':
    n = Navigate()
    n.order()
    
#     n.main_site()
#     n.hover_community()
#     n.click_rankings()
#     n.change_ranking_type()
#     n.click_job()
#     n.click_class_type()
#     n.click_shade()
#     n.click_non_reboot()
#     # n.get_ign()
#     n.get_page_url()
            
