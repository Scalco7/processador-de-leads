import requests
import logging
from src.client.Client import Client

logger = logging.getLogger(__name__)

class AdviceSlipClient(Client):
    """
    Client para a API Advice Slip.

    Essa API fornece conselhos aleatórios e é usada como fallback
    quando o interesse do lead não corresponde a nenhuma API específica.
    """

    BASE_URL = "https://api.adviceslip.com/advice"

    def get_suggestion(self) -> str:
        """
        Obtém um conselho aleatório da API Advice Slip.
        """
        try:
            response = requests.get(self.BASE_URL, timeout=5)
            response.raise_for_status()
            data = response.json()

            slip = data.get("slip", {})
            advice = slip.get("advice", "Nenhum conselho disponível no momento.")

            logger.info("Conselho obtido com sucesso da Advice Slip API.")
            return advice

        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao consultar Advice Slip API: {e}")
            return None
