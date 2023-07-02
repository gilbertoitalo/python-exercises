import controller_validators

while True:
        print("\nMenu:")
        print("1. Validar CPF")
        print("2. Validar CNPJ")
        print("0. Sair")
   
        opcao = input("Escolha uma opcao")
        
        
        match opcao:
          case '1':
            cpf = input("Digite o seu CPF sem pontos ou hifen: ")
            if controller_validators.validar_cpf(cpf):
                print("CPF VALIDO")
            else:
               print("CPF INVALIDO")  

          case '2':
            cnpj = input("Digite o CNPJ sem ponto ou hifen:  ")
            if controller_validators.validar_CNPJ(cnpj):
               print("CNPJ VALIDO")
            else: 
               print("CNPJ INVALIDO")
          
          case '0':
            print("Encerrando o programa")
            break
          
          case _:
              print("opcao invalida")

          