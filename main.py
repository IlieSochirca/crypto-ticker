import requests

from utils.mail import send_email

base_url = "https://pro-api.coinmarketcap.com/v1/"

currencies_listing = "/cryptocurrency/listings/latest"

currencies_mapping = "cryptocurrency/map"

currency_info = "/cryptocurrency/info"

currency_quotes = "/cryptocurrency/quotes/latest"

headers = {"Accepts": "Accepts",
           "X-CMC_PRO_API_KEY": "a9f29d72-eb2e-4d65-b195-a0e73552170b"}

# response_crypto_list = requests.get(url=f'{base_url}/{currencies_listing}', headers=headers)

# response_crypto_map = requests.get(url=f'{base_url}/{currencies_mapping}', headers=headers)

# data = response_crypto_map.json()
# with open("cryptos_list", "w") as file_halder:
#     file_halder.write(response_crypto_list.text)

# with open("cryptos_map", "w") as file_handler:
#     file_handler.write(response_crypto_map.text)


symbols = "XRP,BTC,ETH"

info_url_parameters = {"symbol": "XRP"}
quotes_url_parameters = {"symbol": "XRP,BTC,ETH", "convert": "USD"}

response_currency_info = requests.get(url=f'{base_url}/{currency_info}', headers=headers, params=info_url_parameters)

response_currency_quotes = requests.get(url=f'{base_url}/{currency_quotes}', headers=headers,
                                        params=quotes_url_parameters)

data = (response_currency_quotes.json())["data"]
aggregated_data = {}

for symbol in symbols.split(","):
    currency = data[symbol]
    name = currency["name"]
    symbol = currency["symbol"]
    circulation_supply = currency["circulating_supply"]
    total_supply = currency["total_supply"]
    quotes = currency["quote"]["USD"]

    price = quotes["price"]
    market_cap = quotes["market_cap"]
    percent_change_1h = quotes["percent_change_1h"]
    percent_change_24h = quotes["percent_change_24h"]
    percent_change_7d = quotes["percent_change_7d"]

    currency_data = {}
    currency_data["Name"] = name
    currency_data["Circulation Supply"] = circulation_supply
    currency_data["Total Supply"] = total_supply
    currency_data["Market Cap"] = market_cap
    currency_data["Hour Change"] = str(percent_change_1h)
    currency_data["Day Change"] = str(percent_change_24h)
    currency_data["Week Change"] = str(percent_change_7d)
    currency_data["Price"] = price

    aggregated_data[symbol] = currency_data



if __name__ == "__main__":
    send_email(aggregated_data)
