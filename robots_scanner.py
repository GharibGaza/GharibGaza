import requests
import re
import argparse

logo = """\033[1;31m 
     ____                      _                     _           _   
    / ___|  ___  __ _ _ __ ___| |__        _ __ ___ | |__   ___ | |_ 
    \___ \ / _ \/ _` | '__/ __| '_ \ _____| '__/ _ \| '_ \ / _ \| __|
    ___) |  __/ (_| | | | (__| | | |_____| | | (_) | |_) | (_) | |_ 
    |____/ \___|\__,_|_|  \___|_| |_|     |_|  \___/|_.__/ \___/ \__|\n
     \033[0;34m[=] Exm: \n
        - python3 robots_scanner.py example.com\033[0;39m

        \033[0;31m- Exiting the program .... [Cutrl +C]\033[0;39m


\033[1;39m \n"""
                                                                 
print(logo)
parser = argparse.ArgumentParser(description='Robots.txt Scanner')
parser.add_argument('website', help='Target website')
args = parser.parse_args()

website = args.website

if not website.startswith("http://") and not website.startswith("https://"):
    website = "http://" + website

full_domain = website + "/robots.txt"

try:
    page = requests.get(full_domain).text

    hiddens = re.findall("Disallow: \S{1,}", page)

    for hidden in hiddens:
        link = f"[+] {website}{hidden[10:]}"
        print(link)
except:
    print("\033[0;31mExiting the program...\033[0;39m")
