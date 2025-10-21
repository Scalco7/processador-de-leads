from dotenv import load_dotenv
import os

from src.client.OKX.OKXClient import OKXClient
from src.helpers.load_leads import load_leads

load_dotenv()

LEADS_1_FILE = "data/leads_1.json"
LEADS_2_FILE = "data/leads_2.json"
LEADS_3_FILE = "data/leads_3.json"


# moneyClient = OKXClient()

# print(moneyClient.get_bitcoin_price())
# print(moneyClient.get_suggestion())

leads = load_leads(LEADS_2_FILE)
print(f"Foram carregados {len(leads)} leads.")
for lead in leads:
    print(lead)