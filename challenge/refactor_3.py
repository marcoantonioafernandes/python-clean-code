# Vamos aplicar a regra que está com nomes significativos: 
    # Contexto significativo

import re

class PasswordValidator:
    def __init__(self):
        self.minimum_length = 8
        self.maximum_length = 16

    def validate(self, password:str) -> bool:
        if(
            self.__test_password_length(password) and 
            self.__test_if_password_has_upper_digit(password) and
            self.__test_if_password_has_lower_digit(password) and 
            self.__test_if_password_has_special_caracther(password)
        ):
            return True
        return False

    def __test_password_length(self, password:str) -> bool:
        password_length = len(password)
        return password_length >= self.minimum_length and password_length <= self.maximum_length

    def __test_if_password_has_upper_digit(self, password:str) -> bool:
        return True in [True for digit in password if digit.isupper()]

    def __test_if_password_has_lower_digit(self, password:str) -> bool:
        return True in [True for digit in password if digit.islower()]

    def __test_if_password_has_special_caracther(self, password:str) -> bool:
        # A regra abaixo verifica se a string NÃO tem caracteres especiais
        # por isso é retornado o not
        return not bool(re.search('^[a-zA-Z0-9]*$', password))


if __name__ == '__main__':
    password = input("Informe uma senha: ")
    
    password_validator = PasswordValidator()

    if(password_validator.validate(password)):
        print("Senha válida")
    else:
        print("Senha inválida")
    



