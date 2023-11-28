from concurrent.futures import thread
import threading
import time

'''def worker():
    print('inicio')
    time.sleep(2)
    print('final')

threads = list()

for i in range(2):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for i in threads:
    t.join()'''

def worker_1(rango):
    lista = list()
    for i in range(rango):
        lista.append(i)
        time.sleep(0.01)
    return lista


ti = time.time()
lista = worker_1(100)
tf = time.time() - ti
print(f'Tiempo total en 1 thread: {tf} \n')
print(lista, '\n')

n_thread = 2
lista_2 = list()

def worker_2(inicio, fin):
    for i in range(inicio, fin):
        lista_2.append(i)
        time.sleep(0.02)
    return lista_2

p = len(lista) // n_threads
inicios = list()
fines = list()
inicio = 0
fin = p

for i in range(n_threads):
    inicios.append(inicio)
    fines.append(fin)

ti = time.time()
threads = list()
for i in range(len(inicios)):
    t = threading.Thread(target=worker_2, args=(inicio[i], fines[i]))
    threads.append(t)
    t.start()

for i in threads:
    t.join()

tf = time.time()
print(f"tiempo total rn {n_threads} threads: {tf}")
print