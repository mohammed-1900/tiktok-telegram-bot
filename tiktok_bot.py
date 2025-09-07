from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

# التوكن الخاص بك
TOKEN = "8098576301:AAEtvM74taP9W0BVuw3mtnVhLD5X5ilLfKU"

def start(update, context):
    update.message.reply_text("👋 أهلاً! أرسل لي رابط فيديو من TikTok وسأرجعه لك بدون العلامة المائية.")

def download_tiktok(update, context):
    url = update.message.text.strip()

    api_url = f"https://www.tikwm.com/api/?url={url}"
    r = requests.get(api_url).json()

    try:
        video_url = r["data"]["play"]  # رابط الفيديو بدون العلامة
        update.message.reply_video(video_url, caption="✅ تم التحميل بدون العلامة المائية")
    except Exception as e:
        update.message.reply_text("⚠️ لم أتمكن من تحميل الفيديو. تأكد من الرابط.")
        print("Error:", e)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_tiktok))

updater.start_polling()
updater.idle()
