from datetime import datetime
class Event:
    def __init__(self, sTime: str, wTime: str, isMovable: bool = True):
        self.tformat = "%H:%M"
        self.sTimeObj = datetime.strptime(sTime, self.tformat)
        self.wTimeObj = datetime.strptime(wTime, self.tformat)

        self.isMovable = isMovable
    # Convert to obj
    def intervalFunction(self):
        # sTimeObj = datetime.strptime(self.sTime, self.tformat)
        # wTimeObj = datetime.strptime(self.wTime, self.tformat)

        diffMins = int((self.wTimeObj - self.sTimeObj).total_seconds() / 60)
        print(f"Difference in minutes before adjustment: {diffMins}")
        
        if diffMins < 0:
            diffMins += 24 * 60
        
        hrInterval = diffMins // 60
        minInterval = diffMins % 60
        timeInterval = f"{hrInterval:02}:{minInterval:02}"
        return timeInterval, diffMins
    def adjustInterval(self, newStart: str, newEnd: str):
        newStartObj = datetime.strptime(newStart, self.tformat)
        newEndObj = datetime.strptime(newEnd, self.tformat)
        if self.isMovable == False:
            return "cannot adjust interval"
        elif newStartObj < self.sTimeObj or newEndObj > self.wTimeObj:
            return "cannot adjust interval"
        
        else: 
            self.sTimeObj = newStartObj
            self.wTimeObj = newEndObj
            return self.intervalFunction()
    
    def overlaps(self, other): # check if two events overlap. if they do, check if the events overlapping are movable, and if they are, adjust the interval. 
        pass

class pEvent(Event): #
    def __init__(self, start: str, end: str, name: str, value: int):
        super().__init__(start, end, isMovable = True)
 
        self.value = value # get from valueFunction
        self.start = start # assg l8er
        self.end = end # depends on start
        self.name = name
        self.prefInterval, self.duration = self.intervalFunction()
    def adjustInterval(self, newStart, newEnd):
        super().adjustInterval(newStart, newEnd)
        self.prefInterval, self.duration = self.intervalFunction()
        
    # def adjustInterval(self, newStart: str, newEnd: str):

    #     newStartObj = datetime.strptime(newStart, self.tformat)
    #     newEndObj = datetime.strptime(newEnd, self.tformat)

    #     if newStartObj < self.start or newEndObj > self.end: # if the new interval is outside the preferred interval, it cannot be scheduled
    #         return "cannot adjust interval"
    #     newInterval, newDuration = self.intervalFunction()
    #     print(f"New interval: {newInterval}, New duration: {newDuration}")
    #     self.prefInterval, self.duration = newInterval, newDuration
        

class eEvent(Event):
    def __init__(self, start: str, end: str, name: str, value: int):
        super().__init__(start, end, isMovable=False)
        self.value = value
        self.name = name
        self.durationInterval, self.duration = self.intervalFunction()

d1 = Event("06:00", "22:00") # this should return 16 hours and 960 minutes
interval, minutes = d1.intervalFunction()
print(f"Interval: {interval}, Difference in minutes: {minutes}\n")

p1 = pEvent("10:00", "14:00", "Meeting", 5) # this should return 4 hours and 240 minutes
print(f"pEvent -> Name: {p1.name}, Interval: {p1.prefInterval}, Movable: {p1.isMovable}\n")

e1 = eEvent("12:00", "15:30", "Workshop", 8) # this should return 3:30 hours and 210 minutes
print(f"eEvent -> Name: {e1.name}, Interval: {e1.durationInterval}, Movable: {e1.isMovable}\n")

p1.adjustInterval("11:00", "13:00") # this should return 2 hours and 120 minutes
print(f"pEvent -> Name: {p1.name}, Interval: {p1.prefInterval}, Movable: {p1.isMovable}\n")


