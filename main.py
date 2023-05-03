import threading
import queue
import time
import random

# Classe que representa um cliente
class Cliente:
    def __init__(self, id):
        self.id = id
        self.quantidade_produtos = random.randint(1, 10) # Quantidade aleatória de produtos
        
    def __repr__(self):
        return f'Cliente {self.id} com {self.quantidade_produtos} produtos'

# Função que simula o processamento do cliente no caixa
def processar_cliente(cliente):
    print(f'Caixa {threading.current_thread().name} processando {cliente}')
    tempo = cliente.quantidade_produtos * 1 # Tempo de processamento de acordo com a quantidade de produtos
    time.sleep(tempo) # Simula o tempo de processamento do cliente
    print(f'Caixa {threading.current_thread().name} finalizou {cliente}')

# Função que representa um caixa
def caixa(fila):
    while True:
        cliente = fila.get() # Aguarda um cliente chegar na fila
        processar_cliente(cliente)
        fila.task_done() # Informa que o processamento do cliente foi finalizado

# Cria as filas e caixas
fila1 = queue.Queue()
fila2 = queue.Queue()
fila3 = queue.Queue()

t1 = threading.Thread(target=caixa, args=(fila1,), name='1')
t2 = threading.Thread(target=caixa, args=(fila2,), name='2')
t3 = threading.Thread(target=caixa, args=(fila3,), name='3')

t1.start()
t2.start()
t3.start()

while True:
    # Cria um novo cliente
    cliente = Cliente(random.randint(1, 1000))
    
    # Adiciona o cliente à fila mais curta
    if fila1.qsize() <= fila2.qsize() and fila1.qsize() <= fila3.qsize():
        fila1.put(cliente)
    elif fila2.qsize() <= fila3.qsize():
        fila2.put(cliente)
    else:
        fila3.put(cliente)

# Aguarda a finalização do processamento de todos os clientes nas filas
fila1.join()
fila2.join()
fila3.join()

# Encerra as threads dos caixas
t1.join()
t2.join()
t3.join()
