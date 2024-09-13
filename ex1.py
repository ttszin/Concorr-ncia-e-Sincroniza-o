import logging
import threading
import time

class Filosofo(thread):
    execute = True
    def __init__(self,nome,hashi_esquerda,hashi_direita):
        Thread.__init__(self)
        self.nome = nome
        self.hashi_esquerda = hashi_esquerda
        self.hashi_direita = hashi_direita

    def run():
        while self.execute:
            print("O filósofo {self.name} está pensando...")
            time.sleep(5)
            self.comer()

    def comer():
        hashi1,hashi2 = self.hashi_direita,self.hashi_esquerda
        while self.execute:
            hashi1.acquire(True)
            locked = hashi2.acquire(False)
            if locked:
                break
            hashi1.release()
            else:
                return

def thread_function(id):

    while True:
        S.acquire()
        logging.info("Thread %s entrou no semáforo e vai dormir", id)
        time.sleep(5)
        logging.info("Thread %s acordou", id)
        S.release()
        logging.info("Menos um na região crítica")

S = threading.Semaphore(6)

if __name__ == "__main__":

    threads = [] #armazena os descritores das threads

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    for id in range(1,10):
        Filosofo.execute()
        #t = threading.Thread(target=thread_function, args=(id,)) #inicializa a thread, informa o nome da função e os parâmetros
        logging.info("Main    : before running thread")
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    logging.info("Main    : all done")