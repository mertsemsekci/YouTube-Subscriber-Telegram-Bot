<h1>YouTube Subscriber Count Telegram Bot</h1>
<p>This project is a simple Telegram bot that retrieves the subscriber count of a YouTube channel using the YouTube Data API and sends it to a specified Telegram chat.</p>

<h2>Features:</h2>
<ul>
  <li>Retrieves the subscriber count of a YouTube channel using the YouTube Data API.</li>
  <li>Sends the subscriber count to a specified Telegram chat.</li>
  <li>Error handling and logging for robustness.</li>
</ul>

<h2>Technologies Used:</h2>
<ul>
  <li>Python</li>
  <li>Telebot (Telegram Bot API for Python)</li>
  <li>Google API Client Library for Python</li>
</ul>

<h2>How to Use:</h2>
<ol>
  <li>Clone the repository to your local machine.</li>
  <li>Install the required dependencies using <code>pip install -r requirements.txt</code>.</li>
  <li>Set up your Telegram bot token, YouTube API key, Telegram channel ID, and chat ID in the <code>config.py</code> file.</li>
  <li>Run the <code>main.py</code> file.</li>
</ol>

<h2>Directory Structure:</h2>
<ul>
  <li><code>main.py</code>: Main script to run the bot.</li>
  <li><code>config.py</code>: Configuration file to store API keys and chat IDs.</li>
  <li><code>requirements.txt</code>: List of Python dependencies.</li>
  <li><code>bot.log</code>: Log file for error logging.</li>
</ul>

<h2>Contributors:</h2>
<ul>
  <li><a href="https://github.com/mertsemsekci">Abdurrahman Mert Semsekçi</a></li>
</ul>

<h2>Notes:</h2>
<ul>
  <li>This bot is designed to run continuously in the background. Ensure proper handling when deployed on servers or in production environments.</li>
  <li>Make sure to keep your API keys and tokens secure and do not expose them publicly.</li>
</ul>
