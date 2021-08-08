# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 18:40:16 2021

@author: Piuli
"""

import scrapy



class RankingsSpider(scrapy.spider):
    name = 'rankings'

    def start_requests(self):
        urls = ['https://maplestory.nexon.net/rankings/job-ranking/shade/shade?rebootIndex=0']
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        
        