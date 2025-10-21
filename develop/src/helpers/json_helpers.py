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

def save_json(data: List[Dict[str, Any]], file_path: str) -> None:
    """
    Exporta uma lista de dicionários (ex: leads enriquecidos) para um arquivo JSON.
    O arquivo é salvo com indentação e codificação UTF-8.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            logger.info(f"Arquivo salvo com sucesso: {file_path}")
    except Exception as e:
        logger.error(f"Erro ao salvar arquivo JSON em {file_path}: {e}")