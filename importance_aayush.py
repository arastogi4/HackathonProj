from datetime import datetime,timedelta
import math
class Event:
    def __init__(self,duration, start, end, name, isMovable = False, rating = None):
        rating
        self.duration = duration
        self.start = start
        self.end = end
        self.name = name
        self.isMovable = isMovable
class Day:
    def __init__(self, sTime: str, wTime: str):
        self.wTime = wTime
        self.sTime = sTime
        self.tformat = "%H:%M"
        self.diffMins = 0

    # Convert to obj
    def intervalFunction(self):
        print(f"Start time: {self.sTime}, End time: {self.wTime}")
        sTimeObj = datetime.strptime(self.sTime, self.tformat)
        wTimeObj = datetime.strptime(self.wTime, self.tformat)
        print(f"Start time object: {sTimeObj}, End time object: {wTimeObj}")

        diffMins = int((wTimeObj - sTimeObj).total_seconds() / 60)
        print(f"Difference in minutes before adjustment: {diffMins}")
        
        if diffMins < 0:
            diffMins += 24 * 60
        
        hrInterval = diffMins // 60
        minInterval = diffMins % 60
        timeInterval = f"{hrInterval:02}:{minInterval:02}"
        return timeInterval, diffMins
    
    def RanEvent(self,Estart,Eend):
        self.Estart = Estart
        self.Eend = Eend
        print(f"Start time: {self.Estart}, End time: {self.Eend}")
        Estart = datetime.strptime(self.Estart, self.tformat)
        Eend = datetime.strptime(self.Eend, self.tformat)
        print(f"Start time object: {Estart}, End time object: {Eend}")
        min = 0
        min = int((Eend-Estart).total_seconds() / 60)
        print(f"Difference in minutes before adjustment: {min}")
        
        if min < 0:
            min += 24 * 60
        
        hrInterval = min // 60
        minInterval = min % 60
        timeInterval = f"{hrInterval:02}:{minInterval:02}"
        return timeInterval, min
    
    def intervalWithinDay(self):
        day_st = datetime.strptime(self.sTime,self.tformat)
        day_end = datetime.strptime(self.wTime,self.tformat)
        self.intervalFunction(day_st,day_end)

    def partition(self,events,itrvlmins):
        currtime = datetime.strptime(self.sTime,self.tformat)
        endtime = datetime.strptime(self.wTime,self.tformat)
        while currtime < endtime:
            p = []
            nextime = currtime + timedelta(minutes=itrvlmins)
            p_events = [ev for ev in events if currtime <= datetime.strptime(str(ev.start), "%H%M") < nextime]
            p.append((currtime.strftime(self.tformat),nextime.strftime(self.tformat), p_events))
            currtime = nextime
            return p

        



class main:
    def military(military_time):
        start = 600
        end = 2200
        military_time = int(military_time)
        time_str = f"{military_time:04d}"  
        return datetime.strptime(time_str, "%H%M")
#Constructor called in the format (Duration(min), starttime (24 hour clock), endtime (24 hour clock), name of event, movable boolean, rating)
App1 = Event(30, 930,"10:00","Short Club")
App2 = Event(80,1100,"12:20","English")
App3 = Event(80,1220,"13:50","Discrete")
PREFf1= Event(20,800,"9:30","Breakfast",True)
events = [
    App1,
    App2,
    App3,
    PREFf1
]
my_day = Day("6:00","22:00")
#    dur = input("Duration: ")
#    sta = input("Start: ")
#    end = input("end: ")
#    name = input("name: ")
#    mov = input("is it moveable: ")

#    sta = military(sta)
#    end = military(end)
#    total_time = sta - end
#    if mov == "no" or "No":
#       mov = False
#    else:
#       mov = True


#    if mov == False and not (total_time == dur):
#        print("There is an error with your start and stop time")
#App4 = Event(dur,sta,end,name,mov)

d1 = Day("06:00", "22:00")

interval, minutes = d1.intervalFunction()

print(d1.RanEvent("8:00","9:30"))

