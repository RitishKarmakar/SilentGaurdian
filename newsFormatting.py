from newsextractor import GoogleNews
gn = GoogleNews()

search_res = gn.search('vote')
print(search_res)