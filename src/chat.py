import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os

'''
prompt
'''
class Chat:
    def __init__(self, chat_id: int):
        global prompt

        self.chat_id = chat_id
        self.prompt = ""
        self.esperando_noticias = False

chats: list[Chat] = []

esperando_noticias = False

def cria_botoes():
    # Cria o teclado com 7 botões para o usuário escolher

    botoes = InlineKeyboardMarkup()
    
    botoes.add(
    InlineKeyboardButton("🌎 Como está o dia", callback_data="como_esta_o_dia")
    )
    
    botoes.add(
    InlineKeyboardButton("📚 Educação", callback_data="educacao"),
    InlineKeyboardButton("🎥 Entretenimento", callback_data="entretenimento")
    )
    
    botoes.add(
    InlineKeyboardButton("⚽ Esportes", callback_data="esporte"),
    InlineKeyboardButton("🌱 Meio Ambiente", callback_data="meio_ambiente")
    )
    
    botoes.add(
    InlineKeyboardButton("💊 Saúde", callback_data="saude"),
    InlineKeyboardButton("🏛️ Política", callback_data="politica")
    )

    return botoes

def dicionarios(opcao):
    # Dicionários que associas as opções ao título da notícia e aos emojis
    
    opcoes_resumo = {
        "como_esta_o_dia": "do dia",
        "educacao": "sobre educação",
        "entretenimento": "sobre entretenimento",
        "esporte": "sobre esportes",
        "meio_ambiente": "sobre meio ambiente",
        "saude": "sobre saúde",
        "politica": "sobre política"
    }

    opcoes_emojis = {
        "como_esta_o_dia": "🌎",
        "educacao": "📚",
        "entretenimento": "🎥",
        "esporte": "⚽",
        "meio_ambiente": "🌱",
        "saude": "💊",
        "politica": "🏛️"
    }

    return opcoes_resumo.get(opcao), opcoes_emojis.get(opcao)

if __name__ == "__main__":
    load_dotenv()

    chave_telegram = os.getenv("chave_telegram")
    botNews = telebot.TeleBot(chave_telegram)

    # Identifica o chat atual
    def get_chat(chat_id: int) -> Chat or None:
        for chat in chats:
            if chat.chat_id == chat_id:
                return chat
        return None

    # Manda mensagem inicial com o teclado de botões
    @botNews.message_handler(commands=["start"])
    def bem_vindo(message):
        novo_chat = Chat(message.chat.id)
        chats.append(novo_chat)
        
        texto_bem_vindo = (
            "*Espresso News* ☕📰\n\n"
            "Eu sou um bot e faço os melhores resumos de notícias para você!\n\n"
            "↪️ Se você quer um resumo de tudo que tá rolando, é só clicar em '🌎 Como está o dia'.\n\n"
            "↪️ Quer algo mais específico? É só escolher o assunto que te interessa e eu trago as novidades pra você!\n\n"
            "💡 Divirta-se se informando!"
        )
        
        # Enviando a mensagem com os botões
        botNews.send_message(message.chat.id, texto_bem_vindo, reply_markup=cria_botoes(), parse_mode='Markdown')
        
        
    # Retorna as notícias de acordo com a opção escolhida
    @botNews.callback_query_handler(func=lambda call: True)
    def noticias(call):
        chat = get_chat(call.message.chat.id)

        if chat is None:
            botNews.reply_to(
            call.message, "Você não iniciou o chat comigo. Digite /start para começar."
            )
            return
        
        resumo_maritaca = "..."

        # Enviando uma resposta ao clicar no botão
        opcoes = dicionarios(call.data)

        if opcoes is not None:
            resumo = f"{opcoes[1]} *Resumo das principais notícias {opcoes[0]}:* \n\n {resumo_maritaca}"
            botNews.send_message(call.message.chat.id, resumo, parse_mode='Markdown')


        botNews.answer_callback_query(call.id)
        botNews.send_message(call.message.chat.id, 
                            "🔁 Escolha outro assunto ou veja o resumo do dia novamente:", 
                            reply_markup=cria_botoes())


    botNews.infinity_polling()
