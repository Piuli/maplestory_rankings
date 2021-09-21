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



class RankingsSpider(scrapy.Spider):
    name = 'rankings'

    def start_requests(self):
        page_response = requests.get('https://maplestory.nexon.net/rankings/job-ranking/shade/shade?rebootIndex=0')
        url = page_response.url
        urls = [url]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        name = response.css('div.c-rank-list__table-cell-text').extract()
        rankings = response.css('h1.title').extract()
        location = response.css('div.c-filter__item.c-filter__item--north-america.active').extract()
        
        page_response = requests.get('https://maplestory.nexon.net/rankings/job-ranking/shade/shade?rebootIndex=0')
        url = page_response.url
        
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find('div', class_='c-rank-list__table-cell-text')
        print(results)
     
        yield {
            'name': name,
            'rankings': rankings,
            'url': url,
            'location': location
            }
        
class Rankings():
    
    def navigate_to_rankings(self):
        try:
            link = driver.find_element_by_link_text('Go to Main Site')
            link.click()
            time.sleep(2)
        
            # url = driver.page_source
            # soup = BeautifulSoup(url, 'html.parser')
        except Exception:
            driver.quit()
            
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
            
        try:
            rankings = driver.find_element_by_class_name('ga-community-playerrankings ')
            rankings.click()
            time.sleep(3)
        
            # url = driver.page_source
            # soup = BeautifulSoup(url, 'html.parser')  
        except Exception:
            print('Can\'t find rankings button')
            
        try: 
            both = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/main/div/div/div/div[2]/div[2]/div[3]')
            both.click()
            time.sleep(2)
        except Exception:
            print('Can\'t find both button')

        url = driver.page_source
        soup = BeautifulSoup(url, 'html.parser')  
        
        name = soup.find('div', class_='c-rank-list__table-row c-rank-list__table-row--header')[2]
        print(name)
            

if __name__ == '__main__':
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()

    # url = input('Type in the url: ')
    r = Rankings()
    
    url = 'https://maplestory.nexon.net/landing'
    driver.get(url)
    
    page = requests.get(url)       
    soup = BeautifulSoup(page.content, 'html.parser')

    r.navigate_to_rankings()
    




        