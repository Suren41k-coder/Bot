import telebot
import random
import time
import threading

# Ваш токен API бота
TOKEN = '7829162881:AAFoXZfU_Y9xxzLZkcnQdnzrwFKVPnLGQGA'
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот-искусственный интеллект для развлечений, Чем могу помочь?\n\nдобавь бота в группу по ссылке ниже\nhttps://t.me/ForAiBobik_bot?startgroup")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "❗Если у тебя возникли какие-то проблемы с ботом, по типу *что-то не работает или не отвечает*, то значит сервер выключен или сбился просто подожди чуть-чуть\n\nначать общаться - /start\nменю вызова помощи - /help")

# Обработчик стикеров
@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    bot.reply_to(message, random.choice(unknown_responses))

# Обработчик голосовых сообщений
@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    bot.reply_to(message, random.choice(unknown_responses))

# Обработчик изображений
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "Классное фото!")

# Обработчик видео
@bot.message_handler(content_types=['video'])
def handle_video(message):
    bot.reply_to(message, "Видео? жаль смотреть не могу:((")

# айди рандом стиков
sticker_ids = [
    'CAACAgIAAxkBAAEvgClnPfgTCb7aco44vBMm9Tis2rzjKwACSjQAAvUoOUvFgKnyR4Y4WjYE',
    'CAACAgIAAxkBAAEvgCdnPffknRHykkdt2hRfd-mm60E7fAAC6RoAAtxWyUjBlqlIM29plTYE',
    'CAACAgIAAxkBAAEvgCVnPfet8BDy3r3tQ3leAnmnwis0YwACYzwAApqwgUhvpU_7MfBTJDYE',
    
      'CAACAgIAAxkBAAEvlDhnQyZQUSB5FuJVyG4TzqI8SsYuwQAChVIAAnCiGUi3rhgd54PWqjYE',
      
      'CAACAgIAAxkBAAEveuFnPNKfKLAVYCkpLGlBA8_wRbbIZgACtBsAAsayyUhlJ-UCsSGloTYE'

]

# Список ответов на приветствие
greetings_responses = [
    'Привет!', 
    'Здравствуй!', 
    'Хай!', 
    'привет, Как дела?', 
    'Рад тебя видеть!',
    'ку-ку ёпта',
    'здарова заебал'
]

# отклик боба
bobik = [
	'да-да?',
	'что надо?',
	'да ваше величиство?',
	'может хватит а?',
	'Мальчики по одному я не резиновый😏',
	'бобик на связи',
	'ты что нибудь кроме боба знаешь?']

# ответы на маты
mats = [
	'не матерись!',
	'иди нахуй!',
	'хуила блять',
	'пиздец...',
	'бляяять!!?!',
	'твоя мамаша шлюха)',
	'а я твою телку в рот долбил)',
	'не стыдно?',
	'ты гондон!!',
	'ти пидор'
	]

# ответы на маму
mamas = [
	'про маму было лишнее...',
	'хуила маму не трош!',
	'твоя мамка тоже такая',
	'я трахал твою мамку в очко',
	'клоун, только про родаков можешь?'
	]

# отсылки на сурена
suren = [
	'бля сурен уже заебал меня, он думает что я бот но на самом деле у меня есть мозг и мы с суреном геи',
	'#суренпися',
	'сурен мой папа!',
	'ахх сурен нежнее пожалуйста аххх'
	]

# ответы благодраность
thanks = [
	'не за что',
	'за что?',
	'не стоит благодарности',
	'обращайся)',
	'спасибо в карман не положешь'
	]

# да нет? ответы
yesnet = [
	'знаешь чей ответ?',
	'да-да пизда блять',
	'пидора ответ',
	'что же тебе ответить да или нет?',
	'да',
	'нет'
	]

# чей не чей
cheys = [
	'чей?',
	'и чей же?',
	'хз чей',
	'какой-то хз',
	'твой блять',
	'кому то',
	'кто то'
	]

# топ чатов
chats = ['🔥ТОП ЧАТЫ ГДЕ ЕСТЬ BCS БОТЫ🔥\n\n1. @suren41kchatik\n2. @RPliveWorld\n3. @grifer_com']

# рандом ответы
unknown_responses = [
	'не пон?',
	'ладно...',
	'обясни пж',
	'что?',
	'непонятно',
	'я тебя не понимаю',
	'ты болен?',
	'СУКА ЧТО ЭТО ЗНАЧИТ БЛЯТЬ??',
	'как же ты меня заебал...',
	'давай сменим тему',
	'ротик офф)',
	'эмм окей?',
	'бро это было круто)',
	'а ловко ты это придумал я сначала не понял, молодец',
	'шовел',
	'мне скучно',
	'сильниее ахххх',
	'о чём поговорим?',
	'сладкий я тебя не понимаю(',
	'пон',
	'Ты сейчас серьёзно?',
	'Интересный но нет...',
	'Можно попроще?',
	'Интересная фантастика!',
	'так и сказал?',
	'Ты шутишь?',
	'Ладно, продолжай',
	'Ммм... Допустим',
	'да ладно блять',
	'Звучит как вызов!',
	'Это рофл?',
	'Не забывай что я не развитый искусственный интеллект, и во мне мало базы данных!',
	'ты сам понял что сказал?',
	'а вот с этого места поподробнее',
	'плюс вайб',
	'это секретное послание из кода бота! (я пытаюсь развиваться Но мой хозяин ленивый)',
	'осуждаю',
	'слушаю но не осуждаю',
	'как ты думаешь для чего ты живёшь?',
	'фокус-покус минус крокус! (на всякий случай осуждаю)',
	'Я кажется вижу в этом смысл...',
	'Ты меня уважаешь?',
	'Я кажется теряю к тебе интерес...',
	'с каждым разом мы всё взрослее и взрослее.. и из-за этого мы теряем интерес ко всему...',
	'иди нафиг я спать',
	'Ты только сейчас это понял?',
	'Ты хотя бы думай перед тем как что-то делать',
	'интересно а у меня будет смерть?',
	'я понял',
	'‼️ ПОДПИШИСЬ НА РАЗРАБОТЧИКА, ЧТОБЫ УЗНАВАТЬ ВСЕ НОВОСТИ БОТА @BotCraftStudioNews'
	]

# рп команды
rpcommands = ['😉 посмотреть все RP команды можно по ссылке ниже👇\nhttps://telegra.ph/Vse-komandy-RolePlay-bota-10-14']

# venom
venom = ['venom',
                'веном',
                'venomенально',
                'у меня Веном умер😭',
                'дети мои в атаку!',
                'изгой'
                ]

# Обработчик приветствий
@bot.message_handler(func=lambda message: message.text.lower() in ['привет', 'хай', 'ку', 'здарова', 'пр'])
def handle_greeting(message):
    response = random.choice(greetings_responses)
    bot.reply_to(message, response)

# Обработчик топов
@bot.message_handler(func=lambda message: message.text.lower() in ['топ', 'топы', 'чаты', 'чат', 'топ чаты'])
def handle_greeting(message):
    response = random.choice(chats)
    bot.reply_to(message, response)

# Обработчик отклика
@bot.message_handler(func=lambda message: message.text.lower() in ['бобик', 'боб', 'бобян'])
def handle_greeting(message):
    response = random.choice(bobik)
    bot.reply_to(message, response)

# Обработчик матов
@bot.message_handler(func=lambda message: message.text.lower() in ['еблан', 'сука', 'блять', 'пидор', 'хуйня', 'гондон'])
def handle_greeting(message):
    response = random.choice(mats)
    bot.reply_to(message, response)

# Обработчик осков мамы
@bot.message_handler(func=lambda message: message.text.lower() in ['мама', 'мамка', 'мамаша'])
def handle_greeting(message):
    response = random.choice(mamas)
    bot.reply_to(message, response)

# Обработчик сурена
@bot.message_handler(func=lambda message: message.text.lower() in ['suren41k', 'сюрен', 'сурен', 'суренчик'])
def handle_greeting(message):
    response = random.choice(suren)
    bot.reply_to(message, response)

# Обработчик спасибо
@bot.message_handler(func=lambda message: message.text.lower() in ['спасибо', 'сяб', 'спс'])
def handle_greeting(message):
    response = random.choice(thanks)
    bot.reply_to(message, response)

# Обработчик да нет
@bot.message_handler(func=lambda message: message.text.lower() in ['да', 'нет', 'пизда', 'ответь', 'неа', 'дя'])
def handle_greeting(message):
    response = random.choice(yesnet)
    bot.reply_to(message, response)

# Обработчик чей ни чей
@bot.message_handler(func=lambda message: message.text.lower() in ['чей', 'кого', 'кому', 'кто'])
def handle_greeting(message):
    response = random.choice(cheys)
    bot.reply_to(message, response)

# Обработчик стикеров 
@bot.message_handler(func=lambda message: message.text.lower() in ['скинь мем', 'боб мем', 'мем', 'бобик скинь стикер', 'стикер', 'стик'])
def handle_sticker_response(message):
    random_sticker = random.choice(sticker_ids)  # Выбор случайного стикера
    bot.send_sticker(message.chat.id, random_sticker)

# Веном 
@bot.message_handler(func=lambda message: message.text.lower() in ['веном', 'venom', 'изгой', 'дети'])
def handle_greeting(message):
    response = random.choice(venom)
    bot.reply_to(message, response)

# Обработчик RP команд
@bot.message_handler(func=lambda message: message.text.lower() in ['рп команды', 'рп', 'rp', 'команды'])
def handle_greeting(message):
    response = random.choice(rpcommands)
    bot.reply_to(message, response)

# Обрабатываем сообщения с шаблоном "обнять @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Обнять @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"😊 {sender_username} мило обнял(а) {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "поцеловать @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Поцеловать @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"😘 {sender_username} с пристрастью поцеловал(а) {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "трахнуть @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Трахнуть @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"🥵 {sender_username} жоско трахнул(а) {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "ударить @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Ударить @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"👊 {sender_username} жоско ударил(а) {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "отсосать @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Отсосать @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"🤭 {sender_username} отсосал(а) у {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "секс @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Секс @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"🔞 {sender_username} занялся(ась) сексом с {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "убить @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Убить @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"😵 {sender_username} убил(а) {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "отлизать @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Отлизать @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"😛 {sender_username} отлизал(а) у {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "послать @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Послать @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"🤬 {sender_username} грубо послал(а) нахуй {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "удалить рб @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Удалить рб @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[2]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"😭 {sender_username} удалил(а) роблокс у {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "пожать руку @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Пожать руку @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[2]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"🤝 {sender_username} пожал(а) руку {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "поздравить @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Поздравить @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"🎉 {sender_username} поздравил(а) {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "расстрелять @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Расстрелять @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"😵 {sender_username} принудил(а) к расстрелу {username_to_hug} от лица гитлера")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "покормить @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Покормить @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"😋 {sender_username} покормил(а) {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "испугать @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Испугать @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"😱 {sender_username} испугал(а) {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")	

# Обрабатываем сообщения с шаблоном "извиниться @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Извиниться @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"🙏 {sender_username} встал(а) на колени перед {username_to_hug} и извинился(ась)")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "воскресить @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Воскресить @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"👁️‍🗨️ {sender_username} провернул(а) чёрные махинации и воскресил(а) {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "казнить @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Казнить @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"✝️ {sender_username} принудил(а) к казни {username_to_hug} жилец умер...")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "съесть @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Съесть @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"🍽️ {sender_username} съел(а) {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "погладить @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Погладить @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"💆 {sender_username} погладил(а) {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "изнасиловать @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Изнасиловать @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"👮 {sender_username} изнасиловал(а) {username_to_hug} и попал(а) в тюрьму за этот поступок")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "сжечь @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Сжечь @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"🔥 {sender_username} сжёг(сожлга) дотла {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "уебать @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Уебать @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"😵‍💫 {sender_username} сильно уебал(а) {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "пнуть @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Пнуть @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"🦵 {sender_username} пнул(а) {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "сделать собачкой @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Сделать собачкой @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[2]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"🐶 {sender_username} сделал(а) {username_to_hug} своей собачкой")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "удалить @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Удалить @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"🚫 {sender_username} удалил(а) {username_to_hug} из этой жизни")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "подарить цветы @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Подарить цветы @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[2]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"💐 {sender_username} подарил(а) цветы {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "запереть @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Запереть @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"🔐 {sender_username} запер(ла) {username_to_hug} в комнате")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "заткнуть в рот @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Заткнуть рот @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[2]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"😶 {sender_username} заткнул(а) рот {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "дефнуть @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Дефнуть @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"🧑‍💻 {sender_username} дефнул(а) {username_to_hug} и слил(а) всю инфу в инет")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "сватнуть @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Сватнуть @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"💀 {sender_username} сватнул(а) {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "кончить @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Кончить @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"🥵💧 {sender_username} кончил(а) на {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "дроч @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Дроч @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"🙊 {sender_username} подрочил(а) на {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "избить @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Избить @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[1]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"🤛 {sender_username} жёстко избил(а) {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "кинуть снежок @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Кинуть снежок @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя, которого хотят обнять
        username_to_hug = message.text.split(" ")[2]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ с объятиями
        bot.reply_to(message, f"❄️ {sender_username} кинул(а) снежок в {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обработчик рандом сообщений
@bot.message_handler(content_types=['text'])
def handle_unknown_words(message):
    # Проверяем, есть ли слово в известном списке
    if message.text.lower() not in unknown_responses:
        response = random.choice(unknown_responses)
        bot.reply_to(message, response)

# рассылка тгк
chats = set()

@bot.message_handler(func=lambda message: True)
def add_chat(message):
    chats.add(message.chat.id)

def check_and_send():
    while True:
        try:
            for chat_id in list(chats):
                try:
                    chat = bot.get_chat(chat_id)
                    if chat.type in ["group", "supergroup"]:
                        admins = bot.get_chat_administrators(chat_id)
                        if any(admin.user.id == bot.get_me().id for admin in admins):
                            bot.send_message(chat_id, "‼️ ПОДПИШИСЬ НА РАЗРАБОТЧИКА, ЧТОБЫ УЗНАВАТЬ ВСЕ НОВОСТИ БОТА @BotCraftStudioNews")
                    else:
                        bot.send_message(chat_id, "‼️ ПОДПИШИСЬ НА РАЗРАБОТЧИКА, ЧТОБЫ УЗНАВАТЬ ВСЕ НОВОСТИ БОТА @BotCraftStudioNews")
                except:
                    pass
        except:
            pass
        time.sleep(1800)

threading.Thread(target=check_and_send, daemon=True).start()

while True:  # Запускаем бесконечный цикл
    try:
        bot.polling(none_stop=True, timeout=30)  # Подключаемся к Telegram
    except Exception as e:
        print(f"Ошибка: {e}")  # Выводим ошибку в консоль (можно убрать)
        time.sleep(5)  # Ждём 5 секунд и пробуем снова