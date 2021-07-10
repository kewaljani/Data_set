import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
count = 0
flag = 0
data = []
sub_list = []
for filename in os.listdir(os.getcwd()+'/files'):                                  #iterate through all the files
    with open("files/"+filename,encoding='cp437') as fp:
        soup = BeautifulSoup(fp, 'html.parser') 
    sub_list.append(filename.replace('.txt',' '))
    for website in soup.find_all('meta',{'property':'og:url'}):                    #search for meta tag with attribute property=og.url for website link from source code
        website_name = website['content'].split(" ")
        sub_list.append(website_name[0])
    for status in soup.find_all('meta',{'name':'prerender-status-code'}):          #search for meta tag with attribute name = prerender-status-code  for website error
        if status['content'] == '404':
            sub_list.append('True')
        else:
            sub_list.append('')
    for i in soup.find_all('div',{'at-carousel-header':'true'}):                   #search for div tag with attribute at-carousel-header = true for to check if it still dilivers
        sub_list.append('true')
        break
    else:
        sub_list.append('')
    data.append(sub_list)
    sub_list = []
    flag = 0
    df = pd.DataFrame(data, columns = ['File name', 'URL','RestaurantMissing', 'NotAcceptingOffer'])
df.to_csv('grubhub.csv')