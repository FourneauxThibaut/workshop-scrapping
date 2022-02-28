# workshop-scrapping

we will start by installing our dependency:
type in the terminal
```
pip install beautifulsoup4
pip install requests
```

in the project we are going to import then:
```
from bs4 import BeautifulSoup
import requests
```

we will fetch the data from the website using requests:
```
wanted_game_name = 'name of the game'.lower()
steam = 'https://store.steampowered.com/search/?term='+wanted_game_name
```

lower() will let us use any letter capitalized as we want without error
next, we will get all article inside the page following:

```
game_found = soup.find_all("a", class_="search_result_row")
```

we have now a table of x article (in this case each article is a game page)
foreach we will get the information about the game searched
```
for game in game_found:
                name = str(game.find(class_="title").contents[0]).lower()

                if name == wanted_game_name:
                        price = game.find('div', class_="search_price").contents
                        found = True
```
dont forget to add this, at the beggining of the file
```
found = False
```

we just need to think about exception and print the right information:
```
if found != True:
                print(f'{wanted_game_name} not found, please verify the orthograph')
        else:
                if len(price) == 4:
                        price = price[3].strip()
                        print(f'{wanted_game_name} is {float(price.replace(",", ".")[:-1])} €')
                else:   
                        price = price[0].strip()
                        print(f'{wanted_game_name} is {float(price.replace(",", ".")[:-1])} €')
```

                        
at this point you should have this:
```py
from bs4 import BeautifulSoup
import requests

wanted_game_name = wanted_game_name.lower()
found = False
steam = 'https://store.steampowered.com/search/?term='+(wanted_game_name)

#       ┌────────────────┐
#       │  page request  │
#       └────────────────┘
response = requests.get(steam)
soup = BeautifulSoup(response.text, features='html.parser')

#       ┌────────────┐
#       │  get data  │
#       └────────────┘
game_found = soup.find_all("a", class_="search_result_row")

for game in game_found:
        name = str(game.find(class_="title").contents[0]).lower()

        if name == wanted_game_name:
            price = game.find('div', class_="search_price").contents
            found = True

if found != True:
        print(f'{wanted_game_name} not found, please verify the orthograph')
else:
        if len(price) == 4:
            price = price[3].strip()
            print(f'{wanted_game_name} is {float(price.replace(",", ".")[:-1])} €')
        else:   
            price = price[0].strip()
            print(f'{wanted_game_name} is {float(price.replace(",", ".")[:-1])} €')
```

we will now make this a function to loop in a list of wanted game
this is the final code

```py
from bs4 import BeautifulSoup
import requests

def get_game_price(wanted_game_name):
        wanted_game_name = wanted_game_name.lower()
        found = False
        steam = 'https://store.steampowered.com/search/?term='+(wanted_game_name)

        #       ┌────────────────┐
        #       │  page request  │
        #       └────────────────┘
        response = requests.get(steam)
        soup = BeautifulSoup(response.text, features='html.parser')

        #       ┌────────────┐
        #       │  get data  │
        #       └────────────┘
        game_found = soup.find_all("a", class_="search_result_row")

        for game in game_found:
                name = str(game.find(class_="title").contents[0]).lower()

                if name == wanted_game_name:
                        price = game.find('div', class_="search_price").contents
                        found = True

        if found != True:
                print(f'{wanted_game_name} not found, please verify the orthograph')
        else:
                if len(price) == 4:
                        price = price[3].strip()
                        print(f'{wanted_game_name} is {float(price.replace(",", ".")[:-1])} €')
                else:   
                        price = price[0].strip()
                        print(f'{wanted_game_name} is {float(price.replace(",", ".")[:-1])} €')
                        

my_game_list = ['test nul', 'Iceberg Lovecraft Tribute', 'the evil within', 'elden ring']
for game in my_game_list:
        get_game_price(game)
```
