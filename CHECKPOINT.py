print('')
print('')
print("--------------------------")
print('CONSUMO DE ENERGIA MENSAL!')
print("--------------------------")

print('ATENÇÃO!!!\nTodos os valores serão avaliados em kWh. Selecione o tipo de terreno e a conta será automaticamente calculada de acordo com o seu gasto mensal. ')

retries = 11
terrenos = ['I','C','R']
    
for attempt in range(1, retries):   

    building = input('Por favor, digite o tipo da alocação/terreno (I,C ou R):\n(I) - Industrial\n(C) - Comércio\n(R) - Residência\n')
    building = building.upper()
    if (building not in terrenos):
        print('O valor selecionado não é valido.\n')
        continue

        # CODIGO PARA INDUSTRIA 

    elif (building == 'I'):
        print('Terreno selecionado: Indústria')
        userInput = float(input('Por favor, digite a taxa de consumo deste mês: '))

        if (isinstance(userInput, (float))):
        
            if (userInput >= 5000):
                print('O valor cobrado em sua Industria será:',userInput*0.70,'reais.')
                break

            elif (userInput <= 5000):
                print('O valor cobrado em sua Industria será:',userInput*0.65,'reais.')
                break
        else:
            print('Numero invalido. Reiniciando cobrador.\n')
            continue

        # CODIGO PARA RESIDENCIA

    elif (building == 'R'):
        print('Terreno selecionado: Residência')
        userInput = float(input('Por favor, digite a taxa de consumo deste mês: '))

        if (isinstance(userInput, (float))):
            if (userInput >= 500):
                print('O valor cobrado em sua residência será:',userInput*0.75,'reais.')
                break
            elif (userInput <= 500):
                print('O valor cobrado em sua residência será:',userInput*0.50,'reais.')
                break   
        else:
            print('Numero invalido. Reiniciando cobrador.\n')
            continue    
        # CODIGO PARA COMERCIO

    elif (building == 'C'):
        print('Terreno selecionado: Comercial')
        userInput = float(input('Por favor, digite a taxa de consumo deste mês: '))
    
        if (isinstance(userInput, (float))):
            if (userInput >= 1000):
                print('O valor cobrado em seu comércio será:',userInput*0.70,'reais.')
                break
            elif (userInput <= 500):
                print('O valor cobrado em seu comércio será:',userInput*0.65,'reais.')
                
                break                    
        else:   
            print('Numero invalido. Reiniciando cobrador.\n')
            continue  
        
if (attempt == 10 ):
    print('Você tentou muitas vezes! Tente novamente mais tarde')
  
else:
    print('')
    print('****************')        
    print('Fim do calculo!')
    print('****************')   
    print('')
