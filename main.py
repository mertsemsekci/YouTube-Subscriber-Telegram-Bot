import time
import telebot
from googleapiclient.discovery import build
import logging
import config

# Create Telegram bot
bot = telebot.TeleBot(config.TOKEN)

# Configure error logging
logging.basicConfig(filename='bot.log', level=logging.ERROR)

# Get subscriber count from YouTube API
def get_subscriber_count(channel_id, api_key):
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        request = youtube.channels().list(
            part='statistics',
            id=channel_id
        )
        response = request.execute()
        subscriber_count = response['items'][0]['statistics']['subscriberCount']
        return subscriber_count
    except Exception as e:
        logging.error(f'Error: {e}')
        return None

# Send subscriber count to the specified chat
def send_subscriber_count():
    previous_sub_count = 0
    while True:
        try:
            # Get subscriber count
            subscriber_count = get_subscriber_count(config.CHANNEL_ID, config.API_KEY)

            # If subscriber count is not None and different from previous, send message
            if subscriber_count is not None and subscriber_count != previous_sub_count:
                message = f"Your current subscriber count: {subscriber_count}"
                bot.send_message(chat_id=config.CHAT_ID, text=message)
                previous_sub_count = subscriber_count
        except Exception as e:
            logging.error(f'Error: {e}')
        # Wait for 4 seconds
        time.sleep(4)

# Run the bot
if __name__ == "__main__":
    try:
        send_subscriber_count()
    except KeyboardInterrupt:
        pass
