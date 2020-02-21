from time import sleep
import requests
import smtplib
from email.message import EmailMessage

url = "https://wtfismyip.com/text"
time_between_checks = 10 * 60  # in seconds
send_from = "ipNotifier@gerapi.com"
send_to = "itaygera@gmail.com"


def send_mail(my_ip):
    msg = EmailMessage()
    msg.set_content(f'Hey\nThe ip changed to {my_ip}\nBest regards me')
    msg['Subject'] = f'The ip changed to {my_ip}'
    msg['From'] = send_from
    msg['To'] = send_to

    # Send the message via our own SMTP server.
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()


def main():
    my_ip = ""

    while True:
        resp = requests.get(url=url)
        cur_ip = resp.text.strip()
    if my_ip != cur_ip:
        my_ip = cur_ip
        send_mail(my_ip)
    sleep(time_between_checks)


if __name__ == "__main__":
    main()
