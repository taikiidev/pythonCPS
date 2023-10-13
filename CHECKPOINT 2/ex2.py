import sys
# Exercicio 2
# Definindo as listas
# Pequena alteraçao na ordem de definicao de listas para seguir um padrao de nome, cpf e senha, ao inves de usar senha, nome e cpf
# Outra alteração que eu fiz foi mudar os cpfs_corretos de string para inteiros para facilitar posteriormente, alem de transformar os ints em strings.

nomes_corretos= ["Joao Silva" , "Maria Oliveira", "Pedro Santos"  ,  "Ana Souza"  , "Carlos Pereira"]
cpfs_corretos=  ['12345678900'  ,  '98765432100'    ,  '45678912300 '   ,  '32165498700'  ,     '78912345600']
senhas_corretas=["senha123"   ,  "abc456"       ,  "qwerty"       ,  "admin123"   ,       "letmein"]

# Aqui eu fiz uma função para verificar se a senha está correta ou nao, para nao poluir o codigo la em baixo.

def verificar_senha (username,lista):
    if (username in lista):
        senha = input('Por favor digite sua senha!')
        if (senha == lista[2]):
            print('Entrada aprovada!')
        else :
            print('Senha incorreta!')



# Combinando as 3 listas e Transformando o zip em lista, para poder iterar pelo seu index 
combine = zip (nomes_corretos,cpfs_corretos,senhas_corretas)
newCombine = list(combine)

# Criei uma lista para cada pessoa, que e composta pelo seu cpf e sua senha respectiva

infoJoao = newCombine [0]
infoMaria = newCombine [1]
infoPedro = newCombine [2]
infoAna = newCombine [3]
infoCarlos = newCombine [4]

# Inicializando o total de tentativas que o usuario terá para fazer o login

tentativas = 0
# Iniciando um while loop para que o ususario nao tenha que reiniciar o codigo toda vez que for tentar novamente caso ele erre.

while tentativas < 10:

# Pedindo o nome e o CPF do usuario

    username =  input('Por favor digite seu nomes!')
    userCpf = (input('Por favor digite seu CPF!'))

# Checando se as credenciais se quer fazem parte das credenciais existentes.

    if (username not in nomes_corretos or userCpf not in cpfs_corretos):
        print('Credenciais inválidas!')
        tentativas = tentativas +1
        continue
# Caso as credencias sejam validas, passe para o processo de verificação de senha do usuario respectivo.

    else :
        if (username in infoJoao ):
            verificar_senha(username,infoJoao)
        elif (username in infoMaria):
            verificar_senha(username,infoMaria)
        elif (username in infoPedro):
            verificar_senha(username,infoPedro)
        elif (username in infoAna):
            verificar_senha(username,infoAna)
        elif (username in infoCarlos):
            verificar_senha(username,infoCarlos)
# Quando as tentativas acabam, printar mensagem de aviso

print('Suas tentativas acabaram! Por motivos de segurança, pedimos que tente novamente mais tarde!')

# Fim do exercicio
    