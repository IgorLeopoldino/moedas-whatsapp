# Envio de dados de moedas para Whatsapp

Uma aplicação simples que pega os valores do Dólar, Euro e Bitcoin via API e envia esses dados para o Whatsapp em tempo real.

## Descrição

Esse projeto é uma aplicação automatizada que permite ao usuário receber no próprio Whatsapp, informações dos valores das moedas Dólar, Euro e Bitcoin em tempo real através de uma API econômica. Esse código porém, teve um schedule com o horário de envio às 7:00 da manhã, 
ou seja, todos os dias às 7:00 o user irá receber esses valores no seu whatsapp.

# Bibliotecas utilizadas
Twilio - envio de mensagens;
Schedule - definição de datas/horários para o envio das mensagens;
Time - para definir um delay de 1 segundo;
Requests - para puxar a requisição da API.
