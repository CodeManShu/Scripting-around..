import os
import sys
import calendar
import datetime
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'
def banner():
    print(G + '''
    
____  ___        __________________ __________ 
\   \/  /        \______   \_____  \\______   \ 
 \     /   ______ |     ___//   |   \|     ___/
 /     \  /_____/ |    |   /    |    \    |    
/___/\  \         |____|   \_______  /____|    
      \_/                          \/          @yuva
                                               @codemanshu
       / \      _-'
     _/|  \-''- _ /
__-' { |          \ 
    /             \ 
    /       "o.  |o }
    |            \ ;                         Never steal the code unless you know how it works...
                  ',                         Do not try at home..
       \_         __\
         ''-_    \.//
           / '-____'
          /
        _'
      _-'
   ''')
banner()
print("DISCLAIMER: USE THIS TOOL AT YOUR OWN RISK..'\n' CREATORS OF THIS TOOL ARE NOT RESPONSIBLE FOR MISUSE OF THIS TOOL...")

print("1.Whatsapp Bomb")
print("2.SMS Bombing")
print("3.Update Me")
print("4.Exit this shit")
a = int(input("What you want to do? : "))
if a == 1:
  print("installing requirements please be patient...")
  os.system("apt install urllib")
else:
  print('You messed up check whats wrong..')