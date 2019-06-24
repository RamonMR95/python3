from abc import abstractmethod, ABC


class BMW(ABC):
    def __init__(self, made, model, year):
        self.made = made
        self.model = model
        self.year = year

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass


class ThreeSeries(BMW):
    def __init__(self, cruise_control_enabled, made, model, year):
        super().__init__(made, model, year)
        self.cruise_control_enabled = cruise_control_enabled

    def start(self):
        super().start()
        print("Button start")

    def stop(self):
        print("ThreeSeries Stopped")

    def drive(self):
        print("ThreeSeries driven")


class FiveSeries(BMW):
    def __init__(self, parking_assist, made, model, year):
        BMW.__init__(self, made, model, year)
        self.parking_assist = parking_assist

    def start(self):
        print("FiveSeries Started")

    def stop(self):
        print("FiveSeries Stopped")

    def drive(self):
        print("FiveSeries driven")


three_series = ThreeSeries(True, "BMW", "328i", "2019")
print(three_series.cruise_control_enabled)
print(three_series.made)
print(three_series.model)
print(three_series.year)

five_series = FiveSeries(True, "BMW", "525", "2008")
print(five_series.parking_assist)
print(five_series.made)
print(five_series.model)
print(five_series.year)

three_series.start()
five_series.stop()

three_series.drive()
five_series.drive()
