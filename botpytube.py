import telebot
from pytube import YouTube

bot = telebot.TeleBot("5466840474:AAHkvwnNDbDua_uGraUGr2z5uatoh-eLtjM")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет,этот Бот умеет скачивать видео с YouTube,нужна только ссылка!")

@bot.message_handler(func=lambda message: True)
def bot_save(message):
    yt = YouTube(message.text)
    yt.streams
    YouTube(message.text).streams.filter(res="360p").first().download(filename = f"{message.chat.id}.mp4")  
    bot.send_video(message.chat.id, video = open (f"{message.chat.id}.mp4",'rb'),supports_streaming=True)

bot.infinity_polling()

