import requests
from bs4 import BeautifulSoup


page = requests.get("http://example.com")

webpage = page.content

soup = BeautifulSoup(webpage, "html.parser")

#print(soup)

ps = soup.find_all("p")

#print(ps)

for tag in ps: 
    text = tag.get_text()
    print(text)
    for char in text:
        if char == "p": 
            print(char)
            

