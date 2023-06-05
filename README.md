# Flask SMTP Email API

This repository contains a Flask API for sending emails through a specified SMTP server. The API accepts POST requests at the `/send_email` endpoint with a JSON body containing "to", "subject", and "body" fields to define the recipient, subject, and body of the email.

## Key Features

- Utilizes Flask to handle HTTP POST requests, allowing for the sending of emails via API calls.
- Accepts JSON payloads to set email recipient, subject, and body.
- Uses Python's built-in `smtplib` and `email` modules for constructing and sending the emails.
- Leverages the Google SMTP server for sending emails, with the email account details and the 'From' address stored securely in a `.env` file and loaded via `python-dotenv`.
- Validates API requests using a password sent in the HTTP headers (under 'X-API-KEY').

## Environment Setup and Required Variables

This project uses a Python virtual environment for managing dependencies. Create a new virtual environment in your project directory using:

```bash
python3 -m venv venv
```

Activate the virtual environment with:

```bash
source venv/bin/activate
```

Install the required Python packages with:

```
pip install -r requirements.txt
```

In order to configure your environment variables, make a copy of the .env-example file and rename it to .env. Then, update the variables in the .env file to match your settings:

```bash
cp .env-example .env
```

The file should include these variables:

SMTP_USERNAME: Your SMTP server username.

SMTP_PASSWORD: Your SMTP server password.

API_PASSWORD: The password required for making API calls.

FROM_ADDR: The 'From' address to be used in the emails.

## Deployment
This API is designed to run on an Ubuntu server, with the Flask built-in server listening on all interfaces on port 5000.
