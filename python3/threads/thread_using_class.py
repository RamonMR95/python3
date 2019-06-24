from threading import *
import time


class MyThread:

    @staticmethod
    def display_numbers():
        i = 0
        print(current_thread().getName())
        time.sleep(1)
        while i <= 10:
            print(i)
            i += 1


mt = MyThread()

t = Thread(target=mt.display_numbers)
t.start()


t2 = Thread(target=mt.display_numbers)
t2.start()


t3 = Thread(target=mt.display_numbers)
t3.start()

