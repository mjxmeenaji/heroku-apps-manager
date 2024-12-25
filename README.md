# Heroku Apps Manager

<p align="center">
  <img src="https://i.imgur.com/LqyVINf_d.webp?maxwidth=760&fidelity=grand" alt="Heroku Apps Manager Logo" width="300" />
</p>

<h1 align="center">Heroku Apps Manager</h1>

<p align="center">
  Manage your Heroku apps easily with this Telegram bot!
</p>

## Overview
Heroku Apps Manager is a Python-based Telegram bot designed to simplify the management of Heroku applications. With this bot, users can:

- List all Heroku apps linked to their account.
- View the status of each app's dynos.
- Start or stop dynos directly via Telegram.
- Control scaling of worker and web processes for Heroku apps.

This project leverages the Pyrogram library for Telegram bot interactions and the Heroku3 library to interface with Heroku's API.

---

## Features
1. **List All Apps**: Fetches all Heroku apps in your account (excluding those in the red zone).
2. **App Status**: Displays whether the dynos of each app are running or stopped.
3. **Scale Dynos**: Allows you to start or stop dynos with a simple button click.
4. **Multi-User Support**: Restricts usage to authorized users for enhanced security.

---

## Installation

### Prerequisites
- Python 3.9+
- A Heroku account with an API key.
- Telegram Bot Token (created via [BotFather](https://t.me/botfather)).
- `git` and `pip` installed on your machine.

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/terabyte-26/heroku-apps-manager.git
   cd heroku-apps-manager
   ```

2. **Set Up a Virtual Environment** (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Create a `.env` file in the project directory and add the following keys:
   ```env
   API_ID=your_telegram_api_id
   API_HASH=your_telegram_api_hash
   BOT_TOKEN=your_bot_token
   HEROKU_API_KEY=your_heroku_api_key
   ```

5. **Run the Bot**:
   ```bash
   python main.py
   ```

---

## Deploy to Heroku
You can deploy the bot directly to Heroku using the button below:

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://www.heroku.com/deploy/?template=https://github.com/terabyte-26/heroku-apps-manager)
### Steps for Deployment:
1. Click on the **Deploy to Heroku** button above.
2. Fill in the required environment variables:
   - **API_ID**: Your Telegram API ID.
   - **API_HASH**: Your Telegram API Hash.
   - **BOT_TOKEN**: Token of your Telegram bot.
   - **HEROKU_API_KEY**: Your Heroku API key.
3. Click **Deploy App**.
4. Once deployed, start the bot from the Heroku dashboard.

---

## Usage
1. Start the bot on Telegram by messaging `/start`.
2. View a list of your Heroku apps and their statuses.
3. Use the inline buttons to scale dynos or toggle their statuses.

---

## Files Structure
```
heroku-apps-manager/
├── manager/
│   ├── __init__.py          # Bot initialization
│   ├── callbacks.py       # Telegram bot handlers
│   ├── helpers.py         # Heroku-related helper functions
│   └── vars.py            # Configuration and environment variables
├── main.py                 # Main entry point
├── requirements.txt        # Python dependencies
├── Procfile               # Heroku process types
└── .env                   # Environment variables (not included in repo)
```

---

## Contact
For support or further information, feel free to reach out:

- **Website**: [terabyte-26.com](https://terabyte-26.com/quick-links/)
- **Telegram**: [@hamza_farahat](https://t.me/hamza_farahat)
- **WhatsApp**: [+212772177012](https://wa.me/212772177012)
- **Email**: [farahat.hamza1@gmail.com](mailto:farahat.hamza1@gmail.com)

---

## License
This project is created by Hamza Farahat. All rights reserved. Contact for usage rights and permissions.

