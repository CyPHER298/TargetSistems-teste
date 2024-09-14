# TESTE 1
indice = 13
soma = 0
k = 0
while k < indice:
    k += 1
    soma = soma + k
    print(soma)

# TESTE 2

#Aplicando um input para receber a informação
n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1

#Verificar se um dos resultados for ligado aos primeiros numero da tabela
if (n==1) or (n==2):
    print("1")
else:
    # Para count no mínimo 2 e máximo variavel n fazer a fórmula de fibonacci
    for count in range(2,n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)

# TESTE 3
import json
from statistics import median

# Abrindo o arquivo .json como leitura somente como "vendas"
with open('dados.json', 'r') as vendas:

    # lendo os dados do .json
    dados = json.load(vendas)

    # declaro as variaveis valor_max e valor_min como vazias para poderem ser manipuladas de formas livres
    valor_max = None
    valor_min = None

    # declaro total e count com o valor 0, assim declarando que usarei numeros
    total = 0
    count = 0

    # loop para verificar os dias que não houve valor algum e logo em seguida pegando valores maximos e minimos do mês
    for item in dados:
        if item['valor'] != 0:
            total += item['valor']
            count += 1
            if valor_max is None or item['valor'] > valor_max:
                valor_max = item['valor']
            if valor_min is None or item['valor'] < valor_min:
                valor_min = item['valor']

    # media a partir dos valores obtidos pelos dias trabalhados
    media = total / count

print(f'O maior valor neste mês foi de R${valor_max:.2f}')
print(f'O menor valor deste mês foi de R${valor_min:.2f}')
print(f"R${media:.2f} foi a média deste mês nos dias que tiveram algum valor")


# TESTE 4
# declarados todos os valores de cada estado
sp = 67863.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

# feito a soma de todos os valores para saber o 100% e fazendo valor_estado / o valor_total * 100 para ter a porcentagem
cem_porcent = sp + rj + mg + es + outros
sp_porcent = sp / cem_porcent * 100
rj_porcent = rj / cem_porcent * 100
mg_porcent = mg / cem_porcent * 100
es_porcent = es / cem_porcent * 100
outros_porcent = outros / cem_porcent * 100

print(f"A fatia percentual de cada estado:\n"
      f"São Paulo: {sp_porcent:.2f}%\n "
      f"Rio de Janeiro: {rj_porcent:.2f}%\n "
      f"Minas Gerais: {mg_porcent:.2f}%\n "
      f"Espírito Santo: {es_porcent:.2f}%\n "
      f"Outros estados: {outros_porcent:.2f}%")

#TESTE 5

# Inserindo a palavra
string = input("Inserir a string: ")

# Usando uma função do proprio python para fazer a inversão da string
string_invertida = ''.join(reversed(string))
print(string_invertida)