from collections import defaultdict

class UndergroundSystem:
    def __init__(self):
        self.checkin = {}
        self.trips = defaultdict(list)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkin and self.checkin[id][1] == t:
            return

        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time = t - self.checkin[id][1]
        start = self.checkin[id][0]
        self.trips[(start, stationName)].append(time) 

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.trips[(startStation, endStation)]
        return sum(times) / len(times)
