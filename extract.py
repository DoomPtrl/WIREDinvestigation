import requests
from bs4 import BeautifulSoup
import time
import os

folder_path = 'C:\\Users\\user\\Desktop\\성대수업\\WIRED\\WIRED_htmls'

if not os.path.isdir(folder_path):
    os.mkdir(folder_path)

with open('C:\\Users\\user\\Desktop\\성대수업\\WIRED\\skipped.txt', 'r') as file:
    lines = file.readlines()
skipped = [int(line.strip()) for line in lines]

pgnum = len(os.listdir(f"{folder_path}")) + len(skipped)
if not pgnum:
    pgnum = 1

while True:
    try:
        html = requests.get(
            f"https://www.wired.com/most-recent/?page={pgnum}").content
        soup = BeautifulSoup(html, "html.parser")
        if soup.select_one("#main-content > div > div > div > div > div > header > div > h1"):
            skipped.append(pgnum)
            if len(skipped)>3 and skipped[-1] - skipped[-2] == 1 and skipped[-2] - skipped[-3] == 1:
                break
            with open('C:\\Users\\user\\Desktop\\성대수업\\WIRED\\skipped.txt', 'w+') as file:
                for number in skipped:
                    file.write(str(number) + '\n')
            pgnum += 1 
            continue
        with open(f"{folder_path}/{pgnum}", "w+b") as fw:
            fw.write(html)
        pgnum += 1
    except Exception as e:
        print(f"Error occured: {e}")
        time.sleep(60)
        continue
