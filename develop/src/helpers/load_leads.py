import json
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

def load_leads(file_path: str) -> List[Dict[str, Any]]:
    """
    Lê um arquivo JSON contendo leads e retorna uma lista de dicionários.

    :param file_path: Caminho do arquivo JSON de leads
    :return: Lista de leads como dicionários
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                logger.warning(f"O arquivo {file_path} não contém uma lista de leads.")
                return []
            return data
    except FileNotFoundError:
        logger.error(f"Arquivo {file_path} não encontrado.")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Erro ao decodificar JSON no arquivo {file_path}: {e}")
        return []
    except Exception as e:
        logger.error(f"Erro inesperado ao ler {file_path}: {e}")
        return []
