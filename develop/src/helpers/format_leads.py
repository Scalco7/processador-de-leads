import logging

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

        nome = lead.get("nome")
        telefone = lead.get("telefone")
        interesse = lead.get("interesse")
        orcamento = lead.get("orçamento")

        if not any([nome, telefone]):
            logger.info(f"Lead nulo removido: {lead}")
            continue

        telefone = format_phone_number(telefone)
        lead['telefone'] = telefone

        key = (nome, telefone)
        if key in unique:
            logger.info(f"Lead duplicado removido: {lead}")
            continue
        unique[key] = True

        if all([nome, telefone, interesse, orcamento]):
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
