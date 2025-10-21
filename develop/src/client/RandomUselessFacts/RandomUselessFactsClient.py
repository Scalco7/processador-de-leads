import requests
import logging
from src.client.Client import Client

logger = logging.getLogger(__name__)

class RandomUselessFactsClient(Client):
    """
    Client para a Useless Facts API.

    Essa API retorna fatos aleatórios, curiosos e muitas vezes inúteis,
    perfeitos para leads com interesses em curiosidades e entretenimento.
    """

    BASE_URL = "https://uselessfacts.jsph.pl/api/v2/facts/random"

    def get_suggestion(self):
        """
        Obtém um fato aleatório da Useless Facts API e retorna como sugestão.
        """
        try:
            response = requests.get(self.BASE_URL, timeout=5)
            response.raise_for_status()
            data = response.json()

            fact = data.get("text", "Nenhum fato curioso disponível.")

            logger.info("Fato obtido com sucesso da Useless Facts API.")
            return fact

        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao consultar Useless Facts API: {e}")
            return None
