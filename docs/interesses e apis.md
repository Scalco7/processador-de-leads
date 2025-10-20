# 🧠 Tipos de Interesse — Mapeamento e Contexto

Cada lead possui um campo `interesse`, usado para determinar qual API será consultada para enriquecer suas informações.

Abaixo estão os interesses mapeados e suas categorias temáticas:

| Categoria | Interesses Relacionados | Descrição |
|------------|--------------------------|------------|
| 💰 **Negócios & Tecnologia** | tecnologia, finanças, empreendedorismo | Leads voltados a inovação, mercado financeiro e tecnologia. As sugestões podem conter informações sobre tendências econômicas e digitais. |
| ✈️ **Viagens & Natureza** | viagens, natureza, esportes | Leads interessados em atividades ao ar livre e turismo. O enriquecimento utiliza dados de clima e condições meteorológicas. |
| 🎭 **Cultura & Entretenimento** | gastronomia, música, moda, cinema, arte | Leads voltados a lazer e cultura. O sistema fornece sugestões de atividades recreativas relacionadas. |
| 🌱 **Desenvolvimento Pessoal & Bem-Estar** | saúde, educação, astrologia, leitura | Leads que buscam aprimoramento pessoal, equilíbrio e conhecimento. Recebem conselhos inspiracionais. |
| 🐾 **Animais & Pets** | pets | Leads com interesse em animais domésticos. Recebem curiosidades sobre gatos. |
| 🔧 **Curiosidades & Outros** | automóveis, games, fotografia, sustentabilidade | Leads de interesses diversos. Recebem fatos aleatórios e interessantes. |
| 🧭 **Padrão (Fallback)** | qualquer outro não listado | Para interesses não mapeados, uma API padrão de conselhos é utilizada. |



# 🌍 APIs Públicas Utilizadas — Enriquecimento de Leads

## 🧩 Visão Geral
Cada API foi escolhida por sua simplicidade, estabilidade e relevância temática.  
Todas são **gratuitas e públicas**, não exigem autenticação e retornam dados em JSON.

---

### 1. **CoinDesk API**
- **URL:** `https://api.coindesk.com/v1/bpi/currentprice.json`
- **Interesses:** tecnologia, finanças, empreendedorismo  
- **Descrição:** Retorna a cotação atual do Bitcoin em USD, GBP e EUR.  
- **Exemplo de retorno:**
  ```json
  {"bpi": {"USD": {"rate_float": 68750.34}}}
    ```

### 2. Open-Meteo API
- **URL:** https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&current_weather=true
- **Interesses:** viagens, natureza, esportes
- **Descrição:** Retorna informações sobre clima e temperatura atuais.
- **Exemplo de retorno:**
    ```json
    {"current_weather": {"temperature": 26.4, "windspeed": 8.5}}
    ```


### 3. Bored API
- **URL:** https://www.boredapi.com/api/activity
- **Interesses:** gastronomia, música, moda, cinema, arte
- **Descrição:** Retorna uma sugestão de atividade recreativa ou cultural.
- **Exemplo de retorno:**
    ```json
    {"activity": "Try a new recipe."}
    ```

### 4. Advice Slip API
- **URL:** https://api.adviceslip.com/advice
- **Interesses:** saúde, educação, astrologia, leitura, outros (padrão)
- **Descrição:** Retorna um conselho ou frase inspiracional.
- **Exemplo de retorno:**
    ```json
    {"slip": {"advice": "Don’t count the days, make the days count."}}
    ```

### 5. Cat Facts API
- **URL:** https://catfact.ninja/fact
- **Interesses:** pets
- **Descrição:** Retorna fatos curiosos e engraçados sobre gatos.
- **Exemplo de retorno:**
    ```json
    {"fact": "Cats sleep 70% of their lives."}
    ```

### 6. Random Useless Facts API
- **URL:** https://uselessfacts.jsph.pl/api/v2/facts/random
- **Interesses:** automóveis, games, fotografia, sustentabilidade
- **Descrição:** Retorna fatos aleatórios e divertidos de diversas áreas.
- **Exemplo de retorno:**
    ```json
    {"text": "The inventor of the Pringles can is buried in one."}
    ```

### 7. Advice Slip API (Padrão)
- **URL:** https://api.adviceslip.com/advice
- **Interesses:** Api padrão de qualquer interesse não mapeado.
- **Descrição:** Retorna frases de sabedoria e conselhos aleatórios.
- **Exemplo de retorno:**
    ```json
    {
        "slip": {
            "id": 45,
            "advice": "Don't compare your beginning to someone else's middle."
        }
    }
    ```