from traitlets.traitlets import Float

import random

#1) Faça um programa que recebe uma lista de números reais e exibe o
# seu maior elemento.

# Recebe uma lista de números reais do usuário
numeros = input("Digite uma lista de números reais separados por espaço: ").split()

# Converte os números de string para float e cria a lista de números reais
numeros_reais = [float(numero) for numero in numeros]

# Encontra o maior elemento na lista
maior_elemento = max(numeros_reais)

# Formata o número para remover o ponto decimal
maior_elemento_formatado = "{:.0f}".format(maior_elemento)

#Exibe maior elemento
print("O maior elemento da lista é:", maior_elemento_formatado)




#2) Faça um programa que recebe uma lista de números reais e exibe sua
# média

# Recebe uma lista de números reais do usuário
numeros = input("Digite uma lista de números reais separados por espaço para calcular a media1: ").split()

# Converte os números de string para float e cria a lista de números reais
numeros_reais = [float(numero) for numero in numeros]

#Uma variavel para verificar se a lista está vazia 
lista_vazia = False 
if len(numeros_reais) == 0:
    lista_vazia = True

#Calcula a soma dos números, apenas se a lista não estiver vazia 
if not lista_vazia:
  soma = sum(numeros_reais)

  media = soma/len(numeros_reais)

  print("A media dos numeros é: {:.2f}".format(media))
else:
  print("A lista está vazia, por isso não é possivel calcular a média: ")


#3) Dada uma lista de números inteiros, faça um programa que responda a
# soma de todos os números pares e ímpares.

numeros= input("Digite uma lista de numeros inteiros: ").split()

numeros_inteiros = [float(numero) for numero in numeros]
0
#Variaveis para armazenar a soma dos numeros pares e impares 

somaPares = 0
somaImpares = 0 

for numero in numeros_inteiros:
  if numero % 2 == 0:
    somaPares += numero
  else:
      somaImpares += numero

# Exibe a soma dos números pares e ímpares
print("A soma dos números pares é:", somaPares)
print("A soma dos números ímpares é:", somaImpares)


#4) Faça um programa que receba um número e exiba o fatorial desse
#número140

numeroFatorial = int(input("Digite um número para ser fatorado:  ").replace(',',''))

#Inicializa a varivél fatorial como 1 50

fatorial = 1

#Calcula o fatorial do número 
for i in range(numeroFatorial, 1, - 1):
  fatorial *= (i)

print("O fatorial de", numeroFatorial, "é", fatorial)  



#5) Faça um programa que verifique se uma string possui caracteres
#duplicados

string = input("Digite suas Strings").split()

#Criação de conjunto vazio para armazenar os caracteres únicos

caracteres_unicos = set()

#Verifica se a caracteres duplicados

possui_duplicados = False

#Verifica cada caractere da string
for caractere in string:
  if caractere in caracteres_unicos:
    possui_duplicados = True
    break

 # Add caractere ao conjunto de caracteres únicos
  caracteres_unicos.add(caractere)   


if possui_duplicados:
    print("A string possui caracteres duplicados.")
else:
    print("A string não possui caracteres duplicados.")

# 6) Desenvolva um programa que armazene quatro notas em uma lista e
# que apresente a média final. Caso a média seja igual ou superior a 7,
# apresentar a mensagem "APROVADO", caso contrário, armazenar a
# nota da prova final e recalcular a média. Caso a nova média seja igual
# superior a 5, apresentar a mensagem "APROVADO", caso contrário,
# apresentar a mensagem "REPROVADO"

notasListas = input("Digite as quatro notas por espaço: ").split()

notas = [float(nota) for nota in notasListas]

somaMed = sum(notas) / len(notas)

if somaMed >= 7:
  print("APROVADO")
else:
  finalNota = float(input("Digite a nota final:  ")) 
  if (sum(notas) + finalNota) / 5 >= 5: 
    print("APROVADO")
  else:
    print("REPROVADO")

# 7) Faça um programa que gere um número inteiro aleatório e que peça
# para o usuário adivinhar, informe se o número que o usuário digitou é
# menor ou maior que o número gerado. O jogo acaba quando o usuário
# acertar o número gerado

numeroGerado = random.randint(1,10)
 

while True:
  # Recebe o palpite do usuário 
  palpite = int(input("Advinhe qual o numero que eu gerei entre 1 e 10: "))

  # Verifica se o palpite é menor, maior ou igual ao número gerado
  if palpite < numeroGerado:
      print("O número gerado é maior")
  elif palpite > numeroGerado:
    print("O numero gerado é menor ")
  else: 
    print("Parabens, voce acertou o numero gerado")
    break

# 8) Desenvolva um programa que gere uma lista de números primos 
#    com base em um intervalo fornecido pelo usuário

def verificar_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def gerar_primos(inicio, fim):
    primos = []
    for numero in range(inicio, fim + 1):
        if verificar_primo(numero):
            primos.append(numero)
    return primos

inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))

primos = gerar_primos(inicio, fim)

print("Números primos no intervalo de", inicio, "a", fim, ":")
if primos:
    for primo in primos:
        print(primo)
else:
    print("Nenhum número primo encontrado no intervalo.")
    print("Nenhum numero primo encontrado no intervalo. ")



import random

def jogo_da_forca():
    palavras = ['python', 'programacao', 'desafio', 'computador', 'algoritmo']
    palavra_sorteada = random.choice(palavras)
    palavra_advinha = []
    letras_erradas = []

    while True:
        palavra_mascarada = []
        for palavra in palavra_sorteada:
           if palavra in palavra_advinha:
              palavra_mascarada.append(palavra)
        else:
           palavra_mascarada.append('_')
    
        print('\nPalavra:', ' '.join(palavra_mascarada))
        print('Letras erradas:', ' '.join(letras_erradas))

        if '_' not in palavra_mascarada:
            print('\n Parabens, voce acertou a palavra')
            break
        
    
        letra = input('Digite uma letra: ').lower()

        if len(letra) != 1 or not letra.isalpha():
            print('Por favor, digite apenas uma letra válida.')
            continue

        if letra in palavra_sorteada:
            for i in range(len(palavra_sorteada)):
                if palavra_sorteada[i] == letra:
                    palavra_mascarada[i] = letra
        else:
            letras_erradas.append(letra)


    
    print('\nParabéns, você acertou a palavra!')
    print('A palavra era:', ''.join(palavra_sorteada))

jogo_da_forca()