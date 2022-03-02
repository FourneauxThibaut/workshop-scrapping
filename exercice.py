import requests                     # python pip install requests
from bs4 import BeautifulSoup       # python pip install beautifulsoup4

blog = "https://dev.to/"

#       ┌────────────────┐
#       │  page request  │
#       └────────────────┘
response = requests.get(blog)
soup = BeautifulSoup(response.text, features="html.parser")

#       ┌────────────┐
#       │  get data  │
#       └────────────┘
articles = soup.find_all("div", class_="crayons-story")

for article in articles:
    author = (article.find("a", class_="crayons-story__secondary").contents[0]).strip()
    name = (article.find("a", class_="crayons-story__hidden-navigation-link").contents[0]).strip()
    filtering_tags = article.find_all("a", class_="crayons-tag")
    tags = []
    
    for tag in filtering_tags:
        tags.append(tag.contents[1])
    
    reactions = article.find('div', class_='crayons-story__details')
    
    if len(reactions.find_all('a')) < 2 :
        like = '0'
        comment = '0'
    else:
        like = (reactions.find_all('a')[0].contents[2]).strip()
        if len(reactions.find_all('a')[1].contents) < 2 :
            comment = '0'
        else:
            comment = (reactions.find_all('a')[1].contents[2]).strip()
    
    data = {
        "author": author, 
        "name": name,
        "tags": tags,
        "reactions": {
            "like": like, 
            "comment": comment,
        },
    }
    
    print(data)
    print('\n')
    