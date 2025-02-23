from datetime import datetime
import tkinter as tk
from tkinter import Canvas, simpledialog, colorchooser
from TCNJschedule_logic import *
# this is the final version of the TCNJschedule_logic.py and dayClassMethodScratch.py
# we finally got it working lets GOO
class Event:
    def __init__(self, name: str, sTime: str, wTime: str, isMovable: bool = True, color: str = "lightblue"):
        self.name = name
        self.tformat = "%H:%M"
        self.sTimeObj = datetime.strptime(sTime, self.tformat)
        self.wTimeObj = datetime.strptime(wTime, self.tformat)
        self.isMovable = isMovable
        self.color = color

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

class EventApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Calendar")
        
        self.canvas = Canvas(root, width=500, height=400, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        self.events = []
        self.event_widgets = {}
        self.selectedColor = "lightblue"
        
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=1, column=0)
        
        self.start_entry = tk.Entry(root)
        self.start_entry.grid(row=1, column=1)
        
        self.end_entry = tk.Entry(root)
        self.end_entry.grid(row=1, column=2)
        
        self.add_button = tk.Button(root, text="Add Event", command=self.addEventFromUI)
        self.add_button.grid(row=1, column=3)
    
    def addEvent(self, name, sTime, wTime, isMovable, color):
        try:
            event = Event(name, sTime, wTime, isMovable, color)
            if self.hasOverlap(event):
                self.flashEvent(event)
                return
            self.events.append(event)
            self.displayEvents()
        except ValueError:
            print("Invalid time format. Please use HH:MM.")
    
    def addEventFromUI(self):
        name = self.name_entry.get()
        sTime = self.start_entry.get()
        wTime = self.end_entry.get()
        self.addEvent(name, sTime, wTime, True, "lightblue")
    
    def hasOverlap(self, new_event):
        for event in self.events:
            if not event.isMovable and new_event.isMovable:
                if new_event.sTimeObj < event.wTimeObj and new_event.wTimeObj > event.sTimeObj:
                    new_event.wTimeObj = event.sTimeObj  
                    return False
            elif event.sTimeObj < new_event.wTimeObj and event.wTimeObj > new_event.sTimeObj:
                return True
        return False
    
    def displayEvents(self):
        self.canvas.delete("all")
        self.event_widgets.clear()
        for i, event in enumerate(self.events):
            y_pos = i * 40 + 20
            event_widget = self.canvas.create_rectangle(50, y_pos, 450, y_pos + 30, fill=event.color, tags=str(i))
            text_widget = self.canvas.create_text(250, y_pos + 15, text=f"{event.name}: {event.sTimeObj.strftime('%H:%M')} - {event.wTimeObj.strftime('%H:%M')}", tags=str(i))
            
            self.canvas.tag_bind(event_widget, "<ButtonPress-1>", lambda e, ev=event: self.editEvent(ev))
            self.canvas.tag_bind(text_widget, "<ButtonPress-1>", lambda e, ev=event: self.editEvent(ev))
            
            self.event_widgets[event] = (event_widget, text_widget)
    
    def editEvent(self, event):
        new_name = simpledialog.askstring("Edit Event", "Enter new name:", initialvalue=event.name)
        new_start = simpledialog.askstring("Edit Event", "Enter new start time (HH:MM):", initialvalue=event.sTimeObj.strftime('%H:%M'))
        new_end = simpledialog.askstring("Edit Event", "Enter new end time (HH:MM):", initialvalue=event.wTimeObj.strftime('%H:%M'))
        new_color = colorchooser.askcolor(title="Choose Event Color")[1] or event.color
        
        if new_name and new_start and new_end:
            event.name = new_name
            event.sTimeObj = datetime.strptime(new_start, event.tformat)
            event.wTimeObj = datetime.strptime(new_end, event.tformat)
            event.color = new_color
            self.displayEvents()
    
    def flashEvent(self, event):
        if event in self.event_widgets:
            event_widget, _ = self.event_widgets[event]
            for _ in range(3):
                self.canvas.itemconfig(event_widget, fill="red")
                self.root.update()
                self.root.after(200)
                self.canvas.itemconfig(event_widget, fill=event.color)
                self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = EventApp(root)
    root.mainloop()