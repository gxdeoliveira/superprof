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
'''
bio_data = []

page = 0

# Parsing the HTML with Beautiful Soup

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36", 'accept': 'text/html; charset=utf-8'}
while True:

    page += 1
    print(page)
    url = f'https://www.superprof.com/s/,United-States,,,1.html?n={page}'
    site = requests.get(url, headers=headers)  
    soup = BeautifulSoup(site.text, 'html.parser')
    print(soup)
    break
    school = 'learn'
    school_final = school.lower()
    # Finding all the results in professor's bio
    link_to_profile = soup.find_all('a')
    print(f' a bio eh esta cesar: {link_to_profile}')
    for professors in profile:
        professor_name = soup.find('div', {'class':'prenom'}).text
        bios = soup.find('p', {'class':'AnnonceContent_text'}).text

        print(f' checking professor name {professor_name}')
        if school_final in bios:
            bio_data.append(name.capitalize())
            print(f'The professor found was: {professor_name}')

            if next_page is None:
               	break
print(bio_data)
      '''      
### Passos
### Utilizar o requests pra fazer uma request a url: https://www.superprof.com/a/search/?adress=United%20States&matiere=All%20subjects&page=1
### Guardar o valor currentpage
### Percorrer o array de pessoes no json
### Para cada pessoa se tiver a string "harvard" no "title" escrever ela num arquivo de texto (lowercased) 
### Para garantir, tambem acessar a pagina da pessoa pelo beautiful soup campo "url" da resposta em json
### No beautiful soup achar o paragrafo que contem a bio da pessoa
### Se o paragrafo conter harvard, escrever a pessoa no arquivo de texto e ir para a proxima
### Checar se esta na ultima pessoa do array, caso estiver incrementar o currentPage e repetir os passo
### Checar se esta na ultima pagina, caso estiver encerrar o script
