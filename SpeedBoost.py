  # \033[1;40;31m    \033[1;32;40m

import os
import sys
import time
import random

os.system("clear")
print()
print()
print()


print("""\033[1;32;40m                                    
                                                                                   
                                                      
                          °°°   bbbbb     
                          |||   bb   b     
                          |||   bbbbbb               
                          |||   bb   bb                   
                          |||   bb   bb    
                          |||   bbbbbbb    
                      __________________   
                       ɪɴᴛᴇᴿɴᴇᴛ ʙᴏᴏsᴛᴇᴿ    
                                                                                    
                                      """)
print()
#        coded by RetroAk

print('''\033[1;32;36m                      TOOᒪ ᗷY RetroAk
                                    https://github.com/RetroAk/
''')


print("\n\n\n")

name = input("\033[1;32;40m  [+]  [y] to start setup \n       [n] to cancel  " "\033[1;40;31m <<  [y/n] >>  ")

if name == 'n':
        print("\033[1;40;31m          \n [+] cancelled ")
        exit()

if name == 'y':
       os.system("pkg install python -y && pip install speedtest-cli -y ")
       os.system("clear")
       op = input("\033[1;40;31m \n\n\n DO YOU WANT TO START BOOSTING ?  << [y/n] >>  ")


if op == 'y':
         os.system("clear")
         os.system("speedtest-cli")
         exit()

if op == 'n':
          print("\033[1;40;31m \n cancelled ")
          exit()
else:
    print("\033[1;40;31m \n error character \n ")
    exit()
