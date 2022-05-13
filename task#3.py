import sqlite3
import json
import requests

ip = input("შეიყვანეთ თქვენი აიპი მისამართი: ")
key = "0257c8e7198e899c78cbb42877242e74"
url = f"http://api.ipapi.com/{ip}?access_key={key}"



x = requests.get(url)
description = x.json()
print("ქვეყნის სახელი: ", description.get("country_name"))
print("საქვეყნო კოდი არის: ", description.get("country_code"))
print("არის თუ არა ევროპის ნაწილი : ", description.get("is_eu"))
print("სატელეფონო კოდი : ", description.get("calling_code"))
with open ('description.json', 'w') as file:
    json.dump(description, file, indent=4)
file.close()

y = requests.get(url)
info = y.json()
info_json = json.dumps(info, indent=4)
# print(info_json)


conn = sqlite3.connect('ip_addr.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS ip_addr
           (
            country_name VARCHAR(100),
            city VARCHAR(100)) ''')


list = []
for i in info:
    list.append(info[i])
Country = list[5]
City = list[8]
c.execute(f'''INSERT INTO ip_addr VALUES ('{Country}', '{City}')''')

conn.commit()
conn.close()