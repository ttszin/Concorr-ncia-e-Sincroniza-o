import logging
import threading
import time

class Barbearia:
    def __init__(self,nome):
        self.nome = nome
        

num_cadeiras = 4
def thread_function(id):

    while True:
        S.acquire()
        logging.info("Thread %s entrou na barbearia e vai dormir", id)
        time.sleep(5)
        logging.info("Thread %s acordou", id)
        S.release()
        logging.info("Menos um na região crítica")

S = threading.Semaphore(10)

if __name__ == "__main__":

    cadeiras = 4
    cadeiras_espera = 2
    num_clientes = 0


    threads = [] #armazena os descritores das threads

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    for id in range(1,10):
        t = threading.Thread(target=thread_function, args=(id,)) #inicializa a thread, informa o nome da função e os parâmetros
        logging.info("Main    : before running thread")
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    logging.info("Main    : all done")