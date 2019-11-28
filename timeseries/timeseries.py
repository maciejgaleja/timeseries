from typing import List
import datetime
import statistics

def _round_time(precise: datetime.datetime, period: datetime.timedelta, midpoint: float = 0.5) -> datetime.datetime:
    epoch = datetime.datetime.utcfromtimestamp(0)
    delta_ms = period.total_seconds()
    precise_ms = ((precise-epoch).total_seconds())
    difference = precise_ms % delta_ms
    ret = datetime.datetime.utcfromtimestamp(precise_ms-difference+(delta_ms*midpoint))
    return ret

class _Period:
    def __init__(self) -> None:
        self._time: List[datetime.datetime] = []
        self._data: List[float] = []

    def __len__(self) -> int:
        return len(self._time)

    def add(self, value: float, time: datetime.datetime) -> None:
        self._time.append(time)
        self._data.append(value)

    def time(self, period: datetime.timedelta) -> datetime.datetime:
        return _round_time(self._time[0], period, 0.5)

    def avg(self):
        return statistics.mean(self._data)

class Timeseries:
    def __init__(self) -> None:
        self.time: List[datetime.datetime] = []
        self.avg: List[float] = []
        self.std: List[float] = []
        self.min: List[float] = []
        self.max: List[float] = []
        self.cnt: List[int] = []
        self.averaging_period: datetime.timedelta = None
        self.current_period = _Period()

    def __str__(self) -> str:
        return str(self.time) + str(self.avg)

    def __len__(self) -> int:
        return len(self.time)

    def add(self, value: float, time: datetime.datetime = datetime.datetime.now()) -> None:
        if not self.averaging_period is None:
            if self._is_period_finished(time):
                self.time.append(self.current_period.time(self.averaging_period))
                self.avg.append(self.current_period.avg())
            self.current_period.add(value, time)
            if not self._is_period_finished(time):
                if(len(self.time) == 0):
                    self.time.append(self.current_period.time(self.averaging_period))
                    self.avg.append(self.current_period.avg())
                self.time[-1] = self.current_period.time(self.averaging_period)
                self.avg[-1] = self.current_period.avg()
        else:
            self.time.append(time)
            self.avg.append(value)
            self.std.append(0.0)
            self.min.append(value)
            self.max.append(value)
            self.cnt.append(1)

    def set_averaging_period(self, period: datetime.timedelta) -> None:
        if not self.averaging_period is None:
            # TODO: implement interpolation/extrapolation
            pass
        else:
            self.averaging_period = period

    def set_history_length(self, length: datetime.timedelta) -> None:
        pass

    def begin(self) -> datetime.datetime:
        if(len(self.time) == 0):
            if(len(self.current_period) == 0):
                raise Exception("Timeseries object has not received any data yet")
            else:
                ret = self.current_period._time[0]
        else:
            ret = self.time[0]
        if not self.averaging_period is None:
            ret = _round_time(ret, self.averaging_period, 0.0)
        return ret

    def _is_period_finished(self, time: datetime.datetime) -> bool:
        ret = False
        if(len(self.current_period) > 0):
            ret = ((time - self.begin()) > self.averaging_period)
        return ret


if __name__ == "__main__":
    ts = Timeseries()
    print(ts)
