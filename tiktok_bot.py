from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

TOKEN = "توكن_البوت_حقك"

def start(update, context):
    update.message.reply_text("👋 أهلاً! أرسل لي رابط فيديو من TikTok وسأحمله لك 🎥")

def download_tiktok(update, context):
    url = update.message.text.strip()
    api_url = f"https://www.tikwm.com/api/?url={url}"
    try:
        r = requests.get(api_url).json()
        video_url = r["data"]["play"]  # رابط الفيديو بدون العلامة المائية
        update.message.reply_video(video_url, caption="✅ تم التحميل بنجاح")
    except Exception as e:
        update.message.reply_text("❌ لم أتمكن من تحميل الفيديو. تأكد من الرابط.")

updater = Updater(TOKEN, use_context=True)   # ⚠️ هذا السطر ضروري
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_tiktok))

updater.start_polling()
updater.idle()
