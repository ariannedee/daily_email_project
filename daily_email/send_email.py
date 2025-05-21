import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# from environs import Env


# env = Env()
# env.read_env()
SENDER_EMAIL = 'test@gmail.com' # env('SENDER_EMAIL')
PASSWORD = '' # env('GMAIL_PWD')

SENDER_NAME = 'Python email bot' # env('SENDER_NAME', default='Daily email')
RECEIVER_EMAIL = '' # env('RECEIVER_EMAIL', default=SENDER_EMAIL)
RECEIVER_NAME = 'Arianne' # env('RECEIVER_NAME', default='Me')


def send_text_email(subject, content):
    message = f"""\
From: {SENDER_NAME} ({SENDER_EMAIL})
To: {RECEIVER_NAME}
Subject: {subject}

{content}
"""
    if not SENDER_EMAIL or not PASSWORD:
        print(message)
    else:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(SENDER_EMAIL, PASSWORD)
        smtpObj.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)
        smtpObj.quit()


def send_html_email(subject, content):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(SENDER_EMAIL, PASSWORD)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = f'{SENDER_NAME} ({SENDER_EMAIL})'
    msg['To'] = f'{RECEIVER_NAME} {RECEIVER_EMAIL}'

    as_str = content.replace('<br>', '\n')
    as_str = re.sub('</?.+>', '', as_str)

    html = f"""\
    <html>
      <head></head>
      <body>
        {content}
      </body>
    </html>
    """

    part1 = MIMEText(as_str, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    smtpObj.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
    smtpObj.quit()
