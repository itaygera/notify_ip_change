from time import sleep, localtime
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
    print("Connecting to SMTP server")
    s = smtplib.SMTP('localhost:8025')
    print(f'Sending email to {send_to}, from {send_from}')
    s.send_message(msg=msg)
    s.quit()


def main():
    my_ip = ""

    while True:
        ltime = localtime()
        resp = requests.get(url=url)
        cur_ip = resp.text.strip()
        timestamp = f'{ltime.tm_mday}/{ltime.tm_mon}/{ltime.tm_year}'
        timestamp += f' {ltime.tm_hour}:{ltime.tm_min}'
        print(f'[{timestamp}] the cur ip is {cur_ip}')
        if my_ip != cur_ip:
            print('The ip address have been changed')
            print(f'The old ip was {my_ip}, and the new is {cur_ip}')
            my_ip = cur_ip
            send_mail(my_ip)
        sleep(time_between_checks)


if __name__ == "__main__":
    print("Start")
    main()
    print("End")
