nome1 = input('\nEntre com o nome da primeira pessoa \n')
try:
    verifica_num =input('Olá %s, escolha um número\n' %nome1)
    qty_1 = int(verifica_num)
except:
    if len(verifica_num) == 0: #verifica se não entrou com informação
        print('Você preciso colocar algum número')
    else:
        print('Isso não parece um número válido')

nome2 = input('\nEntre com o nome da segunda pessoa \n')
qty_2 =input('Olá %s, escolha um número\n' %nome2)

