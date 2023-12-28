from bs4 import BeautifulSoup
import requests

# link = "https://www.olx.pl/oferty/q-lego-4195/?search%5Border%5D=created_at:desc"
link = "https://www.olx.pl/oferty/q-lego-42138/?search%5Border%5D=created_at:desc"

# read previous data from txt file
file = open("file.txt", "r")
file_text = file.read()
offers_past = file_text.split("\n")
file.close()

# get current ids of offers
offers_now = []
html_text = requests.get(link).text
soup = BeautifulSoup(html_text, "lxml")

offers = soup.find("div", class_='css-oukcj3').find_all("div", class_="css-1sw7q4x")

for offer in offers:
    offer_name = offer.find("h6", class_ = "css-16v5mdi er34gjf0").text
    offer_link = offer.find("a").get("href")
    offer_link = "https://www.olx.pl" + offer_link
    offer_id = offer.get("id")
    if offer_id not in offers_past:
        print("new: " + offer_id)


#     offers_now.append(offer_id)

# print("amount of offers: " + str(len(offers)))

# file = open("file.txt", "w")
# for offer in offers_now:
#     file.write(offer + "\n")
# file.close()

