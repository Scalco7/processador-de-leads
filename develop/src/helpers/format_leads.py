import logging

from src.helpers.capitalize_name import capitalize_name
from src.helpers.format_phone_number import format_phone_number

logger = logging.getLogger(__name__)

def format_leads(leads: list) -> list:
    """
    Limpa, valida e organiza a lista de leads.
    - Remove duplicados (por nome + telefone)
    - Remove nulos
    - Move incompletos para o final
    """
    if not leads or not isinstance(leads, list):
        logger.warning("Lista de leads inválida ou vazia.")
        return []

    unique = {}
    valid_leads = []
    incomplete_leads = []

    for lead in leads:
        if not isinstance(lead, dict):
            logger.warning(f"Lead inválido (não é dict): {lead}")
            continue

        name = lead.get("nome")
        phone = lead.get("telefone")
        interest = lead.get("interesse")
        budget = lead.get("orçamento")

        if not any([name, phone]):
            logger.info(f"Lead nulo removido: {lead}")
            continue

        phone = format_phone_number(phone)
        name = capitalize_name(name)

        lead['nome'] = name
        lead['telefone'] = phone
        
        key = (name, phone)
        if key in unique:
            logger.info(f"Lead duplicado removido: {lead}")
            continue
        unique[key] = True

        if all([name, phone, interest, budget]):
            valid_leads.append(lead)
        else:
            incomplete_leads.append(lead)

    total_original = len(leads)
    total_validos = len(valid_leads)
    total_incompletos = len(incomplete_leads)

    logger.info(f"Total original: {total_original}")
    logger.info(f"Leads válidos: {total_validos}")
    logger.info(f"Incompletos: {total_incompletos}")
    logger.info(f"Removidos: {total_original - (total_validos + total_incompletos)}")

    return valid_leads + incomplete_leads
