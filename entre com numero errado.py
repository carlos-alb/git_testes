print('\nTestando a verificação de erros com o except ')

tmnh =40
tmnh_2 =50
testando =1 # Para evitar erro ao se colocar uma letra no 

while 1:#loop pseudo infinito, pois temos um break em algum lugar
    
    try:
        testando = input(':')
        num = float(testando)#esse float faz o interpretador esperar um número inteiro ou um número com decimoso separados por .
                           #qualquer coisa fora disso é um erro

    except:
        if len(testando) ==0:
        
            print('você saiu do programa')
            break # encerra o programa
        
        elif ',' in testando: #verifica se em algum ponto do que entrou tem um vírgula
        
            print('='*tmnh_2)
            print('\nvocê deve colocar um . para separar os décimos\n')
            print('='*tmnh_2)
            print('\nO último número digitado foi %s\n' %num)
        
        else:
            
            print('='*tmnh)
            print('\nIsso não parece ser um número válido\n')   
            print('='*tmnh)
            print('\nO último número digitado foi %s\n' %num)            
    
    print(num)