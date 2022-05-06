import constant as keys
from telegram.ext import *
import responses as R 

print("Bot started ...")

def start_command(update, context):
	update.message.reply_text('یه چیزی تایپ کن تا شروع کنیم')

def help_command(update,context):
	update.message.reply_text('اگر کمک خواستی تئ تو گوگل سرچ کن')

def handle_command(update, context):
	text = str(update.message.text).lower()
	response = R.sample_response(text)

	update.message.reply_text(response)

def error(update, context):
	print(f"Update {update} caused error {context.error}")

def update_message_to_channel_B(update, context):
    context.bot.send_message(chat_id='-615643857', text='Message receveid on Channel A')


def main():
	updater = Updater(keys.API_KEY, use_context=True)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler('start', start_command))
	dp.add_handler(CommandHandler('start', help_command))

	dp.add_handler(MessageHandler(Filters.text, handle_command))
	dp.add_handler(MessageHandler(Filters.text, update_message_to_channel_B))

	dp.add_error_handler(error)

	updater.start_polling()

	updater.idle()

main()