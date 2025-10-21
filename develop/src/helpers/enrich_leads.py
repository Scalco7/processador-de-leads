import logging

from src.client.Bored.BoredClient import BoredClient
from src.client.OpenMeteo.OpenMeteoClient import OpenMeteoClient
from src.client.AdviceSlip.AdviceSlipClient import AdviceSlipClient
from src.client.OKX.OKXClient import OKXClient

logger = logging.getLogger(__name__)

# API_MAP = {
#     "criptomoedas": OKXClient,
#     "finanças": OKXClient,
#     "investimentos": OKXClient,
#     "clima": OpenMeteoClient,
#     "viagem": OpenMeteoClient,
#     "aventura": BoredClient,
#     "lazer": BoredClient,
#     "curiosidades": RandomUselessFactsClient,
#     "animais": CatFactsClient,
#     "gatos": CatFactsClient,
# }

def enrich_leads(leads: list) -> list:
    """
    Conecta cada lead à API correspondente com base em seu interesse
    e adiciona sugestões ou informações externas ao objeto do lead.
    """
    enriched = []

    for lead in leads:
        try:
            interesse = lead.get("interesse", "").lower().strip()
            client = AdviceSlipClient()
            
            match interesse:
                case "criptomoedas" | 'finanças' | 'investimentos':
                    client = OKXClient()
                case "clima" | 'viagem':
                    client = OpenMeteoClient(-16.5955381, -39.1095927)
                case 'aventura' | 'lazer':
                    client = BoredClient()
                case _:
                    client = AdviceSlipClient()
            
            suggestion = client.get_suggestion()

            lead["sugestao"] = suggestion
            enriched.append(lead)

            logger.info(f"Lead '{lead.get('nome')}' enriquecido com {type(client).__name__}")

        except Exception as e:
            logger.error(f"Erro ao enriquecer lead {lead.get('nome')}: {e}")
            lead["sugestao"] = {"erro": str(e)}
            enriched.append(lead)

    return enriched
    