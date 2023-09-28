import sys

from apis.weather import get_message as weather_message
from apis.reminders import get_message as reminder_message

SEND_EMAIL = False


def get_name():
    if len(sys.argv) > 1:
        name = " ".join(sys.argv[1:]).strip().title()
    else:
        name = 'Arianne'
    return name


def get_email_contents():
    content = f"""Hello {get_name()},
    
{weather_message()}
    
{reminder_message()}"""

    return content


if __name__ == '__main__':
    email_content = get_email_contents()

    print(email_content)

    if SEND_EMAIL:
        from send_email import send_text_email
        send_text_email(subject='Daily email', content=email_content)
