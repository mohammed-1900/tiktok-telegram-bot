from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

TOKEN = "حط التوكن هنا"

def start(update, context):
    update.message.reply_text("👋 أهلاً! أرسل لي رابط فيديو من TikTok وسأرجعه لك بدون علامة مائية.")

def download_tiktok(update, context):
    url = update.message.text.strip()
    api_url = f"https://www.tikwm.com/api/?url={url}"
    try:
        r = requests.get(api_url).json()
        video_url = r["data"]["play"]  # رابط الفيديو بدون العلامة
        update.message.reply_video(video_url, caption="✅ تم التحميل بنجاح!")
    except Exception as e:
        update.message.reply_text("❌ لم أتمكن من تحميل الفيديو. تأكد من الرابط.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_tiktok))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
