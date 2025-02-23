from datetime import datetime
from TCNJschedule_logic import *


# whats next? this is the prefPeriod so we need to make a method for that
class Knapsack:
    def __init__(self):
        self.events: list[pEvent] = []
        self.availableEvents: list[pEvent] = None
        # available events should take from the events list and filter out the ones that are not movable and the ones that cannot fit an event
        for event in self.events:
            slotDuration = None # come back to this after we make the intervalFunction
            if not event.isMovable: 
                self.availableEvents.append(event)
            
pEvent1 = pEvent("06:00", "22:00", "Event1", 1)

print(f"pEvent1: {vars(pEvent1)}")
print(f"pEvent2: {vars(pEvent2)}")
print(f"pEvent3: {vars(pEvent3)}")
print("hello")