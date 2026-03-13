import requests
from bs4 import BeautifulSoup
import os

webhook = "YOUR_DISCORD_WEBHOOK"

def send_discord(message):
    data = {"content": message}
    requests.post(webhook, json=data)

with open("urls.txt", "r") as f:
    urls = f.readlines()

for url in urls:

    url = url.strip()

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.text

    file_name = url.replace("https://", "").replace("/", "_") + ".txt"

    if os.path.exists(file_name):

        with open(file_name, "r", encoding="utf-8") as f:
            last_title = f.read()

        if last_title != title:
            print(url + " 更新されました")
            send_discord(url + " が更新されました")

        else:
            print(url + " 変化なし")

    else:
        print(url + " 初回保存")

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(title)