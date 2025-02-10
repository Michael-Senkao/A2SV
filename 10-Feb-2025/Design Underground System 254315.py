# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.checkin = {} # Current checked in customers
        self.average = [] # Average of traveling from station x to station y
        self.station_index = {} # Tracks the index of each station in the railway system
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # Check if the current check in station does no have an index assigned
        if stationName not in self.station_index:
            self.station_index[stationName] = len(self.average) # Assign an index to current station

            self.average.append({}) # Track the average from current statuin to other stations

        self.checkin[id] = (stationName, t) # Check in customer with given id

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # Get check in station and check in time of current the trip
        start_station,start_time = self.checkin[id]

        # Get the index of the checked-in station
        start_station_index = self.station_index[start_station]

        del self.checkin[id] # check out customer with give id

        # Update the total time and number of trips between start station and end station 
        total,count = self.average[start_station_index].get(stationName, (0,0))
        total+=(t - start_time)
        count += 1
        self.average[start_station_index][stationName] = (total, count)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total,count = self.average[self.station_index[startStation]][endStation]
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)