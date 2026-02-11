import telebot
import google.generativeai as genai

# Твои ключи
TELEGRAM_TOKEN = '8246409144:AAFGQ_ty2jVgmcUJstM7J1WyWXglBSXJMfk'
GEMINI_KEY = 'AIzaSyBzg6R9YQbVo9cwow7Xw67nO3RWoBku_xQ'

# Настройка
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def chat(message):
    response = model.generate_content(message.text)
    bot.reply_to(message, response.text)

print("Бот запущен...")
bot.infinity_polling()
