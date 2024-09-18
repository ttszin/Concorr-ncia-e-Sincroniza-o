import threading
import random
import time

# Classe que representa uma conta bancária
class ContaBancaria:
    def __init__(self, id_conta, saldo_inicial):
        self.id_conta = id_conta
        self.saldo = saldo_inicial
        self.lock = threading.Lock()  # Lock para garantir exclusividade nas operações de crédito e débito
        self.semaforo_consulta = threading.Semaphore(5)  # Até 5 consultas simultâneas
        self.consultas_ativas = 0  # Contador de consultas de saldo ativas

    # Operação de crédito (depósito)
    def credito(self, valor):
        with self.lock:
            print(f"[Crédito] Conta {self.id_conta}: +{valor} iniciando...")
            self.saldo += valor
            time.sleep(random.uniform(0.5, 1.5))  # Simula tempo de processamento
            print(f"[Crédito] Conta {self.id_conta}: +{valor} finalizado. Saldo atual: {self.saldo}")

    # Operação de débito (saque)
    def debito(self, valor):
        with self.lock:
            print(f"[Débito] Conta {self.id_conta}: -{valor} iniciando...")
            if self.saldo >= valor:
                self.saldo -= valor
                time.sleep(random.uniform(0.5, 1.5))  # Simula tempo de processamento
                print(f"[Débito] Conta {self.id_conta}: -{valor} finalizado. Saldo atual: {self.saldo}")
            else:
                print(f"[Débito] Conta {self.id_conta}: saldo insuficiente! Saldo atual: {self.saldo}")

    # Operação de consulta de saldo
    def consultar_saldo(self):
        with self.semaforo_consulta:  # Permite até 5 consultas simultâneas
            with threading.Lock():
                self.consultas_ativas += 1
            print(f"[Consulta] Conta {self.id_conta}: saldo sendo consultado. Consultas ativas: {self.consultas_ativas}")

            time.sleep(random.uniform(0.5, 1.0))  # Simula tempo da consulta
            print(f"[Consulta] Conta {self.id_conta}: saldo atual é {self.saldo}")

            with threading.Lock():
                self.consultas_ativas -= 1
            print(f"[Consulta] Conta {self.id_conta}: consulta finalizada. Consultas ativas: {self.consultas_ativas}")

# Função que simula uma operação bancária aleatória (crédito, débito ou consulta)
def simular_operacao(conta):
    operacao = random.choice(['credito', 'debito', 'consulta'])
    valor = random.randint(10, 100)  # Valor aleatório para crédito ou débito

    if operacao == 'credito':
        conta.credito(valor)
    elif operacao == 'debito':
        conta.debito(valor)
    else:
        conta.consultar_saldo()

# Função para inicializar a simulação
def iniciar_simulacao(num_threads, contas):
    threads = []

    # Criar e iniciar threads para cada operação
    for _ in range(num_threads):
        conta_escolhida = random.choice(contas)  # Escolhe uma conta aleatoriamente
        thread = threading.Thread(target=simular_operacao, args=(conta_escolhida,))
        threads.append(thread)
        thread.start()

    # Aguarda todas as threads finalizarem
    for thread in threads:
        thread.join()

# Criar contas bancárias
def criar_contas(num_contas, saldo_inicial):
    return [ContaBancaria(id_conta=i, saldo_inicial=saldo_inicial) for i in range(num_contas)]

# Parâmetros da simulação
num_contas = 3
saldo_inicial = 1000
num_threads = 10

# Criar as contas
contas = criar_contas(num_contas, saldo_inicial)

# Iniciar a simulação
iniciar_simulacao(num_threads, contas)

print("Simulação concluída.")
