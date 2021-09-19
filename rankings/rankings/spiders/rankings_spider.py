# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 18:40:16 2021

@author: Piuli
"""

import scrapy
import requests
from bs4 import BeautifulSoup
from selenium import webdriver



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
     
        yield {
            'name': name,
            'rankings': rankings,
            'url': url,
            'location': location
            }


    
    # driver.get('https://maplestory.nexon.net/rankings/job-ranking/shade/shade?rebootIndex=0')
    
    
    # print(response.url)

    # URL = 'https://maplestory.nexon.net/rankings/job-ranking/shade/shade?rebootIndex=0'

    # PATH = "C:\Program Files (x86)\chromedriver.exe"
    # driver = webdriver.Chrome(PATH)

    # driver.get(URL)

    # page = requests.get(URL)
    # soup = BeautifulSoup(page.content, 'html.parser') 


        