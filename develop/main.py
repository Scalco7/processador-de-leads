from dotenv import load_dotenv
import logging
import os

from src.helpers.enrich_leads import enrich_leads
from src.client.OKX.OKXClient import OKXClient
from src.helpers.load_leads import load_leads
from src.helpers.format_leads import format_leads

load_dotenv()

LEADS_1_FILE = "data/leads_1.json"
LEADS_2_FILE = "data/leads_2.json"
LEADS_3_FILE = "data/leads_3.json"


# moneyClient = OKXClient()

# print(moneyClient.get_bitcoin_price())
# print(moneyClient.get_suggestion())

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("develop/logs/app.log", encoding="utf-8"),
        logging.StreamHandler() 
    ]
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Iniciando leitura de leads...")
    leads = load_leads(LEADS_1_FILE)
    
    if len(leads) > 0:
        logger.info(f"{len(leads)} leads carregados com sucesso.")
        leads_formatados = format_leads(leads)
        logger.info(f"{len(leads_formatados)} leads formatados com sucesso.")
        
        enriched_leads = enrich_leads(leads_formatados)
        logger.info(f"{len(enriched_leads)} leads enriquecidos com sucesso.")
        
        for lead in enriched_leads:
            logger.info(lead)
            
    logger.info("Tratamento de Leads finalizado.")
