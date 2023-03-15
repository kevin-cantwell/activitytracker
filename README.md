# Activity Tracker

Activity Tracker is a simple Python script that prompts the user once per hour during the workday (9 am to 5 pm) to select their current activity from a list of predefined options. The user's selected activity and its corresponding timestamp are recorded in an SQLite database.

## Features

- Customizable activity buttons
- Hourly prompts during the workday
- SQLite database to store activity data with timestamps

## Dependencies

- Python 3
- SQLite3

## Setup

1. Ensure you have Python 3 installed. You can download it from [the official Python website](https://www.python.org/downloads/).

2. Clone this repository or download the `activity_tracker.py` script.

```bash
git clone https://github.com/yourusername/activitytracker.git
```

Navigate to the folder containing the activity_tracker.py script in your terminal.
```bash
cd activitytracker
```

Run the script.
```bash
python3 activity_tracker.py
```

The script will now prompt you once per hour during the workday to select your current activity from the available options.

## Modifying Activities
If you would like to customize the list of activities, edit the activities list in the ActivityDialog class within the activity_tracker.py script:

```python
activities = ["Gmail", "Code", "Slack", "Reading Docs", "Writing Docs", "Making Slides", "Procrastinating"]
```

Add or remove activities as needed, and then run the script again.

## Viewing Recorded Data
The script stores the selected activities and their timestamps in an SQLite database named activities.db. To view the recorded data, you can use an SQLite browser or run SQLite commands in your terminal.

For example, to view all records in the database, run the following command in your terminal:

```bash
sqlite3 activities.db "SELECT * FROM activities;"
```


