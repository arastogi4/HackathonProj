from datetime import datetime
class Day:
    def __init__(self, sTime: str, wTime: str):
        self.wTime = wTime
        self.sTime = sTime
        self.tformat = "%H:%M"

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
    def nXORm(self):
        pass
d1 = Day("06:00", "22:00")

interval, minutes = d1.intervalFunction()

print(f"Interval: {interval}, Difference in minutes: {minutes}")



