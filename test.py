from ast import Div
import threading
from tracemalloc import stop

from sqlalchemy import false, true


class Ejecutar_hilo:

    def __init__(self, config_path="", div=3):
        self._config = config_path
        self.i = 0
        self._div = div
        self.stop = False
        print("se inicializo")

    def run(self):
        print("runing")
        while self.i < 20:
            self.i += 1
            # if(self.stop):
            #     break
            print("runing ... run")

            if(self.i % self._div == 0):
                print("runing ... " + str(self.i))

    # def quit(self):
    #     self.stop = True


def worker():
    """thread worker function"""
    for i in range(50):
        print(i)
    print('Worker')


reproctor = Ejecutar_hilo()
# threads = []
t = threading.Thread(target=worker)
t.start()
print('otra cosa')
# reproctor.run()
otro_hilo = threading.Thread(target=reproctor.run())
otro_hilo.start()
print('otra cosa repe')

# for i in range(5):
#     t = threading.Thread(target=worker)
#     threads.append(t)
#     t.start()
