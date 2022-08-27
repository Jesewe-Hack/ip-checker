import requests
from pyfiglet import Figlet
import folium
import time
import colorama
import ctypes
import os
from colorama import init, Fore
init()
ctypes.windll.kernel32.SetConsoleTitleA("IP CHECKER | By Jesewe#8563")

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }
        for k, v in data.items():
            print(f'{k} : {v}')
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')
    except Exception as e:
        os.system("cls")
        print(Fore.RED + '[!] Error: Invalid character')
        
while True:
    os.system("cls")
    print(Fore.MAGENTA + 'Welcome to IP CHECKER', Fore.GREEN + 'By', Fore.RED + 'Jesewe#8563')
    try:
        ip = input(Fore.CYAN + '\nPlease enter a target IP: ')
    except Exception as e:
        os.system('cls')
        print(Fore.RED + '\n[!] Error: Invalid character')
        input(Fore.YELLOW + "\nPress Enter to exit the menu... ")
    else:
        print('\n')
        get_info_by_ip(ip=ip)
        input(Fore.YELLOW + "\nPress Enter to exit the menu... ")