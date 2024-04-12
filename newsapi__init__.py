from newsapi import NewsApiClient
import requests
import json
rapi = 'https://newsapi.org/v2/top-headlines?country=in&apiKey={}'.format('be8c1b00427341bbb654de6635fae2b8')
#qapi = 'https://newsapi.org/v2/top-headlines?country=in&apiKey={}'.format('pass')
local_area = 'greater noida'
category = 'crime'

req = requests.get(rapi)
print(req.content)
# newsapi = NewsApiClient('be8c1b00427341bbb654de6635fae2b8')
# print()


# top_headlines = newsapi.get_top_headlines(q=local_area,
#                                           category=category,
#                                           language='en',
#                                           country='in')


# all_articles = newsapi.get_everything(q='robery',
                                      
#                                       from_param='2024-04-04',
                                      
#                                       language='en'
#                                       )

# print(all_articles)
sources = newsapi.get_sources()