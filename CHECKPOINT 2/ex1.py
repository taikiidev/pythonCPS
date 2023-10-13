
# Exercicio 1
# Definindo as listas
# Mudei um pouco a aparencia das litas para a melhor vizualização de cada propriedade

itens=  ['Feijão', 'Leite', 'Açúcar','‘Arroz', 'azeitona', 'Café em Grãos']
estoque=[  50    ,   20   ,    30   ,   50   ,     30    ,       90       ]
precos =[  5.0   ,  2.0   ,   6.0   ,   10   ,    3.0    ,       3.0      ]

# Iterando a relação de acordo com o que foi pedido no exercicio ( Produtos que a relação resulte num valor maior que 100)
# A variavel 'itens_satisfatorios' terá apenas os produtos que passarem pela condição ' c*b > 100 ', ou seja valor do estoque * valor do preco.

itens_satisfatorios = [a for a,b,c in zip(itens,estoque,precos) if c*b > 100]

# Printando a lista pronta com os itens 

print(f'Os itens cuja relaçãp estão acima de 100 são: {itens_satisfatorios}')


# Fim do exercicio


