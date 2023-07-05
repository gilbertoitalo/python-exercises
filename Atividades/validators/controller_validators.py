import re 
import datetime

def validar_cpf(cpf):
    
     # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Ver se todos os dígitos do CPF nao são iguais
    if cpf == cpf[0] * 11:
        return False
    
    # Calcula o primeiro dígito verificador
    soma = 0 
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto

    # Verifica se o primeiro dígito verificador está correto
    if int(cpf[9]) != digito_verificador_1:
        return False     
    
    return True 

cpf = input("Digite o numero do CPF: ")
if validar_cpf(cpf):
    print("O cpf é valido.")
else:
    print("O CPF é invalido.")


def validar_CNPJ(cnpj):
    
    # Verifica se o numero 
     if len(cnpj) != 14:
         return False 
   
    # Verifica se todos os dígitos do CNPJ são iguais
     if cnpj == cnpj[0] * 14:
        return False 
    
    # Ver se os primeiros numeros oito digitos 
     soma = 0 
     peso = 5
     for i in range(12):
         soma += int(cnpj[i]) * peso
         peso = 9 if peso == 2 else peso -1
     resto = soma % 11
     digito_verificador_11 = 0 if resto < 2 else 11 - resto

    # Ver os ultimos dois digitos estao correto
     if int(cnpj[13]) != digito_verificador_11:
      return False
     
     return True

def validar_email(email):
    # Criar um expressao regular para verificar o email
    padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(padrao, email) is not None 
    # Verificar a existencia do dominio do email se mesmo existe

def validar_data(data):
    try:
        # Verifica se data está no formato correto (dd/mm/aaaa) 
        data_format = datetime.strptime(data, "%d/%m/%Y")
        
        # Verifica se a data é uma data valida no calendario
        return True
    except ValueError:
        return False 
    
data = input("Digite a data (dd/mm/aaaa): ")
                                          
    
    
    
    
     
