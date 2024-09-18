from random import uniform
from time import sleep
from threading import Thread, Lock, Event

# Inicializa a lista de pratos para contabilizar quantas vezes cada filósofo comeu
pratos = [0, 0, 0, 0, 0]  # 0 = Não comeu, 1 = Já comeu


class Filosofo(Thread):
    # Utilizamos um Event para controlar a execução
    execute_event = Event()

    def __init__(self, nome, hashi_esquerda, hashi_direita):
        super().__init__()
        self.nome = nome
        self.hashi_esquerda = hashi_esquerda
        self.hashi_direita = hashi_direita

    def run(self):
        """Define o comportamento do filósofo: pensar e tentar comer enquanto o evento estiver ativo."""
        while Filosofo.execute_event.is_set():
            print(f"{self.nome} está pensando\n")
            sleep(uniform(5, 15))  # Simula o tempo de pensar
            self.comer()

    def comer(self):
        """O filósofo tenta pegar os dois hashis para comer, ou volta a pensar se não conseguir."""
        hashi1, hashi2 = self.hashi_esquerda, self.hashi_direita

        while Filosofo.execute_event.is_set():
            hashi1.acquire(True)  # Tenta pegar o primeiro hashi
            locked = hashi2.acquire(False)  # Tenta pegar o segundo hashi
            if locked:
                print(f"{self.nome} começou a comer")
                sleep(uniform(5, 10))  # Simula o tempo de comer
                print(f"{self.nome} terminou de comer")
                pratos[nomes.index(self.nome)] += 1  # Registra quantas vezes o filósofo comeu
                print(f"Pratos: {pratos}")
                hashi1.release()  # Libera o hashi esquerdo
                hashi2.release()  # Libera o hashi direito
                break
            else:
                # Se não conseguir o segundo hashi, libera o primeiro e volta a pensar
                hashi1.release()
                print(f"{self.nome} não conseguiu pegar ambos os hashis, voltando a pensar")
                sleep(uniform(1, 3))  # Pequena pausa antes de tentar novamente


# Nomes dos filósofos
nomes = ['Aristóteles', 'Platão', 'Sócrates', 'Pitágoras', 'Demócrito']

# Criamos um Lock para cada hashi
hashis = [Lock() for _ in range(5)]

# Criamos uma instância de Filosofo para cada um
mesa = [Filosofo(nomes[i], hashis[i % 5], hashis[(i + 1) % 5]) for i in range(5)]

# Função principal para iniciar a simulação
def iniciar_jantar():
    Filosofo.execute_event.set()  # Inicia a execução dos filósofos

    # Inicia as threads de cada filósofo
    for filosofo in mesa:
        filosofo.start()

    sleep(60)  # Simulação de 60 segundos de jantar

    Filosofo.execute_event.clear()  # Para a execução dos filósofos

    # Espera todas as threads terminarem
    for filosofo in mesa:
        filosofo.join()

# Iniciar a simulação
if __name__ == "__main__":
    print("Iniciando o jantar dos filósofos.\n")
    iniciar_jantar()
    print("Jantar finalizado.")
    print(f"Estatísticas finais dos pratos: {pratos}")
