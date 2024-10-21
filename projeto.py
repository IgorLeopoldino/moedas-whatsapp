# criar um sistema de envio de mensagem automatica via whatsapp que pegue o valor atual do btc e de outras moedas e envie todos os dias as 7 am
import requests
from twilio.rest import Client
import schedule
import time

# 1 - pegar o valor do btc e das moedas via api
api_url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
request = requests.get(api_url)
request_dic = request.json()

def usd():
    doll = float(request_dic["USDBRL"]['bid'])
    dolar = round(doll, 2)
    return dolar

def eur():   
    eur = float(request_dic["EURBRL"]['bid'])
    euro = round(eur, 2)
    return euro

def btc():
    bit = request_dic["BTCBRL"]['bid']
    bitcoin = "R$ " + bit
    return bitcoin

# 2 - enviar a mensagem pelo whatsapp
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client = Client(account_sid, auth_token)
message = client.messages.create(
  from_='whatsapp:+14155238886',
  to='whatsapp:+xxxxxxxxxxxxxx',
  body=f'Preços das moedas em tempo real:\n•Dólar: ${usd()}\n•Euro: €{eur()}\n•Bitcoin: {btc()}'
)

# 3 - programar o horario de envio diario
schedule.every().day.at('07:00').do(message.sid) and schedule.every().day.at('12:00').do(message.sid)

while True:
    schedule.run_pending()
    time.sleep(1)

# 4 - colocar em cloud