import re

def validar_senha(senha):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return "Sua senha e muito curta. Recomenda-se no minimo 8 caracteres."
    
    # Verifica se a senha contém pelo menos uma letra maiúscula
    if not re.search("[A-Z]", senha):
        return "Sua senha nao atende aos requisitos de seguranca."
    
    # Verifica se a senha contém pelo menos uma letra minúscula
    if not re.search("[a-z]", senha):
        return "Sua senha nao atende aos requisitos de seguranca."
    
    # Verifica se a senha contém pelo menos um número
    if not re.search("[0-9]", senha):
        return "Sua senha nao atende aos requisitos de seguranca."
    
    # Verifica se a senha contém pelo menos um caractere especial
    if not re.search("[!@#$%^&*()_+{}|:<>?]", senha):
        return "Sua senha nao atende aos requisitos de seguranca."
    
    # Se todas as verificações passarem, a senha é considerada forte
    return "Sua senha atende aos requisitos de seguranca. Parabens!"

# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = validar_senha(senha)

# Imprimindo o resultado
print(resultado)
