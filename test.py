import datetime as dt
import smtplib
from random import *
QUETES_PATH="day32SendEmail\\quotes.txt"
MY_EMAIL="cemboraceylan19@gmail.com"
MY_PASSWORD="ghljmecjebesxukt"

now=dt.datetime.now()
weekday=now.weekday()

if weekday==1:
    with open(QUETES_PATH) as quetes_file:
        all_quetes=quetes_file.readlines()
        quetes=choice(all_quetes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Tuesday Motivation\n\n{quetes}"
        )