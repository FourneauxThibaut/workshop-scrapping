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