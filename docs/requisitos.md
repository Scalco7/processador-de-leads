# Requisitos de Usuário

## Objetivo
O sistema deve processar uma lista de *leads* (potenciais clientes) contida em um arquivo JSON, validar as informações e enriquecer cada lead com sugestões personalizadas obtidas de APIs públicas.



## Requisitos Funcionais

### RF01 - Leitura de dados
O sistema deve ler um arquivo `leads.json` contendo uma lista de objetos com os campos:
- `nome`
- `telefone`
- `interesse`
- `orçamento`

### RF02 - Validação de dados
O sistema deve:
- Remover duplicados (mesmo telefone ou mesmo nome e telefone);
- Padronizar o formato dos telefones para `+55XXXXXXXXXXX`;
- Corrigir capitalização dos nomes;
- Descartar leads com campos vazios ou inválidos.

### RF03 - Enriquecimento com APIs Públicas
O sistema deve identificar o interesse de cada lead e consultar a API correspondente para gerar sugestões personalizadas, adicionando um campo:
```json
"sugestões": {
  "mensagem": "Texto com informação ou curiosidade",
  "fonte": "URL da API utilizada"
}
```

### RF04 - Geração de arquivo final

O sistema deve gerar um arquivo leads_final.json com os leads válidos e enriquecidos, formatado em JSON legível (indentação e UTF-8).

### RF05 - Exibição de logs

Durante a execução, o sistema deve exibir:

 - Quantos leads foram lidos, válidos e removidos;
 - Tempo total de processamento.
