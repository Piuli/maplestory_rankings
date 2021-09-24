# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 18:40:16 2021

@author: Piuli
"""

import scrapy
import requests
from selenium import webdriver
from .Navigate import Navigate
            
class RankingsSpider(scrapy.Spider):
    name = 'rankings'

    n = Navigate()
    
    def start_requests(self):
        source = self.n.order()
        urls = [source]
 
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        # name = response.css('div.c-rank-list__table-cell-text').extract()
        name = response.xpath('/html/body/div[3]/div[2]/div[2]/div/main/div/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div[3]/div').extract()
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





        