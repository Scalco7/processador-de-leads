import re
import logging

logger = logging.getLogger(__name__)

def format_phone_number(phone: str) -> str:
    """
    Formata um número de telefone para o padrão internacional brasileiro:
    +55DDDXXXXXXXXX

    - Remove tudo que não seja número
    - Adiciona o prefixo +55 se não existir
    - Mantém o DDD e o número final
    """
    if not phone or not isinstance(phone, str):
        logger.warning(f"Número de telefone inválido: {phone}")
        return None

    digits = re.sub(r'\D', '', phone)

    digits = digits.lstrip('0')

    if len(digits) < 10:
        logger.warning(f"Número muito curto: {phone}")
        return None

    if digits.startswith("55"):
        formatted = f"+{digits}"
    else:
        formatted = f"+55{digits}"

    formatted = formatted[:14]
    return formatted
