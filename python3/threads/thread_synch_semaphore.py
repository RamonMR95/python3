from threading import *


class BookMyBus:

    def __init__(self, available_seats):
        self.available_seats = available_seats
        self.sem = Semaphore()

    def buy(self, seats_requested):
        self.sem.acquire()

        print("Seats available", self.available_seats)

        if self.available_seats >= seats_requested:
            print("Confirming seat")
            print("Processing the payment")
            print("Printing the ticket")
            self.available_seats -= seats_requested
        else:
            print("No more tickets left")
        self.sem.release()


bmb = BookMyBus(10)
t1 = Thread(target=bmb.buy, args=(3,))
t2 = Thread(target=bmb.buy, args=(4,))
t3 = Thread(target=bmb.buy, args=(4,))

t1.start()
t2.start()
t3.start()
