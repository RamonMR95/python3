from threading import *


class BookMyBus:

    def buy(self):
        print("Confirming seat")
        print("Processing the payment")
        print("Printing the ticket")


bmb = BookMyBus()
t1 = Thread(target=bmb.buy)
t2 = Thread(target=bmb.buy)
t3 = Thread(target=bmb.buy)

t1.start()
t2.start()
t3.start()

