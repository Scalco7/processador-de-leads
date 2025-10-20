
from src.client.OKX.OKXClient import OKXClient

moneyClient = OKXClient()

print(moneyClient.get_bitcoin_price())
print(moneyClient.get_suggestion())