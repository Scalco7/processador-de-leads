import requests
import logging

from src.client.Client import Client

class OKXClient(Client):
    """
    Cliente para consumir a CoinDesk API e obter informações sobre a cotação do Bitcoin.
    """
    
    api_key = 'fce25e12-a519-4dee-8fd3-6c5b15416171'

    BASE_URL = "https://www.okx.com/api/v5/market/ticker"

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_bitcoin_price(self):
        """
        Faz a requisição à OKX API e retorna o preço atual do par BTC-USDT.
        Retorna um dicionário contendo informações principais da cotação.
        """
        try:
            params = {"instId": "BTC-USDT"}
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            if "data" not in data or len(data["data"]) == 0:
                self.logger.warning("Resposta inesperada da OKX API.")
                return {"error": "Dados indisponíveis no momento."}

            ticker = data["data"][0]
            price_info = {
                "symbol": ticker.get("instId"),
                "last": float(ticker.get("last", 0.0)),
                "high24h": float(ticker.get("high24h", 0.0)),
                "low24h": float(ticker.get("low24h", 0.0)),
                "vol24h": float(ticker.get("vol24h", 0.0))
            }

            self.logger.info("Cotação do Bitcoin obtida com sucesso da OKX API.")
            return price_info

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Erro ao consultar OKX API: {e}")
            return {"error": "Falha ao obter cotação do Bitcoin."}

    def get_suggestion(self):
        """
        Gera uma sugestão com base na variação do preço atual do Bitcoin.
        - Se o preço estiver acima da média das últimas 24h → tendência de alta.
        - Se estiver abaixo → oportunidade de compra.
        """
        data = self.get_bitcoin_price()
        if "error" in data:
            return "Não foi possível obter a cotação do Bitcoin no momento."

        try:
            last = data["last"]
            high = data["high24h"]
            low = data["low24h"]

            avg = (high + low) / 2

            if last > avg * 1.03:
                return f"O Bitcoin ({data['symbol']}) está em alta (${last:.2f}). Talvez seja hora de vender!"
            elif last < avg * 0.97:
                return f"O Bitcoin ({data['symbol']}) está em baixa (${last:.2f}). Pode ser uma boa hora para comprar!"
            else:
                return f"O Bitcoin está estável em ${last:.2f}. Acompanhe o mercado antes de tomar decisões."

        except Exception as e:
            self.logger.error(f"Erro ao gerar sugestão da OKX: {e}")
            return "Cotação disponível, mas não foi possível gerar uma sugestão precisa."