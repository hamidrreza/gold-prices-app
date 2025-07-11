from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    try:
        url = 'https://tabangohar.com'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        taban = soup.find('div', id='gram18_price_now').text.strip()

        url1 = 'https://www.tgju.org/profile/geram18'
        response1 = requests.get(url1)
        soup1 = BeautifulSoup(response1.text, 'html.parser')
        price1 = soup1.find('div', class_='fs-cell fs-xl-3 fs-lg-3 fs-md-6 fs-sm-12 fs-xs-12 top-header-item-block-2 mobile-top-item-hide').span.find_next('span').span.text
        price11 = price1[:-1].replace(',', '')
        tgju1 = ""
        for i in range(len(price11)):
            if i % 3 == 0 and i != 0:
                tgju1 += ","
            tgju1 += price11[len(price11)-1-i]
        tgju = tgju1[::-1]

        url2 = 'https://arzdigital.com/coins/bitcoin/'
        response2 = requests.get(url2)
        soup2 = BeautifulSoup(response2.text, 'html.parser')
        btc = soup2.find('div', class_='arz-coin-page-data__coin-price coinPrice btcprice pulser-dollar-bitcoin').text.strip()

    except Exception as e:
        taban = tgju = btc = f"خطا: {str(e)}"

    return render_template('index.html', taban=taban, tgju=tgju, btc=btc)

if name == 'main':
    app.run(host='0.0.0.0', port=10000)
