# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 18:40:16 2021

@author: Piuli
"""

import scrapy
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

        
class Rankings():
    
    def main_site(self):  
        try:
            link = driver.find_element_by_link_text('Go to Main Site')
            link.click()
            time.sleep(2)
        except Exception:
            driver.quit()
    
    def hover_community(self):
        try:
            community_hover = driver.find_element_by_xpath('/html/body/header/div[1]/nav/ul[1]/li[4]')
            hover = ActionChains(driver).move_to_element(community_hover)
            hover.perform()
            # community_menu = Select(community)
            # community_menu.select_by_index(2)
            
            time.sleep(2)
        
            # url = driver.page_source
            # soup = BeautifulSoup(url, 'html.parser')
        except Exception:
            print("Can't find button\n")
    
    def click_rankings(self):
        try:
            rankings = driver.find_element_by_class_name('ga-community-playerrankings ')
            rankings.click()
            time.sleep(2) 
        except Exception:
            print('Can\'t find rankings button')
                 
    def click_non_reboot(self):
        try: 
            non_reboot = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/main/div/div/div/div[2]/div[2]/div[2]')
            non_reboot.click()
            time.sleep(1)
        except Exception:
            print('Can\'t find non-reboot button')

    def change_ranking_type(self):
        try:
            rank_type = driver.find_elements_by_class_name('c-filter-dd__current-filtered-item ')[0]
            rank_type.click()
            time.sleep(1)
        except Exception:
            print('No rank type found')
            
    def click_job(self):
        try:
            job = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/main/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[5]')  # fix xpath
            job.click()
            time.sleep(1)          
        except Exception:
            print('No category job found')
            
    def click_class_type(self):
        try:
            class_menu = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/main/div/div/div/div[2]/div[1]/div[1]/div/div[1]')  
            class_menu.click()
            time.sleep(1)
        except Exception:
            print('No class dropdown found')
            
    def click_shade(self):
        try:
            shade = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/main/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[17]')
            shade.click()
            time.sleep(1)
        except Exception:
            print('Shade option not found')
            
    def get_ign(self):
        url = driver.page_source
        soup = BeautifulSoup(url, 'html.parser')
        
        while True:
            for ign in soup.find_all('div', class_='c-rank-list__table-row')[1:6]:
                name = ign.find_all('div', class_='c-rank-list__table-cell-text')[2].text
                level = ign.find_all('div', class_='c-rank-list__table-cell-text')[5].text[0]
                print(name + ' ' + level)
            try:
                link = driver.find_element_by_class_name('c-rank-list__arrow.c-rank-list__arrow--right ')
                link.click()
                time.sleep(2)
                    
                url = driver.page_source
                soup = BeautifulSoup(url, 'html.parser')
            except Exception:
                break
                 
            
class RankingsSpider(scrapy.Spider):
    name = 'rankings'

    r = Rankings()

    def start_requests(self):
        r.main_site()
        r.hover_community()
        r.click_rankings()
        r.change_ranking_type()
        r.click_job()
        r.click_class_type()
        r.click_shade()
        r.click_non_reboot()
        
        urls = [driver.page_source]
 
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        name = response.css('div.c-rank-list__table-cell-text').extract()
        rankings = response.css('h1.title').extract()
        location = response.css('div.c-filter__item.c-filter__item--north-america.active').extract()
        
        page_response = requests.get('https://maplestory.nexon.net/rankings/job-ranking/shade/shade?rebootIndex=0')
        url = page_response.url
        
     
        yield {
            'name': name,
            'rankings': rankings,
            'url': url,
            'location': location
            }            

if __name__ == '__main__':
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()

    url = 'https://maplestory.nexon.net/landing'
    driver.get(url)
    
    # page = requests.get(url)       
    # soup = BeautifulSoup(page.content, 'html.parser')

    r = Rankings()
    r.main_site()
    r.hover_community()
    r.click_rankings()
    r.change_ranking_type()
    r.click_job()
    r.click_class_type()
    r.click_shade()
    r.click_non_reboot()
    r.get_ign()




        