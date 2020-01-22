import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Acer-i5-9300H-Processor-15-6-inch-AN715-51/dp/B07TD8KKDY/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=hiwh6eT5S3qTNPB-UsBRMw&hsa_cr_id=5706079120602&ref_=sb_s_sparkle_slot'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_dealprice").get_text()
    price = price.replace(',', '')
    c_price = float(price[2:7])
    if c_price < 63000:
        send_mail()
    else:
        print("Sike!")
    print(title.strip())
    print(c_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('crahul1721@gmail.com', 'l*************f')

    subject = 'Price fell down'
    body = 'Check the amazon link ' \
           'https://www.amazon.in/Acer-i5-9300H-Processor-15-6-inch-AN715-51/dp/B07TD8KKDY/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=hiwh6eT5S3qTNPB-UsBRMw&hsa_cr_id=5706079120602&ref_=sb_s_sparkle_slot'

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'crahul1721@gmail.com',
        'ytpremium15@gmail.com',
        msg
    )

    print('HEYY EMAIL HAS BEEN SENT!!')
    server.quit()


while True:
    check_price()
    time.sleep(60 * 60)
