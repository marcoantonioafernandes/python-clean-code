# Vamos aplicar as regras de funções: 
# 1 - Funções pequenas
# 2 - Funções que façam apenas 1 coisa
# 3 - Nomes descritivos em funções

# Vamos aplicar as regras de comentários


# Basicamente foram criadas funções pequenas, com um objetivo 
# e com nomes descritivos
# Além disso, foi necessário recorrer a um comentário
# em uma das funções que não ficou clara

MINIMUM_PASSWORD_LENGTH = 8
MAXIMUM_PASSWORD_LENGTH = 16

def validate_password(password:str) -> bool:
    if(
        test_password_length(password) and 
        test_if_password_has_upper_digit(password) and
        test_if_password_has_lower_digit(password) and 
        test_if_password_has_special_caracther(password)
    ):
        return True
    return False

def test_password_length(password:str) -> bool:
    password_length = len(password)
    return password_length >= MINIMUM_PASSWORD_LENGTH and password_length <= MAXIMUM_PASSWORD_LENGTH

def test_if_password_has_upper_digit(password:str) -> bool:
    return True in [True for digit in password if digit.isupper()]

def test_if_password_has_lower_digit(password:str) -> bool:
    return True in [True for digit in password if digit.islower()]

def test_if_password_has_special_caracther(password:str) -> bool:
    # A regra abaixo verifica se a string NÃO tem caracteres especiais
    # por isso é retornado o not
    return not bool(re.search('^[a-zA-Z0-9]*$', password))

import re
if __name__ == '__main__':
    password = input("Informe uma senha: ")
    if(validate_password(password)):
        print("Senha válida")
    else:
        print("Senha inválida")
    



