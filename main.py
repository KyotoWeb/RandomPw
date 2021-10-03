from pystyle import Colorate, Colors
from pycenter import center
from os import name, system
import random




def clear():
	system("cls" if name == 'nt' else "clear")


if name =='nt':
	system("title RandomPw & mode 190, 40 ")




banner = """\n

 ██▀███   ▄▄▄       ███▄    █ ▓█████▄  ▒█████   ███▄ ▄███▓ ██▓███   █     █░
▓██ ▒ ██▒▒████▄     ██ ▀█   █ ▒██▀ ██▌▒██▒  ██▒▓██▒▀█▀ ██▒▓██░  ██▒▓█░ █ ░█░
▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌▒██░  ██▒▓██    ▓██░▓██░ ██▓▒▒█░ █ ░█ 
▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌▒██   ██░▒██    ▒██ ▒██▄█▓▒ ▒░█░ █ ░█ 
░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░░▒████▓ ░ ████▓▒░▒██▒   ░██▒▒██▒ ░  ░░░██▒██▓ 
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░▒▓▒░ ░  ░░ ▓░▒ ▒  
  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒   ░ ▒ ▒░ ░  ░      ░░▒ ░       ▒ ░ ░  
  ░░   ░   ░   ▒      ░   ░ ░  ░ ░  ░ ░ ░ ░ ▒  ░      ░   ░░         ░   ░  
   ░           ░  ░         ░    ░        ░ ░         ░                ░    
                               ░                                            
      by K Y O T O
"""


print(Colorate.Vertical(Colors.blue_to_cyan, center(banner, space=60 ), stop=20))




chars = "abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMONPQRSTUVWXYZ1234567890!$^(')"


while 1:
	password_len = int(input((Colorate.Horizontal(Colors.purple_to_blue, "what lenght would you like your password to be : "))))
	password_count = int(input((Colorate.Horizontal(Colors.purple_to_blue, "How many passwords would you like : "))))
	for x in range(0,password_count):
		password = ""
		for x in  range(0,password_len):
			passsword_char = random.choice(chars)
			password       = password + passsword_char
		print("Here is your password :", password)	