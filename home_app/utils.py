from navbar_app.models import OneNavbar, TwoNavbar, ThreeNavbar
import requests

def get_navbars():
    one_navbars = OneNavbar.objects.all()
    two_navbars = TwoNavbar.objects.all()
    three_navbars = ThreeNavbar.objects.all()

    return {
        'one_navbars': one_navbars,
        'two_navbars': two_navbars,
        'three_navbars': three_navbars
    }

def send_message(token, chat_id, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'HTML'
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print('Message sent successfully')
    else:
        print('Failed to send message')
        print(response.json())

