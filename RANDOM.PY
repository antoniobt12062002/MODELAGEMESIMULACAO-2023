import time

def gerar_numero_aleatorio():
    timestamp = int(time.time() * 1000)  # Obtém o tempo atual em milissegundos
    numero = hash(timestamp) % 100  # Limita o número gerado entre 0 e 99
    return numero + 1  # Adiciona 1 para obter um número entre 1 e 100

aleatorio = gerar_numero_aleatorio()
print(aleatorio)
