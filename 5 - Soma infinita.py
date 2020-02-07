print('\n=========================================')
print('\nDigite os números a serem somados')
print('Quando quiser somar pressione a tecla 0\n')
print('=========================================')


n = float(input(':'))
total =n
while n !=0: #comando de interação podemos usar while n
    n = float(input(':'))
    if n <0:
        n =0
    elif n>9:
        n=0
    
    total = total +n
    
    
print('Total = %s' %total)
    