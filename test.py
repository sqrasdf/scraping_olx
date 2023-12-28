from bs4 import BeautifulSoup
import requests
import pyperclip

# link = "https://www.olx.pl/oferty/q-lego-4195/?search%5Border%5D=created_at:desc"

link_list = [
    "https://www.olx.pl/oferty/q-lego-4195/?search%5Border%5D=created_at:desc",
    "https://www.olx.pl/oferty/q-Lego-Piraci-z-Karaibów/?search%5Border%5D=created_at:desc",
    "https://www.olx.pl/oferty/q-Lego-Pirates-of-the-Caribbean/?search%5Border%5D=created_at:desc"
]

# read previous data from txt file
file = open("file.txt", "r")
file_text = file.read()
offers_past = file_text.split("\n")
file.close()

# get current ids of offers
offers_now = []

for link in link_list:
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, "lxml")

    offers = soup.find("div", class_='css-oukcj3').find_all("div", class_="css-1sw7q4x")

    for offer in offers:
        offer_name = offer.find("h6", class_ = "css-16v5mdi er34gjf0").text
        offer_link = offer.find("a").get("href")
        offer_link = "https://www.olx.pl" + offer_link
        offer_id = offer.get("id")
        print(offer_id)


        offers_now.append(offer_id)

# print("amount of offers: " + str(len(offers)))
# print("my old offer (885743309) in current offers:", "885743309" in offers_now)
# print("my new offer (886201838) in current offers:", "886201838" in offers_now)
# print("my old offer (886202326) in current offers:", "886202326" in offers_now)

file = open("file.txt", "w")
for offer in offers_now:
    file.write(offer + "\n")
file.close()

copy_str = "\n".join(offers_now)
pyperclip.copy(copy_str)