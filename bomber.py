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
    |            \ ;                         never steal the code unless you know how it works...
                  ',
       \_         __\ 
         ''-_    \.//
           / '-____'
          /
        _'
      _-'
   ''')
banner()
print("DISCLAIMER: USE THIS TOOL AT YOUR OWN RISK..'\n' CREATORS OF THIS TOOL ARE NOT RESPONSIBLE FOR MISUSE OF THIS TOOL...")

print("1.whatsapp bomb")
print("2.sms bombing")
print("3.update me")
print("4.exit this shit")
a= int(input("what you want to do? : "))
if a== 1:
    print("installing requirements please be patient....")
    os.system("apt install urllib")
