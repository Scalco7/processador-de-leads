from dotenv import load_dotenv
import logging
import os

from src.helpers.enrich_leads import enrich_leads
from src.client.OKX.OKXClient import OKXClient
from src.helpers.json_helpers import load_leads, save_json
from src.helpers.format_leads import format_leads

load_dotenv()

LEADS_PATH = "data/leads.json"
OUTPUT_PATH = "data/out/leads.json"


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
    leads = load_leads(LEADS_PATH)
    
    if len(leads) > 0:
        logger.info(f"{len(leads)} leads carregados com sucesso.")
        leads_formatados = format_leads(leads)
        logger.info(f"{len(leads_formatados)} leads formatados com sucesso.")
        
        enriched_leads = enrich_leads(leads_formatados)
        logger.info(f"{len(enriched_leads)} leads enriquecidos com sucesso.")
        
        save_json(enriched_leads, OUTPUT_PATH)
        logger.info(f"Leads enriquecidos salvos em {OUTPUT_PATH}")
            
    logger.info("Tratamento de Leads finalizado.")
