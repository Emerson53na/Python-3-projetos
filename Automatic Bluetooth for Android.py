from datetime import datetime
from os import system
from time import sleep
import androidhelper

system('clear')

print('''     =                            =
          AUTOMATIC \033[36mBluetooth \033[m
     =                            =''')

on = str(input('[on/off] ')).lower().strip()[:2]
hora = int(input(' Hour: '))
minuto = int(input(' Minute: '))

while True:
 now = datetime.now()       
 system('clear')
 
 if hora == now.hour and minuto == now.minute:
     if on in 'on':
         droid = androidhelper.Android()
         droid.toggleBluetoothState(True)
         print(' \033[32mBluetooth On\033[m')
         exit()
         
     if on in 'of':
         droid = androidhelper.Android()
         droid.toggleBluetoothState(False)
         print(' \033[31mBluetooth off\033[m')
         exit()
     
 else:
     print(f' \033[36m{now.hour}h {now.minute}m {now.second}s\033[m')
     sleep(1.0)
