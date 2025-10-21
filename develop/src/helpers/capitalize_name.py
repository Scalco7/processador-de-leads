import logging

logger = logging.getLogger(__name__)

def capitalize_name(name: str) -> str:
    """
    Padroniza a capitalização dos nomes próprios.
    Exemplo: "joÃO da silva" → "João da Silva"
    """
    if not name or not isinstance(name, str):
        logger.warning(f"Nome inválido: {name}")
        return None

    lowercase_words = {"de", "da", "do", "das", "dos", "e"}
    parts = name.strip().lower().split()

    formatted_parts = []
    for word in parts:
        if word in lowercase_words:
            formatted_parts.append(word)
        else:
            formatted_parts.append(word.capitalize())

    formatted_name = " ".join(formatted_parts)

    return formatted_name
