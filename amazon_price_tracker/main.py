import requests
import lxml
import smtplib
import os
from twilio.rest import Client
from notification_manager import NotificationManager
#--------------------------------------------------------- webscraping --------------------------------------------------------------------------------------------
from bs4 import BeautifulSoup
url_alt="https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
url="https://www.amazon.in/dp/B09G93RSZF?th=1"
# can accept the url also

response = requests.get(url, headers={"Accept-Language":"en-US,en;q=0.9",
                                     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"
                                     }
                        )
soup = BeautifulSoup(response.content,"lxml")
#print(soup.prettify())
price_html = soup.find("span", class_="a-offscreen")
# returns inner text.getText()
price=price_html.getText()
#print(price)
price_without_currency = price.split('₹')[1]
price_without_comma = price_without_currency.replace(",","")
price_float = float(price_without_comma)
print(price_float)
price = price_float
price_limit=10000000
product_title="IPHONE"


#-- sends-----sms using twilio-------------------------


notification_manager = NotificationManager()
if(price<=price_limit):
    print("sending")
    notification_manager.send_sms(
        message=f"Subject: Low Price Alert -- ₹ {price} for {product_title} has dropped to {price}"
    )






