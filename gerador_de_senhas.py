import random
import string

def gerar_senha(comprimento=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    for i in range(comprimento):
        senha = ''.join(random.choice(caracteres))
        return senha
    
if __name__ == "__main__":
    tamanho_desejado = 16
    nova_senha = gerar_senha(tamanho_desejado)
    print(f'Sua nova senha de {tamanho_desejado} caracteres é: {nova_senha}')