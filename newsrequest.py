from requests_html import HTMLSession

url = 'https://news.google.com/search?q='

s = HTMLSession()

r = s.get(url)
for title in r.html.find('title'):
    print(title.text)