# paywall-bypass-bot
The Paywall Buster Bot is a Telegram bot that helps users bypass paywalls on specific domains by providing shortened links using the [12ft.io](https://12ft.io/) service.

## Features
- Bypass paywalls for specific domains using 12ft.io
- Add and manage domains to bypass paywalls
- List currently bypassed domains
- User-friendly commands and interactions

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/paywall-buster-bot.git
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Create a Telegram bot and obtain your bot token. Refer to the [Telegram Bot documentation](https://core.telegram.org/bots#botfather) for instructions.
6. Update the `telegram_bot.py` constants with your information:
   
   ```python
   BYPASSED_DOMAINS_FILE = 'path_to_your_bypassed_domains.json_file'
   BOT_TOKEN = 'your_bot_token'
   CHAT_ID = 'id_of_chat_you_want_to_monitor'
   ```
   You can find your chat ID by adding the bot to the Telegram group you want to monitor and typing a message. When you visit https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates, you'll be presented with a JSON file that has the ID of your chat.
7. Run the bot:
   ```bash
   python telegram_bot.py
   ```

## Commands

- `/start`: Start using the bot and get a brief introduction.
- `/help`: Show available commands and their descriptions.
- `/add_domain <domain>`: Add a domain to the list of domains you want to bypass.
- `/list_domains`: List the currently bypassed domains.

## Free Hosting Options
Your Telegram bot can only monitor for links while the `telegram_bot.py` file is running. You can leave the bot running on your own computer, or just run the Python file when you need the bot. Both of these options are a bit tedious and don't work well when you want the bot to work for other people in your Telegram group. You could rent server space and have your bot run there, but there is typically a cost associated with this. I've outlined below how you can host your bot for free, with certain limitations. 

1. Visit [Python Anywhere](https://www.pythonanywhere.com/) and create an account.
2. Go to the _Files_ section and add your two files, `bypassed_domains.json` and `telegram_bot.py`.
3. Using the Bash console on the webpage, you can install the required Python libraries.
4. Navigate into your `telegram_bot.py` file and run the file.

Your Telegram bot should now be running and you can close the webpage. You may have to occasionally revisit Python Anywhere to start your bot again if you make updates or there is scheduled maintenance.
> **Note**  
> For free accounts on Python Anywhere, there is a storage and CPU usage limit. Once you have maxed out your CPU usage of 100 seconds, the bot will continue to run but with decreased processor priority. This limit is reset every 24 hours. You can view your remaining usage on your dashboard.
