from random import choice
from time import sleep

bos = {1: '\033[36mBoss-Rock ✊\033[m', 2: '\033[mBoss-Paper ✋', 3: '\033[33mBoss-Scissors ✌ \033[m'}
lis = [1, 2, 3]


def erro():
    print('Erro! Esse valor não é valido.')


while True:
    life = 3
    points = 0
    nick = str(input('Nick: '))
    nick = nick[:3]
    while life >= 1:
        mobs = choice(lis)
        print(f'\033[32m[1]{bos[1]} \033[32m[2]{bos[2]} \033[32m[3]{bos[3]}\033[31m')
        for heart in range(0, life):
            print('❤', end='')
        while True:
            player = input('\n\033[m>> ')
            try:
                int(player)
            except:
                erro()
            else:
                player = int(player)
                if player > 3:
                    erro()
                else:
                    break
        sleep(0.3)
        print(' \033[31mJO\033[m')
        sleep(1)
        print(' \033[33mKEN\033[m')
        sleep(1)
        print(' \033[32mPO!!!\033[m\n')

        print('-=' * 10)
        print(f' Player: {bos[player]}\n CPU: {bos[mobs]}')
        print('-=' * 10)

        if player == 1:
            if mobs == 1:
                print(' \033[33mDRAW\033[m')

            elif mobs == 2:
                life -= 1
                print(' life \033[31m-1\033[m')

            elif mobs == 3:
                points += 20
                print(' \033[32mPoints +20\033[m')

        elif player == 2:
            if mobs == 3:
                life -= 1
                print(' Life \033[31m-1\033[m')

            elif mobs == 2:
                print(' \033[33mDraw\033[m')

            elif mobs == 1:
                points += 20
                print(' \033[32mPoints + 20')

        elif player == 3:
            if mobs == 2:
                points += 20
                print(' \033[32mPoints +20\33[m')

            elif mobs == 1:
                life -= 1
                print(' life \033[31m-1\033[m')

            elif mobs == 3:
                print(' \033[33mDraw\033[m')
        input()
    print('___' * 10)
    print(f' Player: {bos[player]}\n CPU: {bos[mobs]}')
    print('___' * 10)
    print(f' \033[33mPoints total: {points}\n \033[31mGAME OVER!\033[m\n ')
    print('''	~RANK~	''')
    input()
