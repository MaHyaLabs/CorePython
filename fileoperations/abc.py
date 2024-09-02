import tkinter as tk
from tkinter import messagebox
import configparser
import schedule
import time
import threading
import random
from datetime import datetime

# Global variable to track whether to skip the next run
skip_next_run = False


# Function to load settings from config.ini
def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    settings = {
        'healthmantra': config.getboolean('Settings', 'healthmantra', fallback=False),
        'motivational_quotes': config.getboolean('Settings', 'motivational_quotes', fallback=False),
        'moodmeter': config.getboolean('Settings', 'moodmeter', fallback=False)
    }
    return settings


# Function to save settings to config.ini
def save_config(settings):
    config = configparser.ConfigParser()
    config['Settings'] = settings
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


# Function to update settings based on user input
def update_settings():
    settings = {
        'healthmantra': str(var_healthmantra.get()),
        'motivational_quotes': str(var_motivational_quotes.get()),
        'moodmeter': str(var_moodmeter.get())
    }
    save_config(settings)
    messagebox.showinfo("Settings", "Settings saved successfully!")


# Function to show motivational quotes
def show_motivational_quotes():
    global skip_next_run
    if skip_next_run:
        print("Skipping motivational quote display.")
        skip_next_run = False  # Reset the flag after skipping
        return
    print("Showing motivational quote: 'The best time for new beginnings is now.'")


# Function to show moodmeter video
def show_moodmeter():
    global skip_next_run
    if skip_next_run:
        print("Skipping moodmeter video display.")
        skip_next_run = False  # Reset the flag after skipping
        return
    print("Showing moodmeter video...")


# Function to show random healthmantra video
def show_healthmantra_video():
    global skip_next_run
    if skip_next_run:
        print("Skipping healthmantra video display.")
        skip_next_run = False  # Reset the flag after skipping
        return
    videos = ['a.mp4', 'b.mp4', 'c.mp4']
    video = random.choice(videos)
    print(f"Showing healthmantra video: {video}")


# Function to skip the next run
def skip_next():
    global skip_next_run
    skip_next_run = True
    print("Next run will be skipped.")


# Task scheduler function
def schedule_tasks():
    settings = load_config()
    if settings['motivational_quotes']:
        schedule.every().day.at("11:00").do(show_motivational_quotes)
    if settings['moodmeter']:
        schedule.every().day.at("15:00").do(show_moodmeter)
    if settings['healthmantra']:
        schedule.every().minutes.do(show_healthmantra_video)

    while True:
        schedule.run_pending()
        time.sleep(1)


# Create the main window
root = tk.Tk()
root.title("DeskFit Application")

# Create variables for checkboxes
var_healthmantra = tk.BooleanVar()
var_motivational_quotes = tk.BooleanVar()
var_moodmeter = tk.BooleanVar()
var_skip_next = tk.BooleanVar()

# Create Settings page
settings_frame = tk.Frame(root)
settings_frame.pack(padx=10, pady=10)

tk.Checkbutton(settings_frame, text="Healthmantra", variable=var_healthmantra).pack(anchor='w')
tk.Checkbutton(settings_frame, text="Motivational Quotes", variable=var_motivational_quotes).pack(anchor='w')
tk.Checkbutton(settings_frame, text="Moodmeter", variable=var_moodmeter).pack(anchor='w')

tk.Checkbutton(settings_frame, text="Skip Next Run", variable=var_skip_next, command=skip_next).pack(anchor='w')
tk.Button(settings_frame, text="Save Settings", command=update_settings).pack(pady=10)

# Load and apply saved settings
settings = load_config()
var_healthmantra.set(settings['healthmantra'])
var_motivational_quotes.set(settings['motivational_quotes'])
var_moodmeter.set(settings['moodmeter'])

# Start scheduling tasks in a separate thread
threading.Thread(target=schedule_tasks, daemon=True).start()

# Run the application
root.mainloop()
