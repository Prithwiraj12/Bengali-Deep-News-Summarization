from requests import get
from bs4 import BeautifulSoup
import re
import sys
from datetime import datetime,date
from datetime import timedelta

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

dates=[]
# Give start date and end date to crawl the summaries and articles within this period
start_date = date(2016, 3,1)
end_date = date(2017, 4, 1)
for single_date in daterange(start_date, end_date):
     dates.append(single_date.strftime("%Y-%m-%d"))
# Give file name with year and month specification for integrating it serially with other crawled date specific files
file = open("summary2016_3.txt","w",encoding="utf-8")
file2 = open("article2016_3.txt","w",encoding="utf-8")
j=0
for date in dates:
    url = 'https://bangla.bdnews24.com/archive/?date='+date
    # print (url)
    # url = ''+xxx+''
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    # print(response)
    # Taking feature names
    specs_key = html_soup.find_all('div',{"class": "article"})
    #print(specs_key)
  
    for i in specs_key:
        # print(i.a.get('href'))
        print("count "+str(j))
        #print(i.get('href'))
        int_response = get(i.a.get('href'))
        #file.write(i.a.get('href'))
        int_html_soup = BeautifulSoup(int_response.text, 'html.parser')
        summary = int_html_soup.find_all('h5', {"class": "print-only"})
        processed_text=""
        document = int_html_soup.find_all('div', {"class": "custombody print-only"})
        for t in document:
          mytext = t.find_all('p')
          for k in mytext:
            words=k.text.split()
            for wd in words :
              processed_text+=" "+wd
        if len(processed_text) < 10:
          continue
        processed_sum=""
        for sum in summary:
            mysum=sum.text.split()
            for tem in mysum :
                processed_sum+=" "+tem 
        if len(processed_sum) < 3 :
            continue
        file.write(processed_sum+"\n")
        file2.write(processed_text+"\n")
        j = j+1  
       
    print(date)
file.close()
file2.close()