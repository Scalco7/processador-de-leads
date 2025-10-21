import requests
import logging
from src.client.Client import Client

logger = logging.getLogger(__name__)

class OpenMeteoClient(Client):
    """
    Client para a API Open-Meteo.

    Essa API fornece dados climáticos (temperatura, clima, vento etc.)
    e pode ser usada para enriquecer leads com interesses em clima, viagens ou natureza.
    """

    BASE_URL = "https://api.open-meteo.com/v1/forecast"
    
    def __init__(self, latitude: float = -23.5505, longitude: float = -46.6333):
        """
        Inicializa o client com coordenadas padrão (São Paulo - Brasil).
        """
        self.latitude = latitude
        self.longitude = longitude

    def get_suggestion(self) -> str:
        """
        Obtém a temperatura atual via API Open-Meteo e retorna uma sugestão.
        """
        
        try:
            params = {
                "latitude": self.latitude,
                "longitude": self.longitude,
                "current_weather": True
            }

            response = requests.get(self.BASE_URL, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()

            weather = data.get("current_weather", {})
            temperature = weather.get("temperature")

            if temperature is not None:
                if temperature > 30:
                    advice = f"Está quente ({temperature}°C)! Que tal um dia de praia ou piscina?"
                elif temperature < 15:
                    advice = f"Está frio ({temperature}°C)! Perfeito para um chocolate quente ☕."
                else:
                    advice = f"A temperatura está agradável ({temperature}°C). Um ótimo dia para sair!"
            else:
                advice = "Não foi possível determinar a temperatura atual."

            logger.info("Dados obtidos com sucesso da Open-Meteo API.")
            return advice

        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao consultar Open-Meteo API: {e}")
            return None
