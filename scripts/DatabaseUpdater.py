from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import requests
import json

pastDate="June 21, 2023"
date_format = "%B %d, %Y"
pastDateObj = datetime.strptime(pastDate, date_format)

def spanish_Detect(string, word_dict):#method for detecting the post type, just see if string contains certain key words
    for word in word_dict:
        if word in string:
            return True
    return False


data=[]
substrings = ["\u2018", "\u201c", "\u201d","\u2019"]
factRating=["barely-true","false","pants-fire"]
Spanish_ID=[" in una "," in une ", " un video ", "un tuit"]

for rating in factRating:
    pages=10000+1 #just a high upperbounds
    i=1 #reset counter
    endDatereached=False
    while i<pages:
        if (endDatereached==False):
            strpageNum=str(i)
            MAIN_URL = "https://www.politifact.com/factchecks/list/?page="+strpageNum+"&ruling="+str(rating)
            #list of dictionaries, MAIN DATA SET
            print(str(rating)+ " page "+str(i) + " parsed")
            response = requests.get(MAIN_URL)
            soup = BeautifulSoup(response.content, 'html.parser') #the BS parser to read the HTML
            try:
                pageExists = soup.find('h2', class_='c-title c-title--subline').text.strip()
                if (pageExists=="No Results found"):
                    print("end of results")
                    break
            except(AttributeError, NameError): #if no element is found that determines the page is empty
                factcheck_items = soup.find_all('li', class_='o-listicle__item')

                for item in factcheck_items:
                    fakenews = item.find('div', class_='m-statement__quote').text.strip()
                    source = "https://www.politifact.com"+item.find('div', class_='m-statement__quote').find('a').get('href')
                    footer = item.find('footer', class_='m-statement__footer').contents[0].strip().replace('By ', '')
                    result = footer.split("•")#creates a list of strings to get the author and date
                    result = [item.strip() for item in result] #strips result
                    author=result[0]
                    date=result[1]
                    langTag = item.find('div', class_='m-statement__desc').text.strip()
                    if(spanish_Detect(langTag,Spanish_ID)):
                        #if spanish
                        print(langTag)
                        continue
                    ###stopping condition
                    dateobj=datetime.strptime(str(date), date_format)
                    if (dateobj<pastDateObj):
                        print("end date discovered")
                        endDatereached=True
                        break
                    else:
                        for substring in substrings:
                            fakenews = fakenews.replace(substring, "'")
                        truenews=""
                        news_Entry = { #the different elements of each data entry
                            'tag':str(langTag),
                            'rating': str(rating),
                            'Fakenews': fakenews,
                            'source': source,
                            'author':author,
                            'date': date,
                            'Truenews': truenews
                        }
                        data.append(news_Entry)#append the news entry to the list    
        else:
            break   
        i+=1
    n=1#page counter for testing purposes
for item in data:
    SUB_URL=item['source'] #to collect the correct news within each link
    response = requests.get(SUB_URL)
    soup = BeautifulSoup(response.content, 'html.parser') #the BS parser to read the HTML
    updated_TrueNews = soup.find('h2', class_='c-title c-title--subline').text.strip()
    #'''#if you want to replace the unicode apostrophes
    for substring in substrings:
        updated_TrueNews = updated_TrueNews.replace(substring, "'")
    #'''
    item['Truenews']=updated_TrueNews
    print(str(n)+"/"+str(len(data)))
    n+=1
    print(item)
print("finished")

json_data = json.dumps(data, indent=4)#write the data entries into the json folder
with open('temp.json', 'w') as file:
    file.write(json_data)




