from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Cria o teclado com botões
def create_buttons():
    buttons = InlineKeyboardMarkup()

    buttons.row(
        InlineKeyboardButton("🌎 Como está o dia", callback_data="como_esta_o_dia"),
    )

    buttons.row(    
        InlineKeyboardButton("📚 Educação", callback_data="educacao"),
        InlineKeyboardButton("🌱 Meio Ambiente", callback_data="meio_ambiente"),
    )

    buttons.row(    
        InlineKeyboardButton("⚽ Esportes", callback_data="esporte"),
        InlineKeyboardButton("💸 Economia", callback_data="economia"),
    )

    buttons.row(
        InlineKeyboardButton("💊 Saúde", callback_data="saude"),
        InlineKeyboardButton("🏛️ Política", callback_data="politica")
    )

    return buttons

# Dicionário de categorias e emojis
def dicts(opt):
    categories = {
        "como_esta_o_dia": "do dia",
        "educacao": "sobre educação",
        "meio_ambiente": "sobre o meio ambiente",
        "esporte": "sobre esportes",
        "economia": "sobre economia",
        "saude": "sobre saúde",
        "politica": "sobre política"
    }
    emojis = {
        "como_esta_o_dia": "🌎",
        "educacao": "📚",
        "meio_ambiente": "🌱",
        "esporte": "⚽",
        "economia": "💸",
        "saude": "💊",
        "politica": "🏛️"
    }
    return categories.get(opt), emojis.get(opt)

# Função para verificar se o chat foi iniciado
def check_chat_started(chat, message, bot):
    if chat is None:
        bot.reply_to(message, "Você não iniciou o chat comigo. Digite /start para começar.")
        return False
    return True

# Função para processar as respostas
def handle_summary(bot, call, chat, maritaca, news):
    request = dicts(call.data)

    bot.answer_callback_query(call.id)

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Resumindo as notícias do dia...", callback_data="processing"))

    # Edita a mensagem atual, removendo os botões
    bot.edit_message_reply_markup(chat.id, call.message.message_id, reply_markup=markup)
    summary = 'teste'

    if call.data == 'como_esta_o_dia': 
        summary = maritaca.run(news.get_top_headlines())
    elif request != None:
        summary = maritaca.filter(call.data, news.get_articles())


    # Edita a mensagem atual, removendo o botão clicável
    bot.edit_message_reply_markup(chat.id, call.message.message_id, reply_markup=None)


    bot.send_message(chat.id,
                     f"{request[1]} *Resumo das principais notícias {request[0]}:* \n\n {summary}",
                     parse_mode='Markdown')

    bot.send_message(chat.id, 
                    "🔁 Escolha outro assunto ou veja o resumo do dia novamente:", 
                    reply_markup=create_buttons())
