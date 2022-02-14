import requests 
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

ext_data = []
bio_data = []
page = 0

while True:
    
    page+=1
    url = (f'https://www.superprof.com/a/search/?adress=United%20States&matiere=All%20subjects&page={page}')
    response = requests.get(url)
    response_json = response.json()
    results_list = response_json['mainResults']
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36", 'accept': 'text/html; charset=utf-8'}

    for person in results_list:
        title = person['title']
        url = person['url']
        html_url = 'https://www.superprof.com'+ url
        site = requests.get(html_url, headers=headers)
        soup = BeautifulSoup(site.text, 'html.parser')
        
        # Finding all the results in professor's bio
        
        link_to_profile = soup.find_all('div', class_='AnnonceContent_Container mb20 mmb3 experience') 
        name = person['teacherName']
        school = 'harvard'
        school_final = school.lower()
        
        for professors in link_to_profile:
            professor_name = soup.find('div', {'class':'prenom'}).text
            bios = soup.find('p', {'class':'AnnonceContent_text'}).text
        
            if school_final in bios:
                bio_data.append(professor_name.capitalize())
                print(f'The professor found was: {bio_data}')

                if school_final in title:
                    ext_data.append(name.capitalize())
                    print(ext_data)
    print(page)
   
print(ext_data)
print(bio_data)

