from random import choice
from time import sleep

boss = {1: '\033[36mBoss-Rock ✊\033[m', 2: '\033[mBoss-Paper ✋', 3: '\033[33mBoss-Scissors ✌ \033[m'}
lis = [1, 2, 3]


def erro():
    print('Error! This value not valid.')


def line():
    print('-'*30)


rank1 = rank2 = rank3 = 0
nick1 = nick2 = nick3 = ''
while True:
    life = 32
    points = 0
    while life >= 1:
        mobs = choice(lis)
        while True:
            print(f'\033[32m[1]{boss[1]} \033[32m[2]{boss[2]} \033[32m[3]{boss[3]}\033[31m')
            for heart in range(0, life):
                print('❤', end='')
            move = input('\n\033[m>> ')
            try:
                int(move)
            except:
                erro()
            else:
                move = int(move)
                if move < 1 or move > 3:
                    erro()
                else:
                    break
        sleep(0.3)
        print(' \033[31mJO\033[m')
        sleep(1)
        print(' \033[33mKEN\033[m')
        sleep(1)
        print(' \033[32mPO!!!\033[m\n')

        line()
        print(f' Player: {boss[move]}\n CPU: {boss[mobs]}')
        line()

        if move == 1:
            if mobs == 1:
                print(' \033[33mDRAW\033[m')
            elif mobs == 2:
                life -= 1
                print(' life \033[31m-1\033[m')
            elif mobs == 3:
                points += 20
                print(' \033[32mPoints +20\033[m')
        elif move == 2:
            if mobs == 3:
                life -= 1
                print(' Life \033[31m-1\033[m')
            elif mobs == 2:
                print(' \033[33mDraw\033[m')
            elif mobs == 1:
                points += 20
                print(' \033[32mPoints + 20')
        elif move == 3:
            if mobs == 2:
                points += 20
                print(' \033[32mPoints +20\33[m')
            elif mobs == 1:
                life -= 1
                print(' life \033[31m-1\033[m')
            elif mobs == 3:
                print(' \033[33mDraw\033[m')
        input()
    line()
    print(f' Player: {boss[move]}\n CPU: {boss[mobs]}')
    line()
    print(f' \033[33mPoints total: {points}\n \033[31mGAME OVER!\033[m\n ')
    print('''	~RANK~	''')
    nick0 = str(input('Nick:\033[32m'))
    nick0 = nick0[:3]
    if points > rank1:
        if rank1 == 0:
            rank1 = points
            nick1 = nick0
        else:
            nick3 = nick2
            rank3 = rank2
            nick2 = nick1
            rank2 = rank1
            nick1 = nick0
            rank1 = points

    elif points > rank2:
        if rank2 == 0:
            nick2 = nick0
            rank2 = points
        else:
            nick3 = nick2
            rank3 = rank2
            nick2 = nick0
            rank2 = points

    elif points > rank3:
        if rank3 == 0:
            nick3 = nick0
            rank3 = points
        else:
            nick3 = nick0
            rank3 = points
    line()
    print(f'''|Rank  Score  name
|1ST:  {nick1:5}: {rank1:5}
|2ND:  {nick2:5}: {rank2:5}
|3ND:  {nick3:5}: {rank3:5}''')
    line()
    input()
