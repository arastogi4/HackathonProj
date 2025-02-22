from datetime import datetime

class Event:
    def __init__(self,duration, start, end, name, isMovable = False, rating = None):
        rating
        self.duration = duration
        self.start = start
        self.end = end
        self.name = name
        self.isMovable = isMovable
    def ratingAlgo(rating):
       

class main:
   def military(military_time):
    
    military_time = int(military_time)
    time_str = f"{military_time:04d}"  
    return datetime.strptime(time_str, "%H%M")
   #Constructor called in the format (Duration(min), starttime (24 hour clock), endtime (24 hour clock), name of event, movable boolean, rating)
   App1 = Event(30, 930,1000,"Short Club")
   App2 = Event(80,1100,1220,"English")
   App3 = Event(80,1220,1350,"Discrete")
   PREFf1= Event(20,800,930,"Breakfast",True)

   dur = input("Duration: ")
   sta = input("Start: ")
   end = input("end: ")
   name = input("name: ")
   mov = input("is it moveable: ")

   sta = military(sta)
   end = military(end)
   total_time = sta - end
   if mov == "no" or "No":
      mov = False
   else:
      mov = True


   if mov == False and not (total_time == dur):
       print("There is an error with your start and stop time")

   App4 = Event(dur,sta,end,name,mov)
   print(App4.duration)

   




