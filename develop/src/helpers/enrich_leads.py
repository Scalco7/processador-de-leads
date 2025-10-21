import logging

from src.client.OKX.OKXClient import OKXClient

logger = logging.getLogger(__name__)

API_MAP = {
    "criptomoedas": OKXClient,
    "finanças": OKXClient,
    "investimentos": OKXClient,
    # "clima": OpenMeteoClient,
    # "viagem": OpenMeteoClient,
    # "aventura": BoredClient,
    # "lazer": BoredClient,
    # "curiosidades": RandomUselessFactsClient,
    # "animais": CatFactsClient,
    # "gatos": CatFactsClient,
}

def enrich_leads(leads: list) -> list:
    """
    Conecta cada lead à API correspondente com base em seu interesse
    e adiciona sugestões ou informações externas ao objeto do lead.
    """
    enriched = []

    for lead in leads:
        try:
            interesse = lead.get("interesse", "").lower().strip()
            # api_class = API_MAP.get(interesse, AdviceSlipClient)
            api_class = API_MAP.get(interesse)

            client = api_class()
            suggestion = client.get_suggestion()

            lead["sugestao"] = suggestion
            enriched.append(lead)

            logger.info(f"Lead '{lead.get('nome')}' enriquecido com {api_class.__name__}")

        except Exception as e:
            logger.error(f"Erro ao enriquecer lead {lead.get('nome')}: {e}")
            lead["sugestao"] = {"erro": str(e)}
            enriched.append(lead)

    return enriched
    