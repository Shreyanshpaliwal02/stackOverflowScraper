pip install requests-html requests pandas

import requests
from requests_html import HTML
import time
import pandas as pd

baseUrl = 'https://stackoverflow.com/questions/tagged/'
tag = 'python'
queryFilter = "Votes"
url = f"{baseUrl}{tag}?tab={queryFilter}"
url

r = requests.get(url)
htmlString = r.text
html = HTML(html = htmlString) 

questionSummaries = html.find(".question-summary")

print(questionSummaries[0].text) #all the text which is inside the "div" tag

keyNames = ['question', 'votes','tags',]
classesReqd = ['.question-hyperlink', '.vote','.tags']
currQuesElement = questionSummaries[0]
currQuesElement.find('.question-hyperlink', first = True).text #first is the actual 1st element in the question-hyperlink class
currQuesElement.find('.vote', first = True).text.replace("\nvotes","")

def cleanScrape(text, keyname = None,):
    if keyname == 'votes':
        return text.replace('\nvotes','')
    return text
  
 datas = []

for queEl in questionSummaries: 
    questionData = {}
    for i, _class in enumerate(classesReqd):
        subEle = queEl.find(_class, first = True)
        keyname = keyNames[i]
        questionData[keyname] = cleanScrape(subEle.text, keyname = keyname)
    datas.append(questionData)

datas[0] 

def parse_tagged_page(html):  #search data on a specific page
    questionSummaries = html.find(".question-summary")
    keyNames = ['question', 'votes','tags',]
    classesReqd = ['.question-hyperlink', '.vote','.tags']
    datas = []
    for queEl in questionSummaries: 
        questionData = {}
        for i, _class in enumerate(classesReqd):
            subEle = queEl.find(_class, first = True)
            keyname = keyNames[i]
            questionData[keyname] = cleanScrape(subEle.text, keyname = keyname)
        datas.append(questionData)
    return datas
  
  def extract_data_from_url(url):
    r = requests.get(url)
    if r.status_code not in range(200,299):
        return []
    htmlString = r.text
    html = HTML(html = htmlString) 
    datas = parse_tagged_page(html)
    return datas
  
  def scraperFunction(tag = 'python', queryFilter = "Votes", maxPages = 10, pagesize = 5):
    baseUrl = 'https://stackoverflow.com/questions/tagged/'
    datas = []
    for p in range(maxPages):
        print(p)
        pageNum = p + 1
        url = f"{baseUrl}{tag}?tab={queryFilter}&page={pageNum}&pagesize={pagesize}"
        datas += extract_data_from_url(url)
    return datas
#now we can store this data in a framework(for eg: pandas)

datas = scraperFunction(tag = 'javascript')
len(datas)
df = pd.DataFrame(datas)
df.head()
df.to_csv("webScraping.csv", index = False) #Exporting
df.shape
