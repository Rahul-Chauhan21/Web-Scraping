import requests
from bs4 import BeautifulSoup
import smtplib
import time

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'}

checkPricing = 1


def checkPrice(URL, expectedPrice, email, password, toEmail):
    page = requests.get(url=URL, headers=headers)
    # print(page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    price = price.replace(',', '')
    cPrice = float(price[2:7])
    print(title.strip())
    if cPrice <= expectedPrice:
        print("Price drop! Expected price: {0} Cost Price {1}".format(
            expectedPrice, cPrice))
        global checkPricing
        checkPricing = 0
        send_mail(URL, email, password, toEmail)
    else:
        print("Price currently high!")


def send_mail(URL, email, password, toEmail):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email, password)

    subject = 'Price fell down'
    body = "Check the amazon link: {0}".format(URL)

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        email,
        toEmail,
        msg
    )

    print('HEYY EMAIL HAS BEEN SENT!!')
    server.quit()


# while True:
# check_price()
#time.sleep(60 * 60)

def driverFunc():
    URL = input("Enter URL :")
    expectedPrice = float(input("Enter expected price: "))
    email = input("Input user mail: ")
    password = input(str("Input user password: (Use App password!) "))
    toEmail = input("Recipient user mail: ")
    while checkPricing == 1:
        checkPrice(URL, expectedPrice, email, password, toEmail)
        if checkPricing == 1:
            time.sleep(60*60)  # check every hour.
        else:
            break


driverFunc()
