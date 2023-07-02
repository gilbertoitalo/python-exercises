import random

def jogo_da_forca():   
    #Criacao das variaves e suas arrays 
    palavras = ['python', 'programacao']
    palavra_sorteada = random.choice(palavras)
    palavra_advinhadas = ['_'] * len(palavra_sorteada)
    letras_erradas = []
   
    # Estruta de um loop para para mostrar as palavras corretas e incorretas
    while '_' in palavra_advinhadas:
        print('\nPalavra:', ' '.join( palavra_advinhadas))
        print('Letras erradas:', ' '.join(letras_erradas))

        # Pede ao user para digitar uma letra 
        letra = input('Olá digite uma letra: ').lower()

        # Verifica se o input do user e valido se nao uma msg de erro é exibida 
        if len(letra) != 1 or not letra.isalpha():
            print('Por favor, digite apenas uma letra válida.')
            continue
        
        # Se o input tiver a letra na palavra sorteada, 
        # o codigo ver em qual posicao esta a letra, 
        # caso contrario e add a array de letras_erradas
        if letra in palavra_sorteada:
            for i in range(len(palavra_sorteada)):
                if palavra_sorteada[i] == letra:
                    palavra_advinhadas[i] = letra
        else:
            letras_erradas.append(letra)
        
        # Caso o user atinga 6 tentativas o jogador perde e palavrar e revelada,
        # e se não restar mais espacos a ser preenchidos, uma msg de parabens e mostrada
        if len(letras_erradas) == 6:
            print('\Voce perdeu, a palavra era:' , palavra_sorteada)
            break
        
        if '_' not in palavra_advinhadas:
         print('\nParabéns, você acertou a palavra!')
         break
       
jogo_da_forca()