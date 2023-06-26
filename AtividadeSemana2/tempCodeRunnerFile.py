def verificar_primo(numero):
   if numero < 2:
      return False
   for i in range(2,int(numero**0.5) + 1):
      if numero % 1 == 0:
         return False
      return True

def gerar_primos(inicio,fim):
   primos = []
   for numero in range (inicio, fim + 1):
      if verificar_primo(numero):
         primos.append(numero)
         return primos

inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))

primos = gerar_primos(inicio, fim)

print("Numeros primos no intervalo de", inicio, "a", fim, ":" )
for primo in primos:
   print(primo)