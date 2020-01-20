import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.simplyrecipes.com/recipes/pressure_cooker_chicken_and_rice_casserole/")

webpage = page.content

soup = BeautifulSoup(webpage, "html.parser")

#print(soup)

ingredient_list = soup.find_all("div", class_="entry-details recipe-ingredients")
       
print(ingredient_list[-1])

actual_ingredient_list = ingredient_list[-1].find_all("ul")

print(actual_ingredient_list)
