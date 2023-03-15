import tkinter as tk
from tkinter import simpledialog
import sqlite3
from datetime import datetime
import time
import multiprocessing

class ActivityDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        self.result = None
        simpledialog.Dialog.__init__(self, parent, title)

    def body(self, master):
        activities = ["Gmail", "Code", "Slack", "Reading Docs", "Writing Docs", "Making Slides", "Procrastinating"]
        row = 0
        col = 0

        for activity in activities:
            button = tk.Button(master, text=activity, width=20, command=lambda a=activity: self.set_result(a))
            button.grid(row=row, column=col)

            col += 1
            if col > 2:
                col = 0
                row += 1

        return None

    def set_result(self, activity):
        self.result = activity
        self.ok()

def setup_database():
    conn = sqlite3.connect("activities.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS activities
                     (timestamp TEXT, activity TEXT)''')
    conn.commit()
    conn.close()

def record_activity(activity):
    conn = sqlite3.connect("activities.db")
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO activities (timestamp, activity) VALUES (?, ?)", (timestamp, activity))
    conn.commit()
    conn.close()

def prompt_user():
    root = tk.Tk()
    root.withdraw()
    activity = ActivityDialog(root, "Activity Tracker").result
    root.destroy()

    if activity:
        record_activity(activity)

def scheduler():
    current_hour = datetime.now().hour
    while 9 <= current_hour < 17:
        prompt_user()
        time.sleep(3600)
        current_hour = datetime.now().hour

if __name__ == "__main__":
    setup_database()
    scheduler_process = multiprocessing.Process(target=scheduler)
    scheduler_process.start()
    scheduler_process.join()
