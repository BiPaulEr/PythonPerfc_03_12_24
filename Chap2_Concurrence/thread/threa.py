import time
from threading import Thread 

def salutation_long():
    print("Je suis la salutation ....zzzz")
    time.sleep(3)
    print("zzzz... longue")

def info(thread):
    print(thread.name)
    print(thread.ident)
    print(thread.is_alive())
t2 = Thread(target=salutation_long)
info(t2)
t2.start()
info(t2)
t1 = Thread(target=salutation_long)
info(t1)
t1.start()
info(t1)