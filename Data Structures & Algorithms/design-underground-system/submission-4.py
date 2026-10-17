from collections import defaultdict

class UndergroundSystem:
    def __init__(self):
        self.checkin = {}
        self.trips = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkin and self.checkin[id][1] == t:
            return

        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time = t - self.checkin[id][1]
        start = self.checkin[id][0]

        if (start, stationName) not in self.trips:
            self.trips[(start, stationName)] = [0, 0]
        self.trips[(start, stationName)][0] += time
        self.trips[(start, stationName)][1] += 1

        del self.checkin[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime = self.trips[(startStation, endStation)][0]
        count = self.trips[(startStation, endStation)][1]
        return totalTime / count
