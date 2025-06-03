from flask import Flask, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = f"User deleted a file:\n\n{data}"
    send_email("raja.l@asian-technology.com", "File Deletion Alert", message)
    return '', 204

def send_email(to, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "raja.l@asian-technology.com"
    msg['To'] = to

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("raja.l@asian-technology.com", "evpi pnkc ohiy gjiv")
    server.send_message(msg)
    server.quit()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
