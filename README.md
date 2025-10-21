# ⚙️ Processador de Leads

Este projeto em Python foi desenvolvido para automatizar o processo de tratamento e enriquecimento de uma base de leads. O sistema lê dados de potenciais clientes a partir de arquivos JSON, realiza validações, padroniza as informações e enriquece cada lead com sugestões personalizadas, consultando APIs públicas com base nos interesses de cada um.

## ✨ Funcionalidades Principais

- **Leitura de Dados**: Carrega leads de arquivos JSON.
- **Validação e Limpeza**:
  - Remove leads duplicados (baseado no telefone ou na combinação de nome e telefone).
  - Padroniza números de telefone para o formato internacional brasileiro (`+55XXXXXXXXXXX`).
  - Corrige a capitalização de nomes.
  - Descarta leads com informações inválidas ou ausentes.
- **Enriquecimento com APIs**: Conecta-se a diferentes APIs públicas para obter sugestões relevantes com base no interesse de cada lead.
- **Geração de Relatório**: Salva os leads processados e enriquecidos em um novo arquivo JSON (`leads.json`), formatado para fácil leitura.
- **Logging**: Registra todas as etapas do processo, desde a leitura até o enriquecimento, em um arquivo de log (`develop/logs/app.log`) e no console.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **requests**: Para realizar as chamadas HTTP às APIs externas.
- **logging**: Para realizar os logs.
- **python-dotenv**: Para gerenciar variáveis de ambiente.

## 📂 Estrutura do Projeto

```
processador-de-leads/
├── data/
│   ├── leads.json         # Arquivo de entrada com os leads
│   └── out/
│       └── leads.json         # Arquivo de saída com os leads processados
├── develop/
│   ├── src/
│   │   ├── client/            # Módulos dos clientes de API
│   │   ├── helpers/           # Funções auxiliares (formatação, enriquecimento)
│   │   └── main.py            # Ponto de entrada da aplicação
│   ├── logs/
│   │   └── app.log            # Arquivo de log
│   └── requirements.txt       # Dependências do projeto
├── docs/
│   └── ...                    # Documentação do projeto
└── README.md                  # Este arquivo
```

## ⚙️ Configuração

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/scalco7/processador-de-leads.git
    cd processador-de-leads
    ```

2.  **Crie um ambiente virtual e ative-o:**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r develop/requirements.txt
    ```

## 🚀 Como Executar

1.  Certifique-se de que seu arquivo de leads (`data/leads.json`) está no local correto.
2.  Execute o script principal a partir da raiz do projeto:
    ```bash
    python develop/main.py
    ```
3.  Após a execução, o arquivo com os leads processados e enriquecidos será salvo em `data/out/leads.json`.

## 🧠 Mapeamento de Interesses e APIs

O enriquecimento dos leads é feito com base no campo `interesse`. Cada interesse é mapeado para um cliente de API específico, conforme a tabela abaixo:

| Categoria | Interesses Relacionados | API Utilizada | Cliente |
|---------------------------------|-----------------------------------------------------------------------------------|--------------------------------|------------------------------|
| 💰 **Negócios & Tecnologia** | `criptomoedas`, `finanças`, `investimentos`, `tecnologia`, `economia`, `empreendedorismo` | OKX API | `OKXClient` |
| ✈️ **Viagens & Natureza** | `clima`, `viagem`, `natureza`, `esportes` | Open-Meteo API | `OpenMeteoClient` |
| 🎉 **Lazer & Atividades** | `aventura`, `lazer`, `diversão` | Bored API | `BoredClient` |
| 💡 **Curiosidades & Conhecimento** | `curiosidades`, `historia`, `ciência`, `arte`, `automóveis`, `games`, `fotografia` | Useless Facts API | `RandomUselessFactsClient` |
| 🐾 **Animais & Pets** | `animais`, `gatos`, `pets` | Cat Facts API | `CatFactsClient` |
| 🧭 **Padrão (Fallback)** | Qualquer outro interesse não listado acima. | Advice Slip API | `AdviceSlipClient` |