# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 14:32:01 2018

@author: Philipp
"""

import bs4, time
from selenium import webdriver
import pandas as pd

def extract_html(url):
    browser = webdriver.Firefox()
    browser.get(url)
    time.sleep(5)
    source = browser.execute_script('return document.documentElement.outerHTML')
    browser.quit()
    return source

def extract_table(html):
    soup = bs4.BeautifulSoup(html, "lxml")
    table = soup.find('table')
    rows = table.find_all('tr', attrs=['even desktop', 'odd desktop'])  #Find all desktop table rows
    str_table= r'<table>'+ str(rows) + r'</table>'   #Make string which pandas can read
    df = pd.read_html(str_table)[0]
    lTeam = df.iloc[:,:5]   # Split table
    rTeam = df.iloc[:,6:]
    rTeam = rTeam[rTeam.columns[::-1]] # rearrange table
    rTeam.columns = [0,1,2,3,4] # Relable rTeams columns
    return lTeam, rTeam

def extract_data(url):
    source = extract_html(url)
    lTeam, rTeam = extract_table(source)
    return lTeam, rTeam