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
    bot.reply_to(message, '🔥 Привет! Напиши мне любую игру на которую тебе нужна скидочка, я тебе пришлю сайт и там ты её найдёшь(пиши типо вот так: FC26 Игра)! Чтобы сразу перейти в стим или что то типо такого то напиши мне Steam или Green Man Gaming')
    bot.reply_to(message, 'Кстати, вот мой список моих команд:\n'
                        '/start = Открывает этот бот\n',
                        '/help = Если есть какие то неполадки\n',
                        '/about = О боте(зачем он создан)\n',
                        '/sendwebsite = Скидывает сайт CheapShark\n',
                        '[имя вашей игры и в конце Игра] = Скидывает сайт CheapShark там где есть ваша игра(если скидка ещё не удалена)\n',
                        '/Steam = Открывает Steam\n',
                        '/TheHumbleStore = Открывает TheHumbleStore\n',
                        '/GreenManGaming = Открывает GreenManGaming\n',
                        '/GameBillet = Открывает GameBillet\n',
                        '/FANATICAL = Открывает FANATICAL\n',
                        '/Gog.com = Открывает Gog.com\n',
                        '/WinGameStore = Открывает WinGameStore\n',
                        '/GamersGate = Открывает GamersGate\n',
                        '/GamesPlanet = Открывает GamesPlanet\n')


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, '⚠️ Помощь. Если бот завис, отправьте команду /start повторно или переустановите его.')
    bot.reply_to(message, '⚠️Если не работают запросы то пиши ему только с ЗАГЛАВНОЙ буквы или переустанови бота')


@bot.message_handler(commands=['about'])
def about(message):
    bot.reply_to(message, '📃 Бот создан для итогового проекта. Перенаправляет на сайт CheapShark и ищет ваши игры.')


@bot.message_handler(commands=['send_website'])
def send_website(message):
    if 'сайт' or 'Сайт' in message.text:
        text1 = (
            f"🔍 Ищите скидки на игру на официальном сайте CheapShark!\n\n"
            f"🔗 Ссылка: [CheapShark](https://cheapshark.com)"
        )
        bot.send_message(message.chat.id, text1, parse_mode="Markdown")
    elif 'игра' or 'Игра':
        text = (
            f"🔍 Ищите скидки на игру **{message.text}** на официальном сайте CheapShark!\n\n"
            f"🔗 Ссылка: [CheapShark](https://cheapshark.com)"
    )
        bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(commands=['Steam'])
def Steam(message):
    if 'Steam' or 'стим' or 'steam' or 'Стим' in message.text:
        text2 = (
            f"🔍 Ваш Steam для поиска игр\n\n"
            f"🔗 Ссылка: [Steam](https://store.steampowered.com/)"
        )
        bot.send_message(message.chat.id, text2, parse_mode="Markdown")

@bot.message_handler(commands=['TheHumbleStore'])
def TheHumbleStore(message):
    text2 = (
            f"🔍 Ваш Steam для поиска игр\n\n"
            f"🔗 Ссылка: [TheHumbleStore](https://www.humblebundle.com/store?irclickid=xwp0EK1hDxyZUxIVHCV1%3AWMtUkuRSnXobSyfV00&sharedid=&irpid=2490816&utm_source=impact&utm_medium=paid&utm_campaign=CheapShark&utm_content=2490816&utm_term=Online%20Tracking%20Link&irgwc=1&afsrc=1)"
        )
    bot.send_message(message.chat.id, text2, parse_mode="Markdown")

@bot.message_handler(commands=['GreenManGaming'])
def GreenManGaming(message):
    text2 = (
            f"🔍 Ваш Steam для поиска игр\n\n"
            f"🔗 Ссылка: [GreenManGaming](https://www.greenmangaming.com/?utm_source=CheapShark&utm_medium=affiliate&utm_campaign=impact&utm_content=1281797&irclickid=xwp0EK1hDxyZUxIVHCV1%3AWMtUkuRSi0kbSyfV00&irgwc=1&afsrc=1)"
        )
    bot.send_message(message.chat.id, text2, parse_mode="Markdown")

@bot.message_handler(commands=['GameBillet'])
def GameBillet(message):
    text2 = (
            f"🔍 Ваш Steam для поиска игр\n\n"
            f"🔗 Ссылка: [GameBillet](https://www.gamebillet.com/?affiliate=25d1c8e9-dbfe-460a-9891-99d76b7af2e5)"
        )
    bot.send_message(message.chat.id, text2, parse_mode="Markdown")

@bot.message_handler(commands=['FANATICAL'])
def FANATICAL(message):
    text2 = (
            f"🔍 Ваш Steam для поиска игр\n\n"
            f"🔗 Ссылка: [FANATICAL](https://www.fanatical.com/en/?utm_source=awin&utm_medium=affiliate&utm_campaign=278415&utm_publisherID=278415&utm_publisherurl=www.cheapshark.com&utm_promotiontype=Comparison+Engine&sv1=affiliate&sv_campaign_id=278415&awc=118821_1779288610_29963aa739886553275618cdec85efac)"
        )
    bot.send_message(message.chat.id, text2, parse_mode="Markdown")

@bot.message_handler(commands=['GamesPlanet'])
def GamesPlanet(message):
    text2 = (
            f"🔍 Ваш Steam для поиска игр\n\n"
            f"🔗 Ссылка: [GamesPlanet](https://us.gamesplanet.com/?ref=cheapshark)"
        )
    bot.send_message(message.chat.id, text2, parse_mode="Markdown")

@bot.message_handler(commands=['WinGameStore'])
def WinGameStore(message):
    text2 = (
            f"🔍 Ваш Steam для поиска игр\n\n"
            f"🔗 Ссылка: [WinGameStore](https://www.wingamestore.com/)"
        )
    bot.send_message(message.chat.id, text2, parse_mode="Markdown")

@bot.message_handler(commands=['GamersGate'])
def GamersGate(message):
    text2 = (
            f"🔍 Ваш Steam для поиска игр\n\n"
            f"🔗 Ссылка: [GamersGate](https://www.gamersgate.com/?caff=2088091&aff=cj&cjevent=9e71f25b545b11f181d300a90a18b8fb&pk_campaign=CheapShark&pk_source=cj&cja=11554588-5715555-)"
        )
    bot.send_message(message.chat.id, text2, parse_mode="Markdown")

@bot.message_handler(commands=['Gog.com'])
def Gog(message):
    text2 = (
            f"🔍 Ваш Steam для поиска игр\n\n"
            f"🔗 Ссылка: [Gog.com](https://www.gog.com/?utm_campaign=cj&utm_medium=affiliate&utm_source=cj&r=true)"
        )
    bot.send_message(message.chat.id, text2, parse_mode="Markdown")

bot.polling()