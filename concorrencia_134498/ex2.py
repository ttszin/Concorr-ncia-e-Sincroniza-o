import threading
import time
import random
from queue import Queue

# Parâmetros da simulação
N = 2  # Número de cadeiras de espera (fixo em 2)
fila_espera = Queue(maxsize=N)  # Fila com no máximo 2 cadeiras de espera
barbeiro_dormindo = threading.Event()  # Evento para controlar se o barbeiro está dormindo

# Função do barbeiro
def barbeiro():
    while True:
        # Verifica se há clientes na fila
        if fila_espera.empty():
            print("Barbeiro dormindo...")
            barbeiro_dormindo.clear()  # Barbeiro dorme
            barbeiro_dormindo.wait()  # Aguardando até que seja acordado por um cliente
        else:
            cliente = fila_espera.get()  # Pega o próximo cliente
            print(f"Barbeiro cortando o cabelo do cliente {cliente}...")
            time.sleep(random.uniform(1, 3))  # Simula o tempo de corte de cabelo
            print(f"Cliente {cliente} saiu com o cabelo cortado.")
            fila_espera.task_done()  # Marca o cliente como atendido

# Função dos clientes
def cliente(cliente_id):
    print(f"Cliente {cliente_id} chegou.")
    if fila_espera.full():
        print(f"Cliente {cliente_id} foi embora, sem cadeiras disponíveis.")
    else:
        fila_espera.put(cliente_id)  # Cliente senta na cadeira de espera
        print(f"Cliente {cliente_id} está esperando.")
        barbeiro_dormindo.set()  # Acorda o barbeiro

# Iniciar a thread do barbeiro
threading.Thread(target=barbeiro, daemon=True).start()

# Simular clientes chegando aleatoriamente
cliente_id = 1
while True:
    time.sleep(random.uniform(0.5, 2))  # Simula o intervalo de chegada de clientes
    threading.Thread(target=cliente, args=(cliente_id,)).start()
    cliente_id += 1
