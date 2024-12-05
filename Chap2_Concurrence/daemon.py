import time
from threading import Thread
def worker(caractere):
    for i in range(0,20):
        print(caractere, end='', flush=True)
        time.sleep(1)

t_point = Thread(target = worker, args = ("."))
t_asterix = Thread(target = worker, args = ("*"), daemon=True)
t_point.start()
time.sleep(4)
t_asterix.start()
t_point.join()
print("\nT_point end\n")