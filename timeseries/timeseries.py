from typing import List
import datetime

class Timeseries:
    def __init__(self, averaging_time: datetime.timedelta = None) -> None:
        self.time: List[float] = []
        self.avg: List[float] = []
        self.std: List[float] = []
        self.min: List[float] = []
        self.max: Lost[float] = []

    def __str__(self) -> str:
        return str(self.time) + str(self.avg)

    def add(value: float, time: float = None):
        pass

if __name__ == "__main__":
    ts = Timeseries()
    print(ts)
