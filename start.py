#import modules
import os
import webbrowser
import json
import tkinter
from termcolor import colored

webbrowser.open('https://discord.com/developers/applications', new=1)

print("██████╗░██████╗░██╗░░░██╗███████╗██╗░░░░░░█████╗░░██████╗  ███╗░░██╗██╗░░░██╗██╗░░██╗███████╗██████╗░ ")
print("██╔══██╗██╔══██╗██║░░░██║██╔════╝██║░░░░░██╔══██╗██╔════╝  ████╗░██║██║░░░██║██║░██╔╝██╔════╝██╔══██╗ ")
print("██████╔╝██████╔╝██║░░░██║█████╗░░██║░░░░░███████║╚█████╗░  ██╔██╗██║██║░░░██║█████═╝░█████╗░░██████╔╝ ")
print("██╔═══╝░██╔══██╗██║░░░██║██╔══╝░░██║░░░░░██╔══██║░╚═══██╗  ██║╚████║██║░░░██║██╔═██╗░██╔══╝░░██╔══██╗ ")
print("██║░░░░░██║░░██║╚██████╔╝██║░░░░░███████╗██║░░██║██████╔╝  ██║░╚███║╚██████╔╝██║░╚██╗███████╗██║░░██║ ")
print("╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝")

token = input("inserisci il token del bot🤖: ")

with open("bot.json") as f:
        data = json.load(f)
        data["token"] = token
        json.dump(data, open("bot.json", "w"), indent = 4)

print("token: " + token)

install = os.system("npm i")

command = os.system("npm start")

webbrowser.open('http://localhost:3000', new=2)








