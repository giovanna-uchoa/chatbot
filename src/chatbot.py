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

    bot.answer_callback_query(call.id, text="Resumindo as notícias do dia...")

    if call.data == 'como_esta_o_dia': 
        summary = maritaca.run(news.get_top_headlines())
    else:
        summary = maritaca.filter(call.data, news.get_articles())

    bot.send_message(chat.id,
                     f"{request[1]} *Resumo das principais notícias {request[0]}:* \n\n {summary}",
                     parse_mode='Markdown')

    bot.answer_callback_query(call.id)
    bot.send_message(chat.id, 
                    "🔁 Escolha outro assunto ou veja o resumo do dia novamente:", 
                    reply_markup=create_buttons())
