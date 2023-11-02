from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests

def brown_dwarfs(page_url):

    page = requests.get(page_url)
    print(page)
    soup = BeautifulSoup(page.text, "html.parser")
    temp_list = []
    page_table = soup.find_all("table", {"class": "wikitable sortable"})
    #print("page_table:", page_table)
    
    for tr in page_table[2].find_all("tr"):
        td = tr.find_all("td")
        row = [i.text.rstrip() for i in td]
        temp_list.append(row)
    print(temp_list)

    name = []
    radius = []
    mass = []
    distance = []

    brown_dwarfs_data = []

    for i in range(1, len(temp_list)):
        name = temp_list[i][0]
        radius = temp_list[i][8]
        mass = temp_list[i][7]
        distance = temp_list[i][5]

        required_data = [name, radius, mass, distance]
        brown_dwarfs_data.append(required_data)

    headers = ["Nome", " Raio", " Massa", " Distância da Terra"]
    print(brown_dwarfs_data)


    dataframe = pd.DataFrame(brown_dwarfs_data, columns = headers)
    dataframe.to_csv("brown_dwarfs_data.csv",  index = True, index_label = "id")






page_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
brown_dwarfs(page_url)