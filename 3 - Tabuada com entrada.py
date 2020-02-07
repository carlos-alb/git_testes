#os comandos e funções usados aqui são para o python 3.0, não funcionando para o python 2.0
num = input('Entra com a tabuada a ser feita\n\n')
resul =0
#resul =int(num)* int(vezes)
print('-'*13)

for vezes in range(1,11):  
    resul = int(vezes) * int(num)
    print('%s x %02s = %2s' %( num, vezes, resul)) #int são mostrados como strings por isso o %s

print('-'*13)
    
# o %s transforma o número em string para ser mostrado na tela
# se não definirmos que "vezes" e "num" são do tipo int, o compilador os considerará como string
#int(vezes) - para "vezes" ser uma int 