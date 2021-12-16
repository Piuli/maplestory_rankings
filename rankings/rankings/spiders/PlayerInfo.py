# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 21:31:05 2021

@author: Piuli
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
import time
import csv

class PlayerInfo():
    
        def __init__(self, player_class, job):
            self.player_class = player_class
            self.job = job
            
            PATH = "C:\Program Files (x86)\chromedriver.exe"
            self.driver = webdriver.Chrome(PATH)
            # self.driver.maximize_window()
    
            self.url = 'https://maplestory.nexon.net/rankings/job-ranking/' + self.player_class + '/' + self.job + '?rebootIndex=2'
            self.driver.get(self.url)
            
        def get_player_info(self):
            url = self.driver.page_source
            soup = BeautifulSoup(url, 'html.parser')
            
            top_rank = 0
            while True:
                for ign in soup.find_all('div', class_='c-rank-list__table-row')[1:6]:
                    # ign
                    name = ign.find_all('div', class_='c-rank-list__table-cell-text')[2].text.strip()
                    
                    # job
                    # job = ign.find_all('div', title=True, class_='c-rank-list__table-cell-text')
                    
                    # world
                    div_tag = ign.find_all('div', class_='c-rank-list__table-cell-text')[3]
                    a_tag = div_tag.find('a')
                    world = a_tag['class'][1]
                    
                    # level
                    level = ign.find_all('div', class_='c-rank-list__table-cell-text')[5].contents[0].strip()
                
                    # rank
                    top_rank = top_rank + 1
                    
                    if (top_rank <= 3):
                        rank = top_rank
                    else:
                        rank = ign.find_all('div', class_='c-rank-list__table-cell-text')[0].text.strip()        
                    
                    print(str(rank) + ' ' + name + ' ' + world + ' ' + level)
                     
                    csv_writer.writerow([rank, name, world, level])
                    
                try:
                    link = self.driver.find_element_by_class_name('c-rank-list__arrow.c-rank-list__arrow--right ')
                    link.click()
                    time.sleep(10)
                        
                    url = self.driver.page_source
                    soup = BeautifulSoup(url, 'html.parser')
                    
                except Exception:
                    break
                
                
if __name__ == '__main__':
    player_class = 'mihile'
    job = 'mihile'
    
    print(datetime.now())
    
    p = PlayerInfo(player_class, job)
    
    csv_file = open(player_class + '_' + job + '_' + datetime.today().strftime('%Y%m%d') + '.csv', 'w', newline='')  
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['rank', 'character', 'world', 'level'])
    
    p.get_player_info()
    
    csv_file.close()
    
    print(datetime.now())