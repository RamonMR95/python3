class Flight:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()


class AirbusEngine:

    @staticmethod
    def start():
        print("Airbus starting")


class BoeingEngine:

    @staticmethod
    def start():
        print("Boeing starting")


a = AirbusEngine()
b = BoeingEngine()

f = Flight(a)
f.start_engine()

f = Flight(b)
f.start_engine()

