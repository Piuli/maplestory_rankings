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
        urls = ['https://maplestory.nexon.net/rankings/job-ranking/shade/shade?rebootIndex=0']
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        name = response.css('div.c-rank-list__table-cell-text').extract()
        yield {
            'name': name
            }


    # URL = 'https://maplestory.nexon.net/rankings/job-ranking/shade/shade?rebootIndex=0'

    # PATH = "C:\Program Files (x86)\chromedriver.exe"
    # driver = webdriver.Chrome(PATH)

    # driver.get(URL)

    # page = requests.get(URL)
    # soup = BeautifulSoup(page.content, 'html.parser') 


        