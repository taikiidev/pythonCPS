#Exercicio 3 

produtos=           ["A", "B", "C", "D", "E", "F", "G"]
vendas_janeiro=     [150, 200, 100, 300, 250, 230, 250] 
vendas_fevereiro=   [120, 180, 150, 280, 200, 210, 240]
vendas_marco=       [200, 220, 170, 320, 250, 230, 315]
vendas_abril=       [180, 215, 185, 290, 250, 410, 390]

# Definindo o total de vendas iniciais de cada produto para facilitar posteriormente

a_inicial = 150
b_inicial = 200
c_inicial = 100
d_inicial = 300
e_inicial = 250
f_inicial = 230
g_inicial = 250

# Como o código está extenso, criei duas funções pra deixar mais simples

# Funçao para calcular as vendas totais de uma lista. Por exemplo se eu digitar vendas janeiro, terei todos os valores de janeiro somados.

def calcular_vendas (lista):
    soma = 0
    for index in lista[1:]:
        soma = soma +index   
    return soma

def calcular_vendas_mes (lista,mes ):

    placeholder = 0
    for x,y in lista:
        if (y > placeholder):
            placeholder = y
    itens_satisfatorios = [a for a,b in lista if b == placeholder]
    print(f'O item que teve maior venda em {mes} foi: ',itens_satisfatorios)

# Calculando total de vendas de cada produto: 
# Zipando os itens e o suas respectivas vendas em uma so lista

combine = zip (produtos,vendas_janeiro,vendas_fevereiro,vendas_marco,vendas_abril)
newCombine = list(combine)

# A criação dessas listas A,B,C,D etc, foi pra tentar deixar o código um pouco mais limpo na hora de printar os resultados

A = newCombine [0]
B = newCombine [1]
C = newCombine [2]
D = newCombine [3] 
E = newCombine [4]
F = newCombine [5]
G = newCombine [6]

# Printando os resultados totais de cada produto

print('*******************************')
print('VENDAS TOTAIS!')
print(f'VENDAS A :',calcular_vendas(A))
print(f'VENDAS B :',calcular_vendas(B))
print(f'VENDAS C :',calcular_vendas(C))
print(f'VENDAS D :',calcular_vendas(D))
print(f'VENDAS E :',calcular_vendas(E))
print(f'VENDAS F :',calcular_vendas(F))
print(f'VENDAS G :',calcular_vendas(G))
print('*******************************')

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Maiores Vendas por mes
# Comecei criando listas para cada mes, para no final comparar qual foi o produto com maior venda em cada caso
combine_jan = list (zip(produtos,vendas_janeiro))
combine_fev = list (zip(produtos,vendas_fevereiro))
combine_mar = list (zip(produtos,vendas_marco))
combine_abr = list (zip(produtos,vendas_abril))

# Aqui eu chamo a função la do começo do código, que verifica pra mim qual e o produto que mais foi vendido em cada mês
# Tudo que eu preciso fazer nessa parte do código é fornecer a lista que contem os produtos e escrever o mes do qual eu quero verificar as vendas

calcular_vendas_mes(combine_jan,'janeiro')
calcular_vendas_mes(combine_fev,'fevereiro')
calcular_vendas_mes(combine_mar,'março')
calcular_vendas_mes(combine_abr,'abril')
print('*******************************')
print('*******************************')

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Calculando produto com maior crescimento percentual entre janeiro e fevereiro 

# Eu criei um novo combine, visto que os meses mudaram eu tambem tenho que mudar minha lista.
# Mas o processo é o mesmo. Criei novas listas que contém os produtos e os meses.

combine_2_meses = zip(produtos,vendas_janeiro,vendas_fevereiro)
newList = list(combine_2_meses) 

# Como eu vi que nao foram todos os produtos que aumentaram suas vendas nesse periodo, eu fiz um codigo pra verificar quais foram os que cresceram primeiro, para depois ver o que teve maior crescimento.
# porcentagem_A =  ((a_final * 100) // a_inicial) - 100

maior_crescimento = [a for a,b,c in newList if b<c ]

# A lista maior_crescimento retorna somente um valor, que é o C. Ou seja o único produto que cresceu foi o C., fazendo assim com que ele seja a resposta da questão.

print(f'O item que teve maior crescimento percentual entre os meses foi o item {maior_crescimento}')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
# O ultimo exercicio tambem é bem simples como o de cima, se usarmos zip e a estrutura de for dentro da lista.
# O processo inicial foi o mesmo, tive que fazer uma nova lista com os meses respectivos do enunciado

list_ex_c = zip (produtos,vendas_marco,vendas_abril)
lista_zipada = list (list_ex_c)

# Na lista_final, eu construo o código de forma que so entre na lista final o a2, que seria o nome do produto, se c2 (valor inicial) for menor que o b2(valor final).
# Fazendo isto, na lista final estarão os produtos cuja as vendas em março foram menores que as vendas em abril, em outras palavras, os produtos em queda.

lista_final = [a2 for a2,b2,c2 in lista_zipada if c2 < b2]

print(f'Os itens que tiveram queda de vendas entre os meses de abril e março foram: {lista_final}')


# Fim do exercicio