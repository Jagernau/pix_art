from telebot import TeleBot, types
from settings import TELEGRAM_BOT_TOKEN

bot = TeleBot(str(TELEGRAM_BOT_TOKEN))

@bot.message_handler(content_types=["photo"])
def photo(message: types.Message):
    photo_chat = bot.get_file(message.photo[len(message.photo)-1].file_id)
    file = bot.download_file(photo_chat.file_path)
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.chat.id, f"{message}")

bot.polling()



