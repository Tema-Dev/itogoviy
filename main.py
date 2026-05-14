import telebot


bot = telebot.TeleBot('8855911885:AAFbmfogMOaRQMRfXVxRnQsAVJRGdf7HgBA')


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
                 'Loading… [][][][][][][][][][] 0%\n'
                 'Loading… ██[][][][][][][][] 25%\n'
                 'Loading… █████[][][][][] 50%\n'
                 'Loading… ███████[][][] 75%\n'
                 'Loading… ██████████] 99%\n'
                 'Loading… ███████████ 100%'
                 )
    bot.reply_to(message, '🔥 Привет! Напиши мне любую игру на которую тебе нужна скидочка, я тебе пришлю сайт и там ты её найдёшь! Чтобы сразу перейти в стим или что то типо такого то напиши мне Steam или Green Man Gaming')


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, '⚠️ Помощь. Если бот завис, отправьте команду /start повторно.')
    bot.reply_to(message, '⚠️Если не работают запросы то пиши ему только с БОЛЬШОЙ буквы или переустанови бота')


@bot.message_handler(commands=['about'])
def about(message):
    bot.reply_to(message, '📃 Бот создан для итогового проекта. Перенаправляет на сайт CheapShark.')


@bot.message_handler(commands=['site'])
def send_website(message):
    text = (
        f"🔍 Ищите скидки на игру **{message.text}** на официальном сайте CheapShark!\n\n"
        f"🔗 Ссылка: [CheapShark](https://cheapshark.com)"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(commands=['Steam'])
def send_website1(message):
    text = (
        f"🔍 Ищите скидки на игру **{message.text}** на официальном сайте CheapShark!\n\n"
        f"🔗 Ссылка: [Steam](https://store.steampowered.com/)"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")




bot.polling(none_stop=True)