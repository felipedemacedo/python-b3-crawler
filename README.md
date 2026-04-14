# Python Selenium B3 Scraper

Este projeto é um script em Python que utiliza Selenium para extrair dados financeiros de Fundos de Investimento Imobiliário (FIIs) do site Status Invest (statusinvest.com.br). O script coleta informações como preço atual, P/VP e dividend yield para uma lista de tickers de FIIs.

## Pré-requisitos

- Python 3.x
- Google Chrome instalado
- Selenium WebDriver (instalado via pip)

## Instalação

1. Clone ou baixe o repositório.
2. Instale as dependências:

```bash
pip install selenium
```

## Uso

Execute o script principal:

```bash
python main.py
```

O script irá processar uma lista pré-definida de tickers de FIIs e imprimir os dados extraídos no console.

## Exemplo de Output

```shell
{'ticker': 'BRCO11', 'preco': '114,60', 'pvp': '0,99', 'dy': '9,32'}
{'ticker': 'BTHF11', 'preco': '9,29', 'pvp': '0,92', 'dy': '12,31'}
{'ticker': 'CACR11', 'preco': '79,62', 'pvp': '0,83', 'dy': '20,00'}
{'ticker': 'HSML11', 'preco': '95,14', 'pvp': '0,92', 'dy': '8,55'}
{'ticker': 'MFII11', 'preco': '68,46', 'pvp': '0,71', 'dy': '18,77'}
{'ticker': 'MXRF11', 'preco': '9,81', 'pvp': '1,02', 'dy': '12,21'}
{'ticker': 'RBRX11', 'preco': '8,72', 'pvp': '0,89', 'dy': '12,30'}
{'ticker': 'RZAT11', 'preco': '94,77', 'pvp': '0,94', 'dy': '12,61'}
{'ticker': 'XPLG11', 'preco': '100,00', 'pvp': '0,94', 'dy': '9,84'}
{'ticker': 'XPML11', 'preco': '111,63', 'pvp': '1,01', 'dy': '9,90'}
{'ticker': 'HGLG11', 'preco': '157,11', 'pvp': '0,95', 'dy': '8,38'}
```

## Notas

- O script roda em modo headless, ou seja, sem interface gráfica.
- Certifique-se de que o ChromeDriver esteja compatível com a versão do seu navegador Chrome. O Selenium Manager geralmente cuida disso automaticamente.
- Em caso de bloqueios ou timeouts, o script pode retornar mensagens de erro.