from random import choice
from time import sleep

rank1 = rank2 = rank3 = 0

bos = {1: '\033[36mRock-Bos\033[m', 2 : '\033[mRole-Bos', 3 : '\033[33mScissors-Bos \033[m'}
lis = [1, 2, 3]

while True:
    life = 3
    spots = 0
    nick = str(input('Nick: '))
    nick = nick[:3]
    while life >= 1:
        mobs = choice(lis)
        player = int(input(f'\n \033[32m[1]{bos[1]} \033[32m[2]{bos[2]} \033[32m[3]{bos[3]}\n \033[31mLife = {life}\033[m\n\n >> '))
        sleep(1)
        print (' \033[31mJO\033[m')
        sleep(1)
        print(' \033[33mKEN\033[m')
        sleep(1)
        print(' \033[32mPO!!!\033[m\n')
    
        print('-='*10)
        print(f' Player: {bos[player]}\n CPU: {bos[mobs]}')
        print('-='*10)
   
    
        if player == 1:
            if mobs == 1:
                print(' \033[33mDRAW\033[m')
                
            elif mobs == 2:
                life -= 1
                print(' life \033[31m-1\033[m')
            
            elif mobs == 3:
                spots += 20
                print(' \033[32mPoints +20\033[m')
    
        elif player == 2:
            if mobs == 3:
                life -= 1
                print(' Life \033[31m-1\033[m')
            
            elif mobs == 2:
                print(' \033[33mDraw\033[m')
         
            elif mobs == 1:
                spots += 20
                print(' \033[32mPoints + 20')
            
        elif player == 3:
            if mobs == 2:
                spots += 20
                print(' \033[32mPoints +20\33[m')
            
            elif mobs == 1:
                life -= 1
                print(' life \033[31m-1\033[m')
            
            elif mobs == 3:
                print(' \033[33mDraw\033[m')
        input()
    print('-='*10)
    print(f' Player: {bos[player]}\n CPU: {bos[mobs]}')
    print('-='*10)    
    print(f' \033[33mtotal points = {spots}\n \033[31mGamer Over!\033[m\n ')
    print('''
    	~~RANK~~
    	''')
    
    input()
