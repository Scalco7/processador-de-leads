import requests
import logging
from src.client.Client import Client

logger = logging.getLogger(__name__)

class BoredClient(Client):
    """
    Client para a Bored API.

    Essa API fornece ideias de atividades aleatórias para lazer, aventura ou viagem.
    Ideal para enriquecer leads que buscam experiências e diversão.
    """

    BASE_URL = "https://bored-api.appbrewery.com/random"

    def get_suggestion(self):
        """
        Obtém uma atividade aleatória da Bored API e retorna como sugestão.
        """
        try:
            response = requests.get(self.BASE_URL, timeout=5)
            response.raise_for_status()
            data = response.json()

            activity = data.get("activity", "Nenhuma atividade disponível.")

            logger.info("Atividade obtida com sucesso da Bored API.")
            return activity

        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao consultar Bored API: {e}")
            return None
