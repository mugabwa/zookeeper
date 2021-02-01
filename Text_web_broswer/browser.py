# write your code here
import sys
import os
import collections
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style

argument = sys.argv
stack = collections.deque()
if os.access(argument[1], os.F_OK):
    pass
else:
    os.mkdir(argument[1])
while True:
    url = input()
    urls = url
    if "." in url:
        if url.startswith("2.") or url.startswith("en."):
            url = "https://" + url
        elif url.startswith("www."):
            urls = urls.replace("www.", "")
            url = url.replace("www.", "https://www.")
        elif url.startswith("https://"):
            urls = urls.replace("https://www.", "")
        else:
            url = url.replace(url, "https://www." + url)
        r = requests.get(url)
        if 200 <= r.status_code < 400:
            tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']
            soup = BeautifulSoup(r.content, 'html.parser')
            val = soup.find_all(tags)
            for vals in val:
                if vals.get('href'):
                    print(Fore.BLUE + vals.get_text())
                else:
                    print(vals.get_text())
            x = urls.split(".")
            if len(x) == 2:
                y = x[0]
            elif len(x) > 2:
                y = x[0] + "_"+x[1]
            else:
                y = x[0]
            path = argument[1] + "\\" + y
            with open(path, 'w', encoding='utf-8') as f1:
                for valr in val:
                    f1.write(valr.get_text())
            stack.append(path)

        elif 400 <= r.status_code < 500:
            print("Error: Client side error")
        else:
            print("Error: serverside error")
    elif url == "exit":
        break
    elif url == 'back':
        if len(stack) <= 1:
            pass
        else:
            stack.pop()
            fil = stack.pop()
            with open(fil, 'r', encoding='utf-8') as f2:
                print(f2.readlines())
            stack.append(fil)
    else:
        print("Error: Incorrect URL")
