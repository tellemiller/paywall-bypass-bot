from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import json

### ONLY CHANGE THE THREE CONSTANTS BELOW THIS LINE ###

BYPASSED_DOMAINS_FILE = 'bypassed_domains.json' # This path should be directed to a JSON file that can store your list of domains to bypass
BOT_TOKEN = 'XXXXX:XXXXXXX:XXXXXX:XXX' # This should be your Telegram Bot Token or API key
CHAT_ID = '-1001966413753' # This is the ID of the chat you want the bot monitor. See https://api.telegram.org/bot<YourBOTToken>/getUpdates

### ONLY CHANGE THE THREE CONSTANTS ABOVE THIS LINE ###

BYPASSED_DOMAINS = []

def save_allowed_domains():
    with open(BYPASSED_DOMAINS_FILE, 'w') as f:
        json.dump(BYPASSED_DOMAINS, f)

def load_allowed_domains():
    try:
        with open(BYPASSED_DOMAINS_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def shorten_url(url):
    return "https://12ft.io/" + url

def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Hi {user.first_name}! I'm the Paywall Buster Bot. Just send me a link from any of the added domains, and I'll help you bypass the paywall!")

def help_command(update: Update, context: CallbackContext) -> None:
    commands = [
        "/start - Start using the bot",
        "/help - Show available commands",
        "/add_domain <domain> - Add a domain to the list of bypassed domains",
        "/list_domains - List the currently bypassed domains"
    ]
    help_text = "\n".join(commands)
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Here are the available commands:\n{help_text}")

def add_domain(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 1:
        new_domain = context.args[0]
        BYPASSED_DOMAINS.append(new_domain)
        save_allowed_domains()
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Added '{new_domain}' to the list of bypassed domains.")
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Usage: /add_domain <domain>")

def list_domains(update: Update, context: CallbackContext) -> None:
    if BYPASSED_DOMAINS:
        domains_list = "\n".join(BYPASSED_DOMAINS)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"The currently bypassed domains are:\n{domains_list}")
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="No domains are currently bypassed.")

def process_message(update: Update, context: CallbackContext) -> None:
    message = update.message.text
    for domain in BYPASSED_DOMAINS:
        if domain in message:
            original_url = message
            shortened_url = shorten_url(original_url)
            context.bot.send_message(chat_id=CHAT_ID, text="Here is the bypass link:\n" + shortened_url)
            break

if __name__ == '__main__':
    BYPASSED_DOMAINS = load_allowed_domains()

    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("add_domain", add_domain, pass_args=True))
    dp.add_handler(CommandHandler("list_domains", list_domains))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, process_message))

    updater.start_polling()
    updater.idle()
