import telebot
from telebot import types
import random
import uuid
from datetime import datetime, timedelta
import time

API_TOKEN = '7361993582:AAFTk5xdf9M74PuWCeNrOhPw7n8cXbyGEJY'
bot = telebot.TeleBot(API_TOKEN)

# Хранение данных о пользователях
users_data = {}

@bot.message_handler(func=lambda message: message.text == 'Пригласить друга')
def invite_friend(message):
    user_id = message.from_user.id
    current_time = datetime.now()

    if user_id not in users_data:
        bot.send_message(message.chat.id, "⚒️ Сначала создайте свою шахту, чтобы создать шахту напишите шахта")
        return
    
    if 'referrals' not in users_data[user_id]:
        users_data[user_id]['referrals'] = []
    if 'used_referrals' not in users_data[user_id]:
        users_data[user_id]['used_referrals'] = []
    if 'last_referral_time' not in users_data[user_id]:
        users_data[user_id]['last_referral_time'] = None

    last_referral_time = users_data[user_id]['last_referral_time']

    if last_referral_time is not None and current_time - last_referral_time < timedelta(days=1):
        remaining_time = timedelta(days=1) - (current_time - last_referral_time)
        bot.send_message(message.chat.id, f"⏳ Вы сможете создать новую реферальную ссылку через {remaining_time}.")
        return
    
    referral_id = str(uuid.uuid4())  # Генерация уникального реферального ID
    referral_link = f"https://t.me/{bot.get_me().username}?start={referral_id}"
    
    users_data[user_id]['referrals'].append(referral_id)
    users_data[user_id]['last_referral_time'] = current_time
    
    bot.send_message(message.chat.id, f"🙋 Пригласите друга с помощью этой ссылки:\n{referral_link}\n\nКогда ваш друг перейдет по этой ссылке, вы получите 15,000 руды! 💎")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username
    args = message.text.split()

    # Создаем запись для пользователя, если ее еще нет
    if user_id not in users_data:
        users_data[user_id] = {
            'username': username,
            'mine_count': 100,  # Начальное количество руды
            'items': [],
            'referrals': [],
            'used_referrals': [],
            'last_referral_time': None
        }

    # Проверяем, является ли аргумент реферальным кодом
    if len(args) > 1:
        referral_id = args[1]
        for referrer_id, referrer_data in users_data.items():
            if referral_id in referrer_data.get('referrals', []) and referral_id not in referrer_data.get('used_referrals', []):
                referrer_data['mine_count'] += 15000  # Награждаем пользователя, который пригласил
                referrer_data['used_referrals'].append(referral_id)
                bot.send_message(referrer_id, f"🎉 Ваш друг присоединился! Вы получили 15,000 руды! 💎")
                break

    bot.send_message(message.chat.id, "Привет я VRT👋\nЯ игровой бот🕹️\nЧтобы узнать как играть перейди по ссылке ниже⚒️\ntelegra.ph/INSTRUKCIYA-PO-ISPOLZOVANIYU---VRT-08-12\n\n📑официальный канал - @VRT_dev",)

# обработка команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    username = message.from_user.first_name  # Получаем имя пользователя
    bot.send_message(
        message.chat.id, 
        f"ℹ️ {username}, если у вас возникла какая-то ошибка по боте, то обратитесь в техподдержку👇\n"
        f"t.me/ManagerBCS\n\n"
        f"🧩 Если вам нужна инструкция по боту, то воспользуйтесь командой команды\n\n"
        f"😔 Если бот снова не работает, значит ведутся технические работы или бот в отключке\n\n"
        f"P.s команда VRT надеемся, что чем-то помогли вам☺️\n\n📑официальный канал - @VRT_dev"
    )

# Обработка нажатия кнопки "ШАХТА"
@bot.message_handler(func=lambda message: message.text == 'Шахта')
def send_mine_info(message):
    user_id = message.from_user.id
    if user_id not in users_data:
        users_data[user_id] = {'username': message.from_user.username, 'mine_count': 0, 'items': []}
    
    user_info = users_data[user_id]
    bot.send_message(message.chat.id, f"⚒️ @{user_info['username']} это твоя шахта\n\n❓Чтобы начать копать руду напиши команду /dig_mine\n\n♻️Всего скопано руды - {user_info['mine_count']}")

# Команда /dig_mine
@bot.message_handler(commands=['dig_mine'])
def dig_mine(message):
    user_id = message.from_user.id
    if user_id in users_data:
        mined_amount = random.randint(1, 100)
        users_data[user_id]['mine_count'] += mined_amount
        mine_count = users_data[user_id]['mine_count']
        bot.send_message(message.chat.id, f"⚒️Вы вскопали {mined_amount}/100 руды\n♻️Всего скопано руды - {mine_count}")
    else:
        bot.send_message(message.chat.id, "⚒️ Сначала создайте свою шахту, чтобы создать шахту напишите шахта")

# Обработка нажатия кнопки "КЕЙСЫ"
@bot.message_handler(func=lambda message: message.text == 'Открыть кейс')
def open_case(message):
    user_id = message.from_user.id

    if user_id not in users_data:
        bot.send_message(message.chat.id, "⚒️ Сначала создайте свою шахту, чтобы создать шахту напишите шахта")
        return

    current_time = datetime.now()
    last_case_time = users_data[user_id].get('last_case_time')

    # Проверка времени последнего открытия кейса
    if last_case_time and current_time - last_case_time < timedelta(minutes=1):
        remaining_time = timedelta(minutes=1) - (current_time - last_case_time)
        bot.send_message(message.chat.id, f"⏳ Вы сможете открыть следующий кейс через {remaining_time.seconds} секунд.")
        return

    # Обновление времени последнего открытия кейса
    users_data[user_id]['last_case_time'] = current_time

    # Вычисление выигранной руды
    received_ore = random.randint(2, 200)  # Увеличение выигрыша в 2 раза
    users_data[user_id]['mine_count'] += received_ore
    mine_count = users_data[user_id]['mine_count']

    # Отправка сообщения с результатом
    bot.send_message(message.chat.id, f"📦 Вы открыли кейс и получили {received_ore} руды! 💎\n♻️ Всего скопано руды - {mine_count}")

# Обработка нажатия кнопки "ПРОФИЛЬ"
@bot.message_handler(func=lambda message: message.text == 'Профиль')
def view_profile(message):
    user_id = message.from_user.id

    if user_id not in users_data:
        bot.send_message(message.chat.id, "⚒️ Сначала создайте свою шахту, чтобы создать шахту напишите шахта")
        return

    user_info = users_data[user_id]
    items_list = '\n'.join(user_info['items']) if user_info['items'] else 'Нет предметов'

    bot.send_message(message.chat.id, f"👤 Профиль @{user_info['username']}:\n\n💎 Всего скопано руды: {user_info['mine_count']}\n🛍️ Купленные предметы:\n{items_list}")

# Примерный список предметов магазина
shop_items = {
    '🚗 Машина': 5000,
    '🏡 Дом': 20000,
    '🛳️ Яхта': 10000,
    '✈️ Самолет': 30000,
    '🏍️ Мотоцикл': 8000
}

# Обработка нажатия кнопки "МАГАЗИН"
@bot.message_handler(func=lambda message: message.text == 'Магазин')
def open_shop(message):
    markup = types.InlineKeyboardMarkup()
    for item, price in shop_items.items():
        markup.add(types.InlineKeyboardButton(text=f"{item} - {price} руды", callback_data=item))
    bot.send_message(message.chat.id, "🛍️ Добро пожаловать в магазин! Выберите предмет для покупки:", reply_markup=markup)

# Обработка покупок из магазина
@bot.callback_query_handler(func=lambda call: call.data in shop_items)
def handle_purchase(call):
    user_id = call.from_user.id
    item = call.data
    price = shop_items[item]

    if user_id in users_data:
        user_info = users_data[user_id]
        if user_info['mine_count'] >= price:
            user_info['mine_count'] -= price
            user_info['items'].append(item)
            bot.send_message(call.message.chat.id, f"🎉 Поздравляем! Вы успешно купили {item}!\n💎 Остаток руды: {user_info['mine_count']}")
        else:
            bot.send_message(call.message.chat.id, "🚫 К сожалению, у вас недостаточно руды для покупки этого предмета.")
    else:
        bot.send_message(call.message.chat.id, "⚒️ Сначала создайте свою шахту, чтобы создать шахту напишите шахта")

# Обработка нажатия кнопки "БОИ"
@bot.message_handler(func=lambda message: message.text == 'Начать бой')
def start_fight(message):
    user_id = message.from_user.id
    if user_id not in users_data:
        users_data[user_id] = {'username': message.from_user.username, 'mine_count': 0, 'items': []}

    # Атака происходит сразу
    success = random.choice([True, False])
    if success:
        mined_amount = random.randint(1, 100)
        users_data[user_id]['mine_count'] += mined_amount
        bot.send_message(message.chat.id, f"🗡️ Вы попали! Вы получили {mined_amount} руды.\n♻️ Всего скопано руды: {users_data[user_id]['mine_count']}")
    else:
        lost_amount = random.randint(1, 100)
        users_data[user_id]['mine_count'] -= lost_amount
        if users_data[user_id]['mine_count'] < 0:
            users_data[user_id]['mine_count'] = 0
        bot.send_message(message.chat.id, f"🛡️ Вы промахнулись! Вы потеряли {lost_amount} руды.\n♻️ Всего скопано руды: {users_data[user_id]['mine_count']}")

# Обработка нажатия кнопки "КАЗИНО"
@bot.message_handler(func=lambda message: message.text == 'Казино')
def start_casino(message):
    user_id = message.from_user.id
    if user_id not in users_data:
        users_data[user_id] = {'username': message.from_user.username, 'mine_count': 0, 'items': []}

    if users_data[user_id]['mine_count'] < 250:
        bot.send_message(message.chat.id, "❌У вас недостаточно руды для ставки. Нужно минимум 250 руды.")
    else:
        users_data[user_id]['mine_count'] -= 250
        outcome = random.choice(['win', 'lose'])
        if outcome == 'win':
            prize = random.randint(1, 1000)
            users_data[user_id]['mine_count'] += prize
            bot.send_message(message.chat.id, f"🎉Поздравляем! Вы выиграли {prize} руды!\n♻️Всего руды - {users_data[user_id]['mine_count']}")
        else:
            bot.send_message(message.chat.id, f"😞Вы проиграли ставку. Минус 250 руды.\n♻️Всего руды - {users_data[user_id]['mine_count']}")
        
# Обработка нажатия кнопки "🔮ШАР СУДЬБЫ🔮"
@bot.message_handler(func=lambda message: message.text == 'Шар судьбы')
def ask_fate_ball_step1(message):
    user_id = message.from_user.id
    if user_id not in users_data:
        users_data[user_id] = {'username': message.from_user.username, 'mine_count': 0, 'items': []}
    
    msg = bot.send_message(message.chat.id, "🔮 Какой вопрос хотите задать?")
    bot.register_next_step_handler(msg, ask_fate_ball_step2)

def ask_fate_ball_step2(message):
    question = message.text
    chance = random.randint(0, 100)
    bot.send_message(message.chat.id, f"🔮 Шанс того, что '{question}' равен {chance}%.")

# Обработка нажатия кнопки "🀄ВИКТОРИНА🀄"
@bot.message_handler(func=lambda message: message.text == 'Викторина')
def quiz_handler(message):
    bot.send_message(message.chat.id, "🀄 Угадайте правильную коробку!\nНашёл — получаешь 10,000 руды 💎\nНе нашёл — минус 1,000 руды 💎\nВсего три попытки!")
    
    markup = types.InlineKeyboardMarkup()
    buttons = []
    
    for i in range(40):
        button = types.InlineKeyboardButton("📦", callback_data=f"box_{i+1}")
        buttons.append(button)
        
        if len(buttons) % 5 == 0:
            markup.row(*buttons)
            buttons = []
    
    if buttons:
        markup.row(*buttons)
    
    bot.send_message(message.chat.id, "Выберите одну из коробок:", reply_markup=markup)

# Обработка выбора коробки
@bot.callback_query_handler(func=lambda call: call.data.startswith('box_'))
def box_callback(call):
    user_id = call.from_user.id
    correct_box = random.randint(1, 40)
    selected_box = int(call.data.split('_')[1])
    
    if user_id not in users_data:
        bot.answer_callback_query(call.id, "⚒️ Сначала создайте свою шахту, чтобы создать шахту напишите шахта")
        return

    if selected_box == correct_box:
        users_data[user_id]['mine_count'] += 10000
        bot.answer_callback_query(call.id, "🎉 Вы нашли правильную коробку! +10,000 руды 💎")
    else:
        users_data[user_id]['mine_count'] -= 1000
        bot.answer_callback_query(call.id, "😞 Неправильная коробка! -1,000 руды 💎")

    # Отправить сообщение с текущим количеством руды
    mine_count = users_data[user_id]['mine_count']
    bot.send_message(call.message.chat.id, f"♻️ Текущий баланс руды: {mine_count}")

# обработка нажатии кнопки РП КОМАНДЫ 
@bot.message_handler(func=lambda message: message.text == 'РП команды')
def rp_commands_info(message):
    bot.send_message(message.chat.id, "❓Чтобы узнать какие есть РП команды перейдите по этой ссылке👇\nhttps://telegra.ph/Kak-ispolzovat-RP-komandy-08-06")

    # Словарь для хранения РП команд и соответствующих ответов
rp_commands = {
    "Обнять": "🤗 Вы обняли {username}!",
    "Поцеловать": "💋 Вы поцеловали {username}!",
    "Пожать руку": "🤝 Вы пожали руку {username}!",
    "Послать нахуй": "😡 Вы послали {username} на хуй!",
    "Трахнуть": "🔥 Вы трахнули {username}!",
    "Убить": "🔪 Вы убили {username}!",
    "Ударить": "👊 Вы ударили {username}!",
    "Пить чай": "🍵 Вы пьете чай с {username}!",
    "Пить кофе": "☕ Вы пьете кофе с {username}!",
    "Расстрелять": "💥 Вы расстреляли {username}!"
}

@bot.message_handler(func=lambda message: any(word in message.text for word in rp_commands.keys()))
def rp_command_response(message):
    user_id = message.from_user.id
    if user_id not in users_data:
        bot.send_message(message.chat.id, "⚒️ Сначала создайте свою шахту, чтобы создать шахту напишите шахта")
        return
    
    command = next(word for word in rp_commands.keys() if word in message.text)
    username = message.text.split()[-1]  # Предполагаем, что имя пользователя указано в конце текста сообщения
    
    if username.startswith("@"):
        response = rp_commands[command].format(username=username)
    else:
        response = "Пожалуйста, укажите правильное имя пользователя (начинается с @)."
    
    bot.send_message(message.chat.id, response)

# обработка кибер команд🥷
# Данные тайм докса
last_dox_time = {}

@bot.message_handler(func=lambda message: message.text.lower().startswith('задоксить'))
def dox_user(message):
    user_id = message.from_user.id
    current_time = time.time()
    
    # Проверяем, есть ли у пользователя шахта
    if user_id not in users_data:
        bot.send_message(message.chat.id, "⚒️ Сначала создайте свою шахту, чтобы создать шахту напишите шахта")
        return
    
    # Проверяем, прошло ли 5 минут с последнего "докса"
    if user_id in last_dox_time and current_time - last_dox_time[user_id] < 300:
        remaining_time = int(300 - (current_time - last_dox_time[user_id]))
        bot.send_message(message.chat.id, f"⏳ Вы сможете доксить снова через {remaining_time} секунд.")
        return
    
    # Получаем username из сообщения
    try:
        target_username = message.text.split()[1]  # Извлекаем username
    except IndexError:
        bot.send_message(message.chat.id, "❌ Пожалуйста, укажите username. Пример: задоксить @suren41k2009")
        return

    # Генерируем вознаграждение от 500 до 2000 руды
    reward = random.randint(500, 2000)
    users_data[user_id]['mine_count'] += reward

    # Отправляем сообщение об успешной "операции"
    bot.send_message(message.chat.id, f"😈 Вы задоксили пользователя {target_username} и получили {reward} руды за слитую информацию!")

    # Обновляем время последнего "докса"
    last_dox_time[user_id] = current_time

    # Отображаем текущий баланс пользователя
    bot.send_message(message.chat.id, f"🥷 Ваш текущий баланс руды {users_data[user_id]['mine_count']} ")

# обработка кнопки прочие 🧩
@bot.message_handler(func=lambda message: message.text == 'Команды')
def send_other_info(message):
    bot.send_message(
        message.chat.id, 
        "🧩Если вы хотите узнать больше о VRT, то перейдите по ссылке ниже. Там указаны все игры, которых нет в главном меню👇\nhttps://telegra.ph/INSTRUKCIYA-PO-ISPOLZOVANIYU---VRT-08-12"
    )

# обработка ежедневного приза🎁💎
last_prize_time = {}  # Словарь для хранения времени последнего получения приза

@bot.message_handler(func=lambda message: message.text.lower() == 'ежедневный приз')
def daily_prize(message):
    user_id = message.from_user.id
    current_time = time.time()

    # Проверка, получал ли пользователь приз за последние 24 часа
    if user_id in last_prize_time and current_time - last_prize_time[user_id] < 86400:
        bot.send_message(message.chat.id, "⏳ Вы уже получали ежедневный приз. Попробуйте снова через 24 часа.")
        return

    # Генерация случайного количества руды от 1,000 до 5,000
    prize = random.randint(1000, 5000)

    # Добавляем приз в переменную mine_count
    if user_id in users_data:
        users_data[user_id]['mine_count'] += prize
    else:
        users_data[user_id] = {'username': message.from_user.username, 'mine_count': prize, 'items': [], 'rank': None}

    # Обновляем время последнего получения приза
    last_prize_time[user_id] = current_time

    # Отправляем сообщение пользователю
    bot.send_message(message.chat.id, f"🎉 Вы активировали ежедневный приз и получили {prize} руды! 🎁\n\nИспользуйте приз снова через 24 часа.")

# обработка такси 🚕

# Словарь для хранения состояния пользователей
user_states = {}

@bot.message_handler(func=lambda message: message.text.lower() == 'такси')
def taxi_handler(message):
    user_id = message.from_user.id
    user_states[user_id] = 'waiting_for_destination'
    
    bot.send_message(message.chat.id, "🚕 Вы вызвали такси. Куда хотите поехать?")

# Обработка следующего сообщения пользователя после вызова такси
@bot.message_handler(func=lambda message: message.from_user.id in user_states and user_states[message.from_user.id] == 'waiting_for_destination')
def destination_handler(message):
    user_id = message.from_user.id
    destination = message.text

    # Списываем 100 руб
    if user_id in users_data:
        users_data[user_id]['mine_count'] -= 100
    else:
        users_data[user_id] = {'username': message.from_user.username, 'mine_count': -100, 'items': [], 'rank': None}

    # Удаляем состояние пользователя
    del user_states[user_id]

    # Отправляем сообщение о прибытии
    bot.send_message(message.chat.id, f"🏁 Вы приехали в \"{destination}\". С вас сняли 100 руды за проезд. Спасибо за использование нашего сервиса такси! 🚖")

# обработки слова токен 🪙
@bot.message_handler(func=lambda message: message.text.lower() == 'токен')
def token_info(message):
    bot.send_message(
        message.chat.id, 
        "🪙 Токен VRT, наша команда хочет сделать свой токен, на котором можно чуть-чуть подзаработать.\n\n"
        "😔 Но, к сожалению, на данный момент нет такой возможности, поэтому следите за новостями в нашем telegram-канале - @VRT_dev.\n\n"
        "🫂 Наша команда постарается сделать токен в ближайшее время!"
    )

# Обработка команды "ограбить банк🥷"
@bot.message_handler(func=lambda message: message.text.lower() == 'ограбить банк')
def rob_bank(message):
    user_id = message.from_user.id

    # Проверяем, если пользователь уже есть в базе данных, если нет — создаем запись
    if user_id not in users_data:
        users_data[user_id] = {
            'username': message.from_user.username,
            'mine_count': 0,
            'items': [],
            'rank': None,
            'last_robbery_time': 0  # Время последнего ограбления
        }

    current_time = time.time()
    last_robbery_time = users_data[user_id].get('last_robbery_time', 0)

    # Проверяем, прошло ли 24 часа (86400 секунд) с последнего ограбления
    if current_time - last_robbery_time < 86400:
        remaining_time = int(86400 - (current_time - last_robbery_time))
        hours = remaining_time // 3600
        minutes = (remaining_time % 3600) // 60
        bot.send_message(message.chat.id, f"⏳ Вы недавно ограбили банк. Попробуйте снова через {hours} часов и {minutes} минут.")
        return

    # 50/50 шанс ограбления
    if random.choice([True, False]):
        # Успешное ограбление: случайное количество руды от 5000 до 10000
        reward = random.randint(5000, 10000)
        users_data[user_id]['mine_count'] += reward
        bot.send_message(message.chat.id, f"💰 Вы ограбили банк и получили {reward} руды! Удача на вашей стороне! 🎉")
    else:
        # Неудачное ограбление: штраф 1000 руды
        fine = 1000
        users_data[user_id]['mine_count'] -= fine
        bot.send_message(message.chat.id, f"🚔 К сожалению, вам не удалось ограбить банк, и вас оштрафовали на {fine} руды. Попробуйте в следующий раз! 😢")

    # Обновляем время последнего ограбления и данные пользователя
    users_data[user_id]['last_robbery_time'] = current_time

# обработка кнопки (promo🎁)
promo_codes = {
    'PRM123': 50000,
    'GFT456': 50000,
    'BNS789': 50000,
    'RWD012': 50000,
    'WIN345': 50000,
    'LCK678': 50000,
    'TRY901': 50000,
    'FUN234': 50000,
    'JOY567': 50000,
    'GLD890': 50000
}

used_promo_codes = {}  # Словарь для отслеживания использованных промокодов каждым пользователем

@bot.message_handler(func=lambda message: message.text == 'Промокоды')
def ask_for_promo_code(message):
    user_id = message.from_user.id
    if user_id in users_data:
        bot.send_message(message.chat.id, "🎁 Введите ваш промокод:")
        bot.register_next_step_handler(message, process_promo_code)
    else:
        bot.send_message(message.chat.id, "⚒️ Сначала создайте свою шахту, чтобы создать шахту напишите шахта")

def process_promo_code(message):
    user_id = message.from_user.id
    
    # Проверка типа сообщения
    if message.content_type != 'text':
        bot.send_message(message.chat.id, "❌ Пожалуйста, введите текстовый промокод.")
        bot.register_next_step_handler(message, process_promo_code)  # Повторно запросить ввод промокода
        return

    promo_code = message.text.strip().upper()

    if promo_code in promo_codes:
        # Проверка, использовал ли этот пользователь уже данный промокод
        if user_id in used_promo_codes and promo_code in used_promo_codes[user_id]:
            bot.send_message(message.chat.id, "❌ Вы уже использовали этот промокод.")
        else:
            users_data[user_id]['mine_count'] += promo_codes[promo_code]
            # Отметить промокод как использованный пользователем
            if user_id not in used_promo_codes:
                used_promo_codes[user_id] = []
            used_promo_codes[user_id].append(promo_code)
            bot.send_message(message.chat.id, f"✅ Промокод успешно активирован! Вы получили {promo_codes[promo_code]} руды. 💎")
    else:
        bot.send_message(message.chat.id, "❌ Неверный промокод.")
        bot.register_next_step_handler(message, process_promo_code)  # Повторно запросить ввод промокода

# обработка кнопки трейдинг📉📈
@bot.message_handler(func=lambda message: message.text == 'Трейд')
def ask_for_trade_input(message):
    user_id = message.from_user.id
    if user_id in users_data:
        bot.send_message(message.chat.id, "💹 Введите сумму и направление (вверх/вниз) в формате: {сумма} вверх/вниз")
        bot.register_next_step_handler(message, process_trade)
    else:
        bot.send_message(message.chat.id, "⚒️ Сначала создайте свою шахту, чтобы создать шахту напишите шахта")

def process_trade(message):
    user_id = message.from_user.id
    try:
        trade_input = message.text.strip().split()
        trade_amount = int(trade_input[0])
        trade_direction = trade_input[1].lower()

        if trade_direction not in ['вверх', 'вниз']:
            bot.send_message(message.chat.id, "❌ Неверное направление. Пожалуйста, введите 'вверх' или 'вниз'.")
            return

        if trade_amount > users_data[user_id]['mine_count']:
            bot.send_message(message.chat.id, "❌ Недостаточно руды для такой ставки.")
            return

        # Определение случайного исхода
        outcome = random.choice(['вверх', 'вниз'])
        # Определение случайного процента от 1% до 100%
        percentage_change = random.randint(1, 100)
        change_amount = trade_amount * percentage_change // 100

        if trade_direction == outcome:
            users_data[user_id]['mine_count'] += change_amount
            bot.send_message(message.chat.id, f"🎉 Ваша ставка на {trade_direction} оказалась верной! Ваш баланс увеличился на {change_amount} руды ({percentage_change}%). 💰\n♻️Ваш текущий баланс руды: {users_data[user_id]['mine_count']}")
        else:
            users_data[user_id]['mine_count'] -= change_amount
            bot.send_message(message.chat.id, f"😞 Ваша ставка на {trade_direction} не сыграла. Вы потеряли {change_amount} руды ({percentage_change}%). 💸\n♻️Ваш текущий баланс руды: {users_data[user_id]['mine_count']}")

    except (ValueError, IndexError):
        bot.send_message(message.chat.id, "❌ Неверный формат ввода. Пожалуйста, введите данные в формате: {сумма} вверх/вниз")

user_states = {}

# Словарь для хранения времени последнего открытия кейса пользователями
last_case_open_time = {}

# Данные пользователей
last_work_time = {}

# обработка работы
@bot.message_handler(func=lambda message: message.text.lower() == 'работа')
def start_work(message):
    user_id = message.from_user.id
    current_time = time.time()

    # Проверяем, есть ли пользователь в базе
    if user_id not in users_data:
        bot.send_message(message.chat.id, "⚒️ Сначала создайте свою шахту, чтобы создать шахту напишите шахта")
        return

    # Проверяем, прошло ли 5 минут с последней работы
    if user_id in last_work_time and current_time - last_work_time[user_id] < 300:
        remaining_time = int(300 - (current_time - last_work_time[user_id]))
        bot.send_message(message.chat.id, f"⏳ Вы можете снова работать через {remaining_time} секунд.")
        return

    # Проверяем, есть ли у пользователя минимум 200 руды
    if users_data[user_id]['mine_count'] < 200:
        bot.send_message(message.chat.id, "❌ У вас недостаточно руды для работы. Требуется 200 руды.")
        return

    # Отнимаем 200 руды за начало работы
    users_data[user_id]['mine_count'] -= 200

    # Шанс на успех 70%
    if random.random() <= 0.7:
        # Успех: заработал от 1000 до 3000 руды
        earnings = random.randint(1000, 3000)
        users_data[user_id]['mine_count'] += earnings
        bot.send_message(message.chat.id, f"💰 Поздравляем! Вы успешно завершили работу и заработали {earnings} руды!")
    else:
        # Неудача: теряет 200 руды
        bot.send_message(message.chat.id, "😞 Увы, вы прогорели на работе и потеряли 200 руды")

    # Обновляем время последней работы
    last_work_time[user_id] = current_time

    # Информация о количестве руды
    bot.send_message(message.chat.id, f"💎 Ваш текущий баланс руды {users_data[user_id]['mine_count']}")

# обработка кейс 2
@bot.message_handler(func=lambda message: message.text.lower() == 'открыть кейс 2')
def open_case_2(message):
    user_id = message.from_user.id
    current_time = time.time()

    # Проверка, создал ли пользователь шахту
    if user_id not in users_data:
        bot.send_message(message.chat.id, "⚒️ Сначала создайте свою шахту, чтобы создать шахту напишите шахта")
        return

    # Проверка, прошло ли 5 минут с последнего открытия кейса
    if user_id in last_case_open_time and current_time - last_case_open_time[user_id] < 300:
        time_left = int(300 - (current_time - last_case_open_time[user_id]))
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        bot.send_message(message.chat.id, f"⏳ Вы недавно открыли кейс 2. Подождите {minutes_left} мин {seconds_left} сек перед следующим открытием.")
        return

    # Генерация случайной суммы от 500 до 1,000 руб
    reward = random.randint(500, 1000)
    users_data[user_id]['mine_count'] += reward

    # Обновляем время последнего открытия кейса
    last_case_open_time[user_id] = current_time

    # Отправляем сообщение пользователю
    bot.send_message(message.chat.id, f"🎉 Вы открыли кейс 2 и получили {reward} руды! 💎\n♻️ Всего руды - {users_data[user_id]['mine_count']}")

# обработка кнопки шипперим💞
@bot.message_handler(func=lambda message: message.text == 'Шипперим')
def request_usernames(message):
    if message.chat.type in ['group', 'supergroup']:
        user_states[message.from_user.id] = {'state': 'waiting_for_usernames'}
        bot.send_message(message.chat.id, "💬 Введите 2 юзернейма, которые хотите зашиперить (например, @user1 @user2):")
    else:
        bot.send_message(message.chat.id, "❌ Эту команду можно использовать только в группе.")

@bot.message_handler(func=lambda message: user_states.get(message.from_user.id, {}).get('state') == 'waiting_for_usernames')
def handle_usernames(message):
    if message.chat.type in ['group', 'supergroup']:
        text = message.text.strip()
        usernames = text.split()
        
        if len(usernames) == 2 and all(username.startswith('@') for username in usernames):
            user1, user2 = usernames
            bot.send_message(message.chat.id, f"💞 Шипперим: {user1} и {user2} живите вместе счастливо и долго ☺️")
        else:
            bot.send_message(message.chat.id, "❌ Введите два корректных юзернейма через пробел (например, @user1 @user2).")
        
        # Сброс состояния пользователя
        user_states[message.from_user.id] = {'state': 'none'}
    else:
        bot.send_message(message.chat.id, "❌ Эта команда доступна только в группах.")

# новогодний ивент
NewYear = ('')

# обработка новогодний ивент ❄️❄️❄️
@bot.message_handler(func=lambda message: message.text == 'Ивент')
def send_other_info(message):
    bot.send_message(
        message.chat.id, 
        "❄️НОВОГОДНИЙ ИВЕНТ❄️\n\n🎅в эту новогоднюю ночь придёт санта!\nесли ты вёл себя хорошо то получишь хорошие подарки на этот ивент!\n\n🎇разработчики хотят поздравить всех с новым годом!\n\n🪨на новогодний ивент вы получите много руды и много новых команд и будете собирать снежки!\n\n💬все новогодние команды и т.д. находятся по ссылке ниже👇\nhttp://telegra.ph/INSTRUKCIYA-PO-ISPOLZOVANIYU---VRT-08-12")

# Обработка собрать снежки 
@bot.message_handler(func=lambda message: message.text == 'Собрать снежки')
def open_case(message):
    user_id = message.from_user.id

    if user_id not in users_data:
        bot.send_message(message.chat.id, "⚒️ Сначала создайте свою шахту, чтобы создать шахту напишите шахта")
        return

    current_time = datetime.now()
    last_cas_time = users_data[user_id].get('last_cas_time')

    # Проверка времени последнего открытия кейса
    if last_cas_time and current_time - last_cas_time < timedelta(minutes=1):
        remaining_time = timedelta(minutes=5) - (current_time - last_cas_time)
        bot.send_message(message.chat.id, f"⏳ Вы сможете собрать снежки снова через {remaining_time.seconds} секунд")
        return

    # Обновление времени последнего открытия кейса
    users_data[user_id]['last_cas_time'] = current_time

    # Вычисление выигранной руды
    received_ore = random.randint(1000, 5000)  # Увеличение выигрыша в 2 раза
    users_data[user_id]['mine_count'] += received_ore
    mine_count = users_data[user_id]['mine_count']

    # Отправка сообщения с результатом
    bot.send_message(message.chat.id, "❄️ Вы собрали снежки и обменяли их на руду!\nЧтобы узнать количество руды напишите Профиль")

# Обработчик для символа ❄️
@bot.message_handler(func=lambda message: message.text == "❄️")
def send_halloween_greeting(message):
    user_id = message.from_user.id

    # Проверка, существует ли у пользователя шахта
    if user_id not in users_data:
        bot.reply_to(message, "⚒️ Сначала создайте свою шахту, чтобы создать шахту напишите шахта")
        return

    # Проверка, активировал ли пользователь ❄️ ранее
    if users_data[user_id].get('halloween_claimed', False):
        bot.reply_to(message, "❄️ Приз на новый год можно получить только один раз!")
        return

    # Увеличение mine_count на 10.000 и установка флага активации
    users_data[user_id]['mine_count'] += 10000
    users_data[user_id]['halloween_claimed'] = True
    bot.reply_to(message, "🎄С НОВЫМ ГОДОМ\n❄️ ты получил 10.000 руды")

# Обрабатываем сообщения с шаблоном "кинуть снежок @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Кинуть снежок @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя
        username_to_hug = message.text.split(" ")[2]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ
        bot.reply_to(message, f"☃️ {sender_username} кинул(а) снежок в {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "подарить подарок @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Подарить подарок @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя
        username_to_hug = message.text.split(" ")[2]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ
        bot.reply_to(message, f"🎁 {sender_username} подарил(а) подарок {username_to_hug}")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# Обрабатываем сообщения с шаблоном "скинуть в сугроб @username"
@bot.message_handler(func=lambda message: message.text and message.text.startswith("Скинуть в сугроб @"))
def hug_user(message):
    try:
        # Извлекаем имя пользователя
        username_to_hug = message.text.split(" ")[3]
        
        # Получаем username отправителя
        sender_username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        
        # Отправляем ответ
        bot.reply_to(message, f"🧗 {sender_username} скинул(а) {username_to_hug} в сугроб")
    except IndexError:
        bot.reply_to(message, "Упс! Похоже, ты не указал пользователя")

# обработка 🍊
@bot.message_handler(func=lambda message: message.text == 'Съесть мандарин')
def send_other_info(message):
    bot.send_message(
        message.chat.id, 
        "🍊 БРО СОЖЫРАЛ МАНДАРИН!")

# обработка снег ❄️
@bot.message_handler(func=lambda message: message.text == 'Снег')
def send_other_info(message):
    bot.send_message(
        message.chat.id, 
        "🌨️ кажись снег пошёл...")

# обработка ёлка🎄
@bot.message_handler(func=lambda message: message.text == 'Ёлка')
def send_other_info(message):
    bot.send_message(
        message.chat.id, 
        "🎄ёлка горит!")

# обработка украсть подарки 🎁
@bot.message_handler(func=lambda message: message.text == 'Украсть подарки')
def send_other_info(message):
    bot.send_message(
        message.chat.id, 
        "🐲 Бля Гринч спиздил подарки у детей...")

# обработка запустить фейерверк 🎇
@bot.message_handler(func=lambda message: message.text == 'Запустить фейерверк')
def send_other_info(message):
    bot.send_message(
        message.chat.id, 
        "🎇 Фейерверки были запущены!!!")

# обработка поздравить с новым годом 2️⃣0️⃣2️⃣5️⃣
@bot.message_handler(func=lambda message: message.text == 'Поздравить с нг')
def send_other_info(message):
    bot.send_message(
        message.chat.id, 
        "‼️Команда будет доступна:\n3️⃣1️⃣ 1️⃣2️⃣ 2️⃣0️⃣2️⃣4️⃣")

# обработка построить снеговика
@bot.message_handler(func=lambda message: message.text == 'Построить снеговика')
def send_other_info(message):
    bot.send_message(
        message.chat.id, 
        "⛄Вы построили снеговика!")

# обработка 🎅 
@bot.message_handler(func=lambda message: message.text == 'Санта')
def send_other_info(message):
    bot.send_message(
        message.chat.id, 
        "🎅ХО-ХО-ХО ты вёл себя хорошо в этом году?")

# обработка построить иглу
@bot.message_handler(func=lambda message: message.text == 'Построить иглу')
def send_other_info(message):
    bot.send_message(
        message.chat.id, 
        "🐻‍❄️ Вы построили иглу и живёте там хах")

# топ чатов
chats = ['🔥ТОП ЧАТЫ ГДЕ ЕСТЬ BCS БОТЫ🔥\n\n1. @suren41kchatik\n2. @RPliveWorld\n3. @grifer_com']

# Обработчик топов
@bot.message_handler(func=lambda message: message.text.lower() in ['топ', 'топы', 'чаты', 'чат', 'топ чаты'])
def handle_greeting(message):
    response = random.choice(chats)
    bot.reply_to(message, response)

# Запуск бота
bot.polling(none_stop=True)