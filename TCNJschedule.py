from datetime import datetime
class Event:
    def __init__(self, sTime: str, wTime: str, isMovable: bool = True):
        self.wTime = wTime
        self.sTime = sTime
        self.tformat = "%H:%M"
        self.isMovable = isMovable
    # Convert to obj
    def intervalFunction(self):
        sTimeObj = datetime.strptime(self.sTime, self.tformat)
        wTimeObj = datetime.strptime(self.wTime, self.tformat)

        diffMins = int((wTimeObj - sTimeObj).total_seconds() / 60)
        print(f"Difference in minutes before adjustment: {diffMins}")
        
        if diffMins < 0:
            diffMins += 24 * 60
        
        hrInterval = diffMins // 60
        minInterval = diffMins % 60
        timeInterval = f"{hrInterval:02}:{minInterval:02}"
        return timeInterval, diffMins

class pEvent(Event): #
    def __init__(self, start: str, end: str, name: str, value: int):
        super().__init__(start, end, isMovable = True)
 
        self.value = value # get from valueFunction
        self.start = start # assg l8er
        self.end = end # depends on start
        self.name = name
        self.prefInterval, self.duration = self.intervalFunction()
    def adjustInterval(self, newStart: str, newEnd: str):
        self.start = newStart
        self.end = newEnd
        self.prefInterval, self.duration = self.intervalFunction()

class eEvent(Event):
    def __init__(self, start: str, end: str, name: str, value: int):
        super().__init__(start, end, isMovable=False)
        self.value = value
        self.name = name
        self.durationInterval, self.duration = self.intervalFunction()

d1 = Event("06:00", "22:00")
interval, minutes = d1.intervalFunction()
print(f"Interval: {interval}, Difference in minutes: {minutes}")

p1 = pEvent("10:00", "14:00", "Meeting", 5)
print(f"pEvent -> Name: {p1.name}, Interval: {p1.prefInterval}, Movable: {p1.isMovable}")

e1 = eEvent("12:00", "15:30", "Workshop", 8)
print(f"eEvent -> Name: {e1.name}, Interval: {e1.durationInterval}, Movable: {e1.isMovable}")
p1.adjustInterval("09:00", "13:00")
print(f"pEvent -> Name: {p1.name}, Interval: {p1.prefInterval}, Movable: {p1.isMovable}")


