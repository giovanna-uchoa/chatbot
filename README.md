# Espresso News

Projeto desenvolvido para o bootcamp "IA + Bots", promovido pelo grupo de extensão USP CodeLab Butantã, o Espresso News é um chatbot para Telegram que informa o usuário sobre as notícias do dia. O chatbot foi implementado no Telegram, utilizando as APIs da [News API](https://www.newsapi.ai/) e Maritaca AI. A API Maritaca é responsável por categorizar as manchetes e gerar resumos com base nessas categorias

## Acesso ao Bot

t.me/espressoNews_bot

## Pré-Requisitos
Para rodar o projeto na sua máquina local, você precisa ter as seguintes ferramentas instaladas:
* Python 3
* Python PIP

## Como Rodar o Projeto?
1. Clone o repositório na sua máquina
2. Copie o .env.example e crie um .env para configurar variáveis do seu sistema: `cp .env.example .env`
3. Rode `./run.sh` para configurar o ambiente virtual e instalar as dependências
4. Ative o ambiente virtual: `source ./.venv/bin/activate`
5. Finalmente, rode `python3 src/main.py` para ativar o chatbot

**NOTA: Para desativar o ambiente virtual basta executar `deactivate` na linha de comando.**
