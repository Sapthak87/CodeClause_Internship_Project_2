import tkinter as tk
import datetime
import time
import winsound

def set_alarm():
    alarm_time = entry.get()
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            window1 = tk.Tk()
            label = tk.Label(window1, text="The alarm is ringing")
            label.pack()
            play_alarm()
            window1.mainloop()
            break

def play_alarm():
    winsound.PlaySound('C:\Vector Calculus\Bell.wav', winsound.SND_ASYNC)

window = tk.Tk()
window.title("Alarm Clock")

label = tk.Label(window, text="Enter alarm time (HH:MM:SS):")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Set Alarm", command=set_alarm)
button.pack()

window.mainloop()