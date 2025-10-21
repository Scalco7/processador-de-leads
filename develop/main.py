from dotenv import load_dotenv

from src.client.OKX.OKXClient import OKXClient

load_dotenv()

moneyClient = OKXClient()

print(moneyClient.get_bitcoin_price())
print(moneyClient.get_suggestion())