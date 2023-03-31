# Vamos aplicar nomes significativos: 
# 1 - Nomes que revelem seu propósito
# 2 - Nomes pronunciáveis
# 3 - Nomes passíveis de busca
# Alterações: 
    # password = password
    # valid_password = is_valid_password
    # 8 = MINIMUM_PASSWORD_LENGTH
    # 16 = MAXIMUM_PASSWORD_LENGTH
    # l = digit
    # valid_upper = has_any_upper_digit
    # valid_lower = has_any_lower_digit

MINIMUM_PASSWORD_LENGTH = 8
MAXIMUM_PASSWORD_LENGTH = 16

import re
if __name__ == '__main__':
    password = input("Informe uma senha: ")
    is_valid_password = True

    # regra para verificar se a senha tem um tamanho válido
    if len(password) <= MINIMUM_PASSWORD_LENGTH:
        is_valid_password = False
    
    if len(password) >= MAXIMUM_PASSWORD_LENGTH:
        is_valid_password = False
    
    # Validação de letra minuscula
    # l = letra
    has_any_upper_digit = False
    for digit in password:
        if digit.isupper():
            has_any_upper_digit = True
            break

    # Validação de letra minuscula
    # l = letra
    has_any_lower_digit = False
    for digit in password:
        if digit.islower():
            has_any_lower_digit = True
            break
    
    if not (has_any_upper_digit):
        is_valid_password = False

    if not (has_any_lower_digit):
        is_valid_password = False

    
    # verifica se a senha tem caracteres especiais
    if(bool(re.search('^[a-zA-Z0-9]*$', password))==True):
        is_valid_password = False

    if is_valid_password == False:
        print("Senha inválida")
    else:
        print("Senha válida")
    



