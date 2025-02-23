from datetime import datetime
import tkinter as tk
from tkinter import messagebox, Canvas

class Event:
    def __init__(self, sTime: str, wTime: str, isMovable: bool = True):
        self.tformat = "%H:%M"
        self.sTimeObj = datetime.strptime(sTime, self.tformat)
        self.wTimeObj = datetime.strptime(wTime, self.tformat)
        self.isMovable = isMovable

    def intervalFunction(self):
        diffMins = int((self.wTimeObj - self.sTimeObj).total_seconds() / 60)
        if diffMins < 0:
            diffMins += 24 * 60
        hrInterval = diffMins // 60
        minInterval = diffMins % 60
        return f"{hrInterval:02}:{minInterval:02}", diffMins
    
    def adjustInterval(self, newStart: str, newEnd: str):
        newStartObj = datetime.strptime(newStart, self.tformat)
        newEndObj = datetime.strptime(newEnd, self.tformat)
        if not self.isMovable:
            return "Cannot adjust interval"
        elif newStartObj < self.sTimeObj or newEndObj > self.wTimeObj:
            return "Cannot adjust interval"
        else:
            self.sTimeObj = newStartObj
            self.wTimeObj = newEndObj
            return self.intervalFunction()

    def isWithinInterval(self, tCheck: str):
        tCheckObj = datetime.strptime(tCheck, self.tformat)
        return self.sTimeObj <= tCheckObj <= self.wTimeObj

class EventApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Calendar")
        
        self.canvas = Canvas(root, width=500, height=400, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        
        tk.Label(root, text="Start Time (HH:MM):").grid(row=1, column=0, padx=5, pady=5)
        self.startTimeInput = tk.Entry(root)
        self.startTimeInput.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(root, text="End Time (HH:MM):").grid(row=2, column=0, padx=5, pady=5)
        self.endTimeInput = tk.Entry(root)
        self.endTimeInput.grid(row=2, column=1, padx=5, pady=5)
        
        self.movableCheckBoxVar = tk.BooleanVar()
        self.movableCheckBox = tk.Checkbutton(root, text="Movable Event", variable=self.movableCheckBoxVar)
        self.movableCheckBox.grid(row=3, columnspan=2, padx=5, pady=5)
        
        self.addButton = tk.Button(root, text="Add Event", command=self.addEvent)
        self.addButton.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
        self.events = []
        self.event_widgets = []
    
    def addEvent(self):
        sTime = self.startTimeInput.get()
        wTime = self.endTimeInput.get()
        isMovable = self.movableCheckBoxVar.get()
        
        try:
            event = Event(sTime, wTime, isMovable)
            self.events.append(event)
            self.displayEvent(event)
        except ValueError:
            messagebox.showerror("Error", "Invalid time format. Please use HH:MM.")
    
    def displayEvent(self, event):
        y_pos = len(self.events) * 40 + 20
        event_widget = self.canvas.create_rectangle(50, y_pos, 450, y_pos + 30, fill="lightblue")
        text_widget = self.canvas.create_text(250, y_pos + 15, text=f"{event.sTimeObj.strftime('%H:%M')} - {event.wTimeObj.strftime('%H:%M')}")
        
        if event.isMovable:
            self.canvas.tag_bind(event_widget, "<ButtonPress-1>", lambda e, ew=event_widget, ev=event: self.startMove(e, ew, ev))
            self.canvas.tag_bind(event_widget, "<B1-Motion>", lambda e, ew=event_widget, ev=event: self.onMove(e, ew, ev))
            self.canvas.tag_bind(text_widget, "<ButtonPress-1>", lambda e, ew=event_widget, ev=event: self.startMove(e, ew, ev))
            self.canvas.tag_bind(text_widget, "<B1-Motion>", lambda e, ew=event_widget, ev=event: self.onMove(e, ew, ev))
            
        self.event_widgets.append((event_widget, text_widget, event))
    
    def startMove(self, event, widget, event_obj):
        self.canvas.tag_raise(widget)
        self.lastY = event.y
        self.movingEvent = event_obj
    
    def onMove(self, event, widget, event_obj):
        dy = event.y - self.lastY
        self.canvas.move(widget, 0, dy)
        self.lastY = event.y
        
        # Update event time logic (Placeholder)
        newStart = event_obj.sTimeObj.strftime('%H:%M')
        newEnd = event_obj.wTimeObj.strftime('%H:%M')
        event_obj.adjustInterval(newStart, newEnd)

if __name__ == "__main__":
    root = tk.Tk()
    app = EventApp(root)
    root.mainloop()
