#!/usr/bin/env python
#-*-coding:utf-8-*-
##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import smtplib
import random
MY_EMAIL="aaa@gmail.com"
MY_PASSWORD="ghljmecjebesxukt"
CSV_PATH="birthdays.csv"
PLACEHOLDER="[NAME]"
XXX="zzz"
YYY="yyy"
ZZZ="xxx"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
data=pandas.read_csv(CSV_PATH)
dictionary=data.to_dict(orient="records")


now=dt.datetime.now()
year=now.year
month=now.month
day=now.day

for x in dictionary:
    if x["name"]==ZZZ and x["day"]==day and x["month"]==month:
        with open("letter_templates/letter_4.txt","r") as letter_file:
            letter_contents=letter_file.read().rstrip()
            new_letter=letter_contents.replace(PLACEHOLDER,x["name"])
            # print(new_letter)
            emailSubject="Subject:Doğum Günün Kutlu Olsun Balim"
            emailContent=new_letter
            with smtplib.SMTP("smtp.gmail.com") as  connection:
                connection.starttls()
                connection.login(user=MY_EMAIL,password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=x["email"],
                    msg=(emailSubject+"\n\n"+emailContent).encode("utf-8")
                )
    elif x["name"]==YYY and x["day"]==day and x["month"]==month:
        with open("letter_templates/letter_5.txt") as letter_file:
            letter_contents=letter_file.read()
            new_letter=letter_contents.replace(PLACEHOLDER,x["name"])
            # print(new_letter)
            emailSubject="Subject:Birinci Yil Dönümümüz Kutlu Olsun"
            emailContent=new_letter

            with smtplib.SMTP("smtp.gmail.com") as  connection:
                connection.starttls()
                connection.login(user=MY_EMAIL,password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=x["email"],
                    msg=(emailSubject+"\n\n"+emailContent).encode("utf-8")
                )

    elif x["name"]==XXX and x["day"]==day and x["month"]==month:
        with open("letter_templates/letter_6.txt") as letter_file:
            letter_contents=letter_file.read()
            new_letter=letter_contents.replace(PLACEHOLDER,x["name"])
            # print(new_letter)
            emailSubject="Subject:İkinci Yil Dönümümüz Kutlu Olsun"
            emailContent=new_letter
            with smtplib.SMTP("smtp.gmail.com") as  connection:
                connection.starttls()
                connection.login(user=MY_EMAIL,password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=x["email"],
                    msg=(emailSubject+"\n\n"+emailContent).encode("utf-8")
                )

    elif x["day"]==day and x["month"]==month:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
            letter_contents=letter_file.read()
            new_letter=letter_contents.replace(PLACEHOLDER,x["name"])
            # print(new_letter)
            emailSubject="Subject:Doğum Günün Kutlu Olsun"
            emailContent=new_letter
            with smtplib.SMTP("smtp.gmail.com") as  connection:
                connection.starttls()
                connection.login(user=MY_EMAIL,password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=x["email"],
                    msg=(emailSubject+"\n\n"+emailContent).encode("utf-8")
                )
    




