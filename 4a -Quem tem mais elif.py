print('\n Verifica quem tem mais moedas \n')

nome1 = input('Entre com o nome da primeira pessoa\n')
nome2 = input('Entre com o nome da segunda pessoa\n')

p1 = int(input('Qual a quantidade de moedas de %s\n' %nome1))
p2 = int(input('Qual a quantidade de moedas de %s\n' %nome2))

print('\n%s tem %s moedas e %s tem %s moedas \n' %(nome1, p1,nome2, p2))

if p1 > p2:

    resul = p1 - p2
    print('Portanto %s tem %s moedas a mais que %s\n' %(nome1, resul, nome2))

elif p1 < p2:

    resul = p2 -p1
    print('Portanto %s tem %s moedas a mais que %s\n' %(nome2, resul, nome1))

elif p1 == p2:
        
    print('Portanto %s e %s têm a mesma quantidade de moedas!\n' %(nome1, nome2))    
