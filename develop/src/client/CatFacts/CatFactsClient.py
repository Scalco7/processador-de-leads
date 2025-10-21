import requests
from src.client.Client import Client
import logging

class CatFactsClient(Client):
    """
    Esta classe conecta-se à API pública catfact.ninja para obter fatos aleatórios sobre gatos.
    Cada chamada à função get_suggestion() retorna um fato divertido que pode ser usado para enriquecer dados
    ou gerar curiosidades em um fluxo de comunicação.
    """

    BASE_URL = "https://catfact.ninja/fact"

    def get_suggestion(self):
        """
        Faz uma requisição GET para a API catfact.ninja/fact e retorna um fato sobre gatos.
        Caso ocorra um erro de conexão ou a resposta seja inválida, retorna uma mensagem padrão.
        """
        try:
            response = requests.get(self.BASE_URL, timeout=5)
            response.raise_for_status()
            data = response.json()
            return data.get("fact", "Os gatos são criaturas misteriosas — e esta API não respondeu.")
        except Exception as e:
            logging.error(f"Erro ao buscar fato sobre gatos: {e}")
            return "Os gatos decidiram não compartilhar fatos agora."
