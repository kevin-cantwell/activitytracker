import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import time
import threading

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

    activities = ["Gmail", "Code", "Slack", "Reading Docs", "Writing Docs", "Making Slides", "Procrastinating"]
    activity = messagebox.askquestion("Activity Tracker", "What are you doing?", type="custom", default="Gmail",
                                      custom_buttons=activities)

    if activity != "cancel":
        record_activity(activity)

    root.destroy()

def scheduler():
    current_hour = datetime.now().hour
    while 9 <= current_hour < 17:
        prompt_user()
        time.sleep(3600)
        current_hour = datetime.now().hour

if __name__ == "__main__":
    setup_database()
    activity_tracking_thread = threading.Thread(target=scheduler)
    activity_tracking_thread.start()
