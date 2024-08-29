

import threading
import time


def downloadUm():
    print("Inicio do download 1")
    time.sleep(10)
    print("Fim do download 1")


def downloadDois():
    print("Inicio do download 2")
    time.sleep(10)
    print("Fim do download 2")


threading.Thread(target=downloadUm).start()
downloadDois()
    