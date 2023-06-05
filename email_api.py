from flask import Flask, request, jsonify
from dotenv import load_dotenv 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

load_dotenv()

app = Flask(__name__)  # Flask application instance

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    headers = request.headers

    # Check API password
    api_password = os.getenv('API_PASSWORD')
    provided_password = headers.get('X-API-KEY')

    if provided_password != api_password:
        abort(401, description='Unauthorized: Incorrect API password')

    fromaddr = os.getenv('FROM_ADDR')
    toaddr = data.get('to')
    subject = data.get('subject')
    body = data.get('body')
    username = os.getenv('SMTP_USERNAME')
    password = os.getenv('SMTP_PASSWORD')

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(username, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        return jsonify({"status": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"status": "Failed", "error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
