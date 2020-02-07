#entra com duas pessoas e a quantidade de moedas que cada uma tem, depois diz qual é a pessoa e quantas moedas a mais ela tem
print('\n'*2)# pula duas linha
print('Mostra quem tem mais moedas')
print('\n')# pula uma linha

nome1 = input('Nome da primeira pessoa \n')
nome2 = input('Nome da segunda pessoa \n')

pess1 = int(input('Entre com a quantidade de moedas de %s \n' %nome1)) # declaramos pess1 como int assim que usamos o input, 
pess2 = int(input('Entre com a quantidade de moedas de %s \n' %nome2)) # assim diminuimos a qty de declarações


if pess1 > pess2:
    qty = pess1 - pess2
    print('%s tem %s moedas a mais que %s ' %(nome1, qty ,nome2))
else:
    if pess1 < pess2:
        qty = pess2 - pess1
        print('A segunda pessoa tem  %s moedas a mais que a primeira ' %qty)
    else:
        if pess1 == pess2:
            pess3 = pess1
            print('As duas têm a mesma quantidade de moedas: %s' %pess3)
            
            
# verificar se a quantidade de moedas é um número
# verificar se o nome não tem números
# limpar a tela
#fazer o mesmo usando o comando elif
            