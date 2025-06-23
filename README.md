# Awesomeness Reminder

A Python application that generates ~~uplifting messages~~ a short quip about AI eminetly destroying humanity using an LLM and sends them via email to a list of recipients. It supports both local LLM use with ollama or services like anthropic.

## Overview

This project uses:
- **LLM Providers**: Supports both Ollama (local) and Anthropic (Claude) for generating positive messages
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

3. **Configure LLM Provider**
   - For Ollama: Ensure Ollama is running on your network
   - For Anthropic: Get your API key from https://console.anthropic.com/

4. **Create environment file**
   Create a `.env` file with:
   ```
   # Email configuration
   FROM_EMAIL=your-email@gmail.com
   GOOGLE_APP_PASSWORD=your-google-app-password
   
   # LLM configuration
   LLM_PROVIDER=ollama  # or "anthropic"
   
   # Ollama settings
   OLLAMA_HOST=http://your-ollama-host:11434
   OLLAMA_MODEL=deepseek-r1:8b
   
   # Anthropic settings
   ANTHROPIC_API_KEY=your-anthropic-api-key
   ANTHROPIC_MODEL=claude-3-haiku-20240307  # or claude-3-sonnet-20240229, claude-3-opus-20240229
   ```

5. **Configure recipients**
   
   **Option 1: Using a file (for local development)**
   Create a `recipients.txt` file with one email per line:
   ```
   recipient1@example.com
   recipient2@example.com
   ```
   
   **Option 2: Using environment variable (for CI/CD)**
   Add to your `.env` file:
   ```
   RECIPIENTS=recipient1@example.com,recipient2@example.com
   ```
   
   Note: The environment variable takes precedence over the file.

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

## GitHub Actions Automation

The project includes a GitHub Actions workflow to run daily at 7:30 AM Eastern Time. To set it up:

1. Go to your repository Settings → Secrets and variables → Actions
2. Add these secrets:
   - `ANTHROPIC_API_KEY`: Your Anthropic API key
   - `FROM_EMAIL`: Your Gmail address
   - `GOOGLE_APP_PASSWORD`: Your Gmail app password
   - `RECIPIENTS`: Comma-separated list of email addresses

The workflow file is located at `.github/workflows/daily-reminder.yml`.

## Customization

Modify the prompt in `main.py` to change the type of messages generated.
