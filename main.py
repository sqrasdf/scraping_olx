from bs4 import BeautifulSoup
import requests

import http.client, urllib
from datetime import datetime

api_token = "as7kmkwzoaxu7bzwdz6rjycp25rm2a"  # app token
user_key = "u759ikjxp3m64f91oudv2gd95u4b7v"   # my token
adik_key = "ufs46mazffpk9roie9kxhwwe81785o"   # adik's token

def notifySqr(message):
  conn = http.client.HTTPSConnection("api.pushover.net:443")
  conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
      "token": api_token,
      "user": user_key,
      "message": message,
    }), { "Content-type": "application/x-www-form-urlencoded" })
  conn.getresponse()

def notifyAdik(message):
  conn = http.client.HTTPSConnection("api.pushover.net:443")
  conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
      "token": api_token,
      "user": adik_key,
      "message": message,
    }), { "Content-type": "application/x-www-form-urlencoded" })
  conn.getresponse()


link = "https://www.olx.pl/oferty/q-lego-4195/?search%5Border%5D=created_at:desc"

# read previous data from txt file
file = open("file.txt", "r")
file_text = file.read()
offers_past = file_text.split("\n")
file.close()

# for offer in offers_past:
#     notifySqr(offer)

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

    # comparing current and past ids
    if offer_id not in offers_past:
        print("notifying about: " + offer_name + " " + offer_id)
        notifySqr(offer_name + "\n" + link)
        # notifyAdik(offer_name + "\n" + link)

    offers_now.append(offer_id)

file = open("file.txt", "w")
for offer in offers_now:
    file.write(offer + "\n")
file.close()


# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# notifySqr("good file, time: " + current_time)