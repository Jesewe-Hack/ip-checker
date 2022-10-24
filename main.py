import requests
from pyfiglet import Figlet
import folium
import time
import colorama
import ctypes
import os
import socket
from colorama import init, Fore
init()
ctypes.windll.kernel32.SetConsoleTitleW('IP CHECKER | By Jesewe Hack')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
            print(bcolors.OKCYAN + f'                                    {k} : {v}')
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')
    except Exception as e:
        os.system("cls")
        print(bcolors.FAIL + '                                    [!] Error: Invalid character')

banner="""
                                    ▪   ▄▄▄·     ▄▄·  ▄ .▄▄▄▄ . ▄▄· ▄ •▄ ▄▄▄ .▄▄▄  
                                    ██ ▐█ ▄█    ▐█ ▌▪██▪▐█▀▄.▀·▐█ ▌▪█▌▄▌▪▀▄.▀·▀▄ █·
                                    ▐█· ██▀·    ██ ▄▄██▀▐█▐▀▀▪▄██ ▄▄▐▀▀▄·▐▀▀▪▄▐▀▀▄ 
                                    ▐█▌▐█▪·•    ▐███▌██▌▐▀▐█▄▄▌▐███▌▐█.█▌▐█▄▄▌▐█•█▌
                                    ▀▀▀.▀       ·▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀
"""
while True:
    os.system("cls")
    print(bcolors.OKGREEN + banner)
    print(bcolors.OKBLUE + """
                                [ Made by Jesewe Hack : https://github.com/Jesewe-Hack ]
    """ + bcolors.ENDC)
    try:
        print(Fore.YELLOW + "                                                Your IP: " + socket.gethostbyname(socket.gethostname()))
        ip = input(bcolors.OKBLUE + '\n                                  Please enter a target IP: ')
    except Exception as e:
        os.system('cls')
        print(bcolors.FAIL + '\n                                    [!] Error: Invalid character')
        input(Fore.OKGREEN + "\n                                    Press Enter to exit the menu... ")
    else:
        print('')
        get_info_by_ip(ip=ip)
        input(bcolors.OKGREEN + "\n                                    Press Enter to exit the menu... ")
