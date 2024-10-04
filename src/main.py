from chatbot import create_buttons, check_chat_started, handle_summary
from dotenv import load_dotenv
import summarizer
import researcher
import telebot
import os


# Função para configurar o bot e as APIs
def setup():
    load_dotenv()
    print("Conectando ao bot do telegram...")
    bot = telebot.TeleBot(os.getenv("TELEGRAM_KEY"))
    print("Conectado com sucesso!")

    print("Conectando com as APIs: Maritaca e NewsApi...")
    maritaca = summarizer.MaritacaAdapter(os.getenv("MARITACA_KEY"))
    print("Conectado com Maritaca!")
    news = researcher.NewsAdapter(os.getenv("NEWSAPI_KEY"), 'pt', 'br', ['blasting-news-br'])    
    print("Conectado com NewsAPI!")

    return bot, maritaca, news


if __name__ == "__main__":
    bot, maritaca, news = setup()
    chats = {}

    @bot.message_handler(commands=['start'])
    def welcome(message):
        chats[message.chat.id] = message.chat

        welcome_text = (
            "*Espresso News* ☕📰\n\n"
            "Eu sou um bot e faço os melhores resumos de notícias para você!\n\n"
            "↪️ Se você quer um resumo de tudo que tá rolando, é só clicar em '🌎 Como está o dia'.\n\n"
            "↪️ Quer algo mais específico? É só escolher o assunto que te interessa e eu trago as novidades pra você!\n\n"
            "💡 Divirta-se se informando!"
        )
        bot.send_message(message.chat.id, welcome_text, reply_markup=create_buttons(), parse_mode='Markdown')

    @bot.message_handler(func=lambda message: True)
    def reply_to_message(message):
        chat = chats.get(message.chat.id)
        if check_chat_started(chat, message, bot):
                choose_text = (
                     "*Espresso News* ☕📰\n\n"
                     "Olá, "+ chat.username +"!👾\n\n" 
                     "Por favor, escolha um dos assuntos abaixo ou veja o resumo do dia:", 
                )
                
                bot.send_message(chat.id,choose_text, reply_markup=create_buttons(), parse_mode='Markdown')


    @bot.callback_query_handler(func=lambda call: True)
    def return_summary(call):
        chat = chats.get(call.message.chat.id)
        if check_chat_started(chat, call.message, bot):
            handle_summary(bot, call, chat, maritaca, news)

    bot.infinity_polling(timeout=60, long_polling_timeout=60)