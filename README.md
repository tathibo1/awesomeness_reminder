# Awesomeness Reminder

A Python application that generates uplifting messages using a local LLM (Ollama) and sends them via email to a list of recipients. Perfect for sending daily motivational messages or positive affirmations.

## Overview

This project uses:
- **Ollama** with DeepSeek R1 model for generating positive messages
- **Gmail SMTP** for sending emails
- **Python dotenv** for environment configuration

## Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd awesomeness_reminder
   ```

2. **Install dependencies**
   ```bash
   pipenv install
   ```

3. **Configure Ollama**
   - Ensure Ollama is running on your network

4. **Create environment file**
   Create a `.env` file with:
   ```
   OLLAMA_HOST=http://your-ollama-host:11434
   FROM_EMAIL=your-email@gmail.com
   GOOGLE_APP_PASSWORD=your-google-app-password
   ```

5. **Add recipients**
   Create a `recipients.txt` file with one email per line:
   ```
   recipient1@example.com
   recipient2@example.com
   ```

## Usage

Run the application:
```bash
pipenv run python main.py
```

The app will:
1. Generate an uplifting message using the LLM
2. Send the message to all recipients in `recipients.txt`

## Google App Password

To use Gmail SMTP, you need an App Password:
1. Enable 2-factor authentication on your Google account
2. Go to Google Account settings → Security → 2-Step Verification → App passwords
3. Generate a new app password for "Mail"
4. Use this password in your `.env` file

## Customization

Modify the prompt in `main.py` to change the type of messages generated.
