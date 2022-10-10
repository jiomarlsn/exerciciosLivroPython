def prog1():
    # 3.3 - Variaveis do tipo logico
    resultado = True
    aprovado = False


def prog2():
    # 3.3.1 - Operadores relacionais
    a = 1
    b = 5
    c = 2
    d = 1
    print('a == b ', a == b)
    print('b > a ', b > a)
    print('a == d ', a == d)
    print('b >= a ', b >= a)
    print('c <= b ', c <= b)
    print('d != a ', d != a)
    print('d != b ', d != b)


def prog3():
    # 3.3.2.1 - Operador not
    print(not True)
    print(not False)


def prog4():
    # 3.3.2.2 - Operador and
    print(True and True)
    print(True and False)
    print(False and True)
    print(False and False)


def prog5():
    # 3.3.2.3 - Operador or
    print( True or True)
    print(True or False)
    print(False or True)
    print(False or False)


def prog6():
    # Expressoes logicas
    print('''
    True or False and not True
    True or False and False
    True or False
    True
    ''')
    salario = 1500
    idade = 18
    print('salario > 1000 and idade > 18 = ', salario > 1000 and idade > 18)


def prog7():
    # 3.4 - Variaveis Strings
    print(len('A'))
    print(len('AB'))
    print(len(''))
    print(len('O rato roeu a roupa'))

    print('\n')

    a = 'ABCDEF'
    print(a[0])
    print(a[1])
    print(a[5])
    print('Tamanho de a: ', len(a))
    print(a[6])


def prog8():
    # 3.4.1 Operações com Strings
    s = "ABC"
    print(s + "C")
    print(s + "D" * 4)
    print('X' + '-' * 10 + 'X')
    print(s + 'x4= ' + s * 4 )


def prog9():
    # 3.4.1.2 - Compisição
    idade = 22
    print("[%d]" % idade)
    print("[%03d]" % idade)
    print("[%3d]" % idade)
    print("[%-3d]" % idade)
    print('\n')
    print('%5f' % 5)
    print('%5.2f' % 5)
    print('%10.5f' % 5)

    print('\n Forma Antiga de usar composição\n')
    nome = 'joão'
    idade = 22
    grana = 51.34
    print("%s tem %d anos e R$%f no bolso." % (nome, idade, grana))
    print("%12s tem %3d anos e R$%5.2f no bolso." % (nome, idade, grana))
    print("%12s tem %03d anos e R$%5.2f no bolso." % (nome, idade, grana))
    print("%-12s tem %-3d anos e R$%-5.2f no bolso." % (nome, idade, grana))

    print('\n Composição com o .format\n')
    print('{} tem {} anos e R${} no bolso'.format(nome, idade, grana))
    print('{:12} tem {:3} anos e R${:5.2f} no bolso'.format(nome, idade, grana))
    print('{:12} tem {:03} anos e R${:5.2f} no bolso'.format(nome, idade, grana))
    print('{:<12} tem {:<3} anos e R${:5.2f} no bolso'.format(nome, idade, grana))

    print('\n Composição com o f-String\n')
    print(f'{nome} tem {idade} anos e R${grana} no bolso')
    print(f'{nome:12} tem {idade:3} anos e R${grana:5.2f} no bolso')
    print(f'{nome:12} tem {idade:03} anos e R${grana:5.2f} no bolso')
    print(f'{nome:<12} tem {idade:<3} anos e R${grana:5.2f} no bolso')




prog9()