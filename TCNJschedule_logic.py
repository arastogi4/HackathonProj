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
    def isWithinInterval(event, tCheck: str):
        tCheckObj = datetime.strptime(tCheck, event.tformat)
        if event.sTimeObj <= tCheckObj <= event.wTimeObj:
            return True, f"The time {tCheck} falls within the event interval ({event.sTimeObj.strftime('%H:%M')} - {event.wTimeObj.strftime('%H:%M')})."
        return False, f"The time {tCheck} does NOT fall within the event interval ({event.sTimeObj.strftime('%H:%M')} - {event.wTimeObj.strftime('%H:%M')})."
    def overlapCheck(self, event2):
        
        if self.isWithinInterval(event2.sTimeObj.strftime(self.tformat)) or self.isWithinInterval(event2.wTimeObj.strftime(self.tformat)):
            overlapPt = event2.sTimeObj.strftime(self.tformat) or event2.wTimeObj.strftime(self.tformat)
            return True, f"Event {event2.name} overlaps with event {self.name} at {overlapPt}. {event2.name}."
        return False, f"Event {event2.name} does NOT overlap with event {self.name}."

    def overlapFix(self, event2):

        def overlapPointType(overlapPoint):
            overlapTime = overlapPoint.strftime(self.tformat)
            if overlapTime == event2.sTimeObj.strftime(self.tformat):
                return "start"
            elif overlapTime == event2.wTimeObj.strftime(self.tformat):
                return "end"
            else:
                return "middle"
        if isinstance(event2, pEvent):
            overlapPoint = max(self.sTimeObj, event2.sTimeObj)  # Where the overlap starts
            pointType = overlapPointType(overlapPoint)

            if pointType == "start":
                # Adjust event2's start time forward to match self's end time
                event2.adjustInterval(self.wTimeObj.strftime(self.tformat), event2.wTimeObj.strftime(self.tformat))
            elif pointType == "end":
                # Adjust event2's end time backward to match self's start time
                event2.adjustInterval(event2.sTimeObj.strftime(self.tformat), self.sTimeObj.strftime(self.tformat))
            elif pointType == "middle":
                # If event2 is fully contained within self, shrink it to avoid overlap
                event2.adjustInterval(self.wTimeObj.strftime(self.tformat), event2.wTimeObj.strftime(self.tformat))
            if event2 is type() == pEvent:
                if event2.overlapPointType == "start":
                    event2.adjustInterval(event2.sTimeObj.strftime(self.tformat), self.sTimeObj.strftime(self.tformat))
        pass

class pEvent(Event):
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

print(p1.isWithinInterval("12:00")) # this should return True
print(p1.isWithinInterval("09:00")) # this should return False
print(p1.overlapCheck(e1)) # this should return True
if __name__ == "__main__":
    d1 = Event("06:00", "22:00")
    interval, minutes = d1.intervalFunction()
    print(f"Interval: {interval}, Difference in minutes: {minutes}")

