 
print('Digite os valores a somar seguidos de [ENTER].')
print('Para encerrar apenas [ENTER].')

total = 0

while 1: #fica no loop até encontrar um "break"
    try: #verifica se é possível fazer o que está dentro do  try
        linha = input(':')
        n = float(linha)
        total = total + n
        
    except:
        if len(linha) == 0:
        
            break # qualquer coisas que não conseguir ser transformada em float, sai do loop
        
        elif ',' in linha:
            print( 'Use o . (ponto) como separador decimal.')
        else:
           print ('Isso nao parece um numero valido.')
        
    print('TOTAL: %s' % total)
    
    