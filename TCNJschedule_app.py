# event_gui.py
import tkinter as tk
from tkinter import messagebox
from TCNJschedule_logic import Event  

class EventApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Scheduler")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Start Time (HH:MM):").grid(row=0, column=0)
        tk.Label(self.root, text="End Time (HH:MM):").grid(row=1, column=0)

        self.start_entry = tk.Entry(self.root)
        self.start_entry.grid(row=0, column=1)

        self.end_entry = tk.Entry(self.root)
        self.end_entry.grid(row=1, column=1)

        self.result_label = tk.Label(self.root, text="", fg="blue")
        self.result_label.grid(row=3, columnspan=2)

        tk.Button(self.root, text="Create Event", command=self.create_event).grid(row=2, columnspan=2)

    def create_event(self):
        start_time = self.start_entry.get()
        end_time = self.end_entry.get()

        try:
            event = Event(start_time, end_time)
            interval, minutes = event.intervalFunction()
            self.result_label.config(text=f"Interval: {interval}, Minutes: {minutes}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter time in HH:MM format")

if __name__ == "__main__":
    root = tk.Tk()
    app = EventApp(root)
    root.mainloop()
