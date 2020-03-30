# Python-3-projetos

delta = {1 : 'I',  2 : 'II', 3 : 'III', 4 : 'IV', 5 : 'V', 6 : 'VI', 7 : 'VII', 8 : 'VIII', 9 : 'IX',
          10 : 'X', 20 : 'XX', 30 : 'XXX', 40 : 'XL' , 50 : 'L', 60 : 'LX', 70 : 'LXX' , 80 : 'LXXX', 90 : 'XC',
          100 : 'C', 200 : 'CC', 300 : 'CCC', 400 : 'CD', 500 : 'D', 600 : 'DC', 700 : 'DCC', 800 : 'DCCC', 900 : 'CM',
          1000 : 'M', 2000 : 'MM', 3000 : 'MMM'}


while True:
    opc = str(input('\n>> '))
    le = len(opc)
             
    if le == 1:
        print(delta[int(opc)])
                          
    elif le == 2:
        print(delta[int(opc[0]) * 10], end='')
        if int(opc[1]) >= 1:
            print( delta[ int( opc[1] ) ] )

    elif le == 3:
        print(delta[int(opc[0]) * 100] , end='')
        if int(opc[1]) >= 1:
            print(delta[int(opc[1]) * 10], end='')
        if int(opc[2]) >= 1:
            print(delta[int(opc[2])])

    elif le == 4:
        print(delta[int(opc[0]) * 1000], end='')
        if int(opc[1]) >= 1:
            print(delta[int(opc[1]) * 100], end='')
        if int(opc[2]) >= 1:
            print(delta[int(opc[2]) * 10], end='')
            
        if int(opc[3]) >= 1:
            print(delta[int(opc[3])])
