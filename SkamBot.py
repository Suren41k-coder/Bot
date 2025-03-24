import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7960010107:AAE9jhGbXha0faHIM5IsbvFE7WlSZulw-SY"
bot = telebot.TeleBot(TOKEN)

# Id
TARGET_USER_ID = 6288632545

user_data = {}

@bot.message_handler(commands=['reqpay'])
def send_command(message):
    user_data[message.chat.id] = {}
    bot.send_message(message.chat.id, "Введите название банка куда хотите вывести:")
    bot.register_next_step_handler(message, get_text)

def get_text(message):
    user_data[message.chat.id]['text'] = message.text
    bot.send_message(message.chat.id, "Введите сумму платежа:")
    bot.register_next_step_handler(message, get_amount)

def get_amount(message):
    user_data[message.chat.id]['amount'] = message.text
    bot.send_message(message.chat.id, "Введите номер банковской карты:\n\n(Если нужны какие-то данные то их тоже укажите)")
    bot.register_next_step_handler(message, get_number)

def get_number(message):
    user_data[message.chat.id]['number'] = message.text
    data = user_data[message.chat.id]

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Подтвердить", callback_data=f"confirm_{message.chat.id}"))

    text = f"📩 Новое сообщение:\n🔹 {data['text']}\n💰 {data['amount']}\n🔢 {data['number']}"
    bot.send_message(TARGET_USER_ID, text, reply_markup=markup)
    bot.send_message(message.chat.id, "❗запрос отправлен на модерацию\n(убедитесь что вы ввели всё верно иначе вы потеряете свою выплату и больше не сможете её получить)\n\nЕсли вы вели какой-то спам или что-то неправильно то запрос будет проигнорирован!")

@bot.callback_query_handler(func=lambda call: call.data.startswith("confirm_"))
def confirm_data(call):
    user_id = int(call.data.split("_")[1])
    bot.send_message(user_id, "✅ Подтверждено! (ожидайте вашей выплаты в течение трёх дней)")
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Привет, это бот для выплат сотрудников @TeamWorkCommes\n\nкоманды для помощи👇\n\n/start - Начало\n/reqpay - запросить выплату\n/help - помощь по боту или же информация о нём")
    
# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "🚩 У вас возникла ошибка с ботом или с выплатой?\n\nобратитесь к нашему менеджеру для решения проблемы - @managerBCS\n\n❓информация о боте: данный бот был создан Для выплат сотрудников канала @TeamWorkCommes\n\nзанимаясь арбитражом или комментариями вы можете заработать бешеные деньги! Вся информация тут - https://t.me/TeamWorkCommes/7\n\n⭐ Если у тебя есть лишние звёзды то мы рады будем скупать их у тебя!\nДля этого просто обратись сюда - @managerBCS")
    
while True:  # Запускаем бесконечный цикл
    try:
        bot.polling(none_stop=True, timeout=30)  # Подключаемся к Telegram
    except Exception as e:
        print(f"Ошибка: {e}")  # Выводим ошибку в консоль (можно убрать)
        time.sleep(5)  # Ждём 5 секунд и пробуем снова