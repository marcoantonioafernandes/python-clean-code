import re
if __name__ == '__main__':
    pwd = input("Informe uma senha: ")
    valid_pwd = True

    # regra para verificar se a senha tem um tamanho válido
    if len(pwd) <= 8:
        valid_pwd = False
    
    if len(pwd) >= 16:
        valid_pwd = False
    
    # Validação de letra minuscula
    # l = letra
    valid_upper = False
    for d in pwd:
        if d.isupper():
            valid_upper = True
            break

    # Validação de letra minuscula
    # l = letra
    valid_lower = False
    for d in pwd:
        if d.islower():
            valid_lower = True
            break
    
    if not (valid_upper):
        valid_pwd = False

    if not (valid_lower):
        valid_pwd = False

    
    # verifica se a senha tem caracteres especiais
    if(bool(re.search('^[a-zA-Z0-9]*$', pwd))==True):
        valid_pwd = False

    if valid_pwd == False:
        print("Senha inválida")
    else:
        print("Senha válida")
    



