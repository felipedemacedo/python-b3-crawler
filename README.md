# Python Selenium B3 API

Esta API em Python utiliza Selenium para extrair dados financeiros de Fundos de Investimento Imobiliário (FIIs) do site Status Invest (statusinvest.com.br). A API fornece um endpoint para consultar dados de um ticker específico, retornando preço atual, P/VP e dividend yield em formato JSON.

## Pré-requisitos

- Python 3.x
- Google Chrome instalado
- Dependências listadas em `requirements.txt`

## Instalação

1. Clone ou baixe o repositório.
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Copie o arquivo `.env.example` para `.env` e configure as credenciais:

```bash
cp .env.example .env
```

Edite o `.env` com suas credenciais desejadas.

## Uso

Execute a API:

```bash
python main.py
```

A API estará disponível em `http://localhost:8000`.

### Endpoint

- **GET /fii/{ticker}**

  Retorna os dados do FII para o ticker especificado.

  **Autenticação:** HTTP Basic Auth
  - Username e Password definidos no arquivo `.env`

  **Exemplo de Requisição:**

  ```bash
  curl -u admin:secret123 http://localhost:8000/fii/CACR11
  ```

  **Exemplo de Resposta:**

  ```json
  {
    "ticker": "CACR11",
    "preco": "79,62",
    "pvp": "0,83",
    "dy": "20,00"
  }
  ```

  Se houver erro, a resposta incluirá um campo "erro".

## Notas

- O scraping roda em modo headless.
- Certifique-se de que o ChromeDriver seja compatível com sua versão do Chrome.
- Em produção, use credenciais mais seguras e considere rate limiting.
- O arquivo `.env` contém credenciais sensíveis e deve ser adicionado ao `.gitignore`.