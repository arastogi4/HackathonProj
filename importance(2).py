from datetime import datetime
class Peg():

    counter = 0
    #Rings = [p1(), p2(), p3()]
    def __init__(self, rings = 0, empty = True, compliant = True, cardinal = 0):
        Peg.counter +=1

        self.rings = rings
        self.empty = empty
        self.compliant = compliant
        self.cardinal = Peg.counter
    def __str__(self):
        return f"Peg info: \nRings: {self.rings}\nCompliant: {self.compliant}\nEmpty: {self.empty}"
    def getRings(self):
        return self.rings
    def setRings(self, ringAmt):
        # self.rings = ringList
        ringData = {}
        for x in range(ringAmt):
            ringData['r' + str(ringAmt)] = Ring(ringAmt, self.cardinal)
            ringAmt -= 1
            if ringAmt == 0:
                break
        self.rings = ringData
    def isCompliant(self):
    # rule: a peg cannot be moved on top of a smaller one
    # corollary: a peg cannot ever be on top of a smaller one
        ringVals = list(self.rings.values())
       # print(ringVals)
        ringSizes = []
        for x in ringVals:
            ringSizes.append(x.getSize())
      #  print(ringSizes)

     #   print(sorted(ringSizes, reverse = True))
        if ringSizes == sorted(ringSizes, reverse = True):
            self.compliant = True
        else: 
            self.compliant = False
        return self.compliant
    def isEmpty(self):
        keys = [*self.rings]
        values = list(self.rings.values())
        if not keys and not values:
            self.empty = True
        else: 
            self.empty = False
        return self.empty
class Ring(): 
    def __init__(self, size, peg = None):
        self.size = size
        self.peg = peg
        self.parity = self.getParity()
        self.destination = None
    def __str__(self):
        return f"Ring({self.size}, {self.parity}, {self.peg})"
    def __repr__(self):
        return self.__str__()
    def getSize(self):
        return self.size
    def getPeg(self):
        return self.peg
    def getParity(self):
        if self.size % 2 == 0:
            return "even"
        else:
            return "odd"
    def findDestination():
        pass

        
# list = []

# list.append(Ring(3))
# list.append(Ring(2))
# list.append(Ring(1))
# p1, p2, p3 = Peg(), Peg(), Peg()
# pList = [p1, p2, p3]

# p1.setRings(list)
# for x in pList:
#     print(x)

p1 = Peg()
# p1.setRings(1)
# print(p1.getRings())
# print(p1.isCompliant())
# print(p1.isEmpty())
# print(p1)
p2 = Peg()
p2.setRings(1)
print(p2)
print("\n\n\n" + str(p2.cardinal))
class Day: # rn this class defines a day, we need to add the 
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
    def dayFunction(self):
        
    def nXORm(self):
        pass
d1 = Day("06:00", "22:00")

interval, minutes = d1.intervalFunction()

print(f"Interval: {interval}, Difference in minutes: {minutes}")



