from tkinter import *
import pygame as pg


#ask the user to start the count down
#start the count down
#when count down reach zero, countdown 5 minutes for break
#then continue

pg.mixer.init()
pg.mixer.music.set_volume(0.5)

window = Tk()
window.title("Pomodoro Program")
window.config(bg="lightblue")
width = 500
height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

window.geometry(f"{width}x{height}+{x}+{y}")
work_time = 1800
time_ = work_time
break_time = 300

hours = time_ // 3600
minutes = (time_ % 3600) // 60
seconds = time_ % 60
is_work_mode = True
task = None

def update_time():
    global is_work_mode
    global time_ 
    global task

    hours = time_ // 3600
    minutes = (time_ % 3600) // 60
    seconds = time_ % 60
    countdown_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    time_ -= 1
    
    if time_ < 0:
        show_window()
        if is_work_mode:
            # Switch to break mode
            is_work_mode = False
            time_ = break_time # short break for demo
            status_label.config(text="BREAK TIME !!")
        else:
            # Switch back to work mode
            is_work_mode = True
            time_ = work_time
            status_label.config(text="WORK MODE")
        task = window.after(3000, update_time)
        return

    task = window.after(1000, update_time)

status_label = Label(window, text="WORK MODE", font=("Monospace", 20, "bold"), fg="darkblue", bg='lightblue')
status_label.grid(row=0, column=0, padx=165, pady=(30, 10))

control_label = Label(window, text="START", font=("Monospace", 10, "bold"), fg="red", bg='lightblue')
control_label.grid(row=1, column=0, padx=155)

countdown_label = Label(window, text=f"{hours:02d}:{minutes:02d}:{seconds:02d}",font=("Consolas", 50), bg='lightblue')
countdown_label.grid(row=2, column=0, padx=70)
is_paused = True

def pause():
    global task
    if task:
        window.after_cancel(task)

def continue_():
    global task
    task = window.after(1000, update_time)

def control():
    global is_paused
    if not is_paused:
        pause()
        pause_continue_button.config(fg="darkred", bg="lightpink")
        control_label.config(text="PAUSED")
        is_paused = True
    else:
        continue_()
        pause_continue_button.config(bg="lightgreen", fg="darkgreen")
        control_label.config(text="RUNNING")
        is_paused = False


pause_continue_button = Button(window, text="Pause/Continue",font=("Consolas", 15), command=control, state=DISABLED)
pause_continue_button.grid(row=3, column=0)
pause_continue_button.config(fg="darkred", bg="lightpink")

start_button = Button(window, text="Start",font=("Consolas", 15), command=lambda: start(), bg="lightgreen", fg='darkgreen')
start_button.grid(row=4, column=0)

def show_window():
    window.deiconify()
    window.lift()
    window.focus_force()

def set_vol(val):
    new_vol = float(val) / 100
    pg.mixer.music.set_volume(new_vol)

slider_volume = Scale(window, from_=0, to=100, bg="lightblue",orient=HORIZONTAL, fg="darkblue", troughcolor="royalblue", command=set_vol)
slider_volume.grid(row=5, column=0, pady=(30,10))

def start():
    global is_paused
    pause_continue_button.config(state=NORMAL, bg="lightgreen", fg="darkgreen")
    start_button.config(fg="darkred", bg="lightpink", state=DISABLED)
    control_label.config(text="RUNNING")
    is_paused = False
    continue_()

music_paused = False
music_started = False

def play_music():
    global music_paused, music_started

    if not music_started:
        pg.mixer.music.load('music/classicalmusic.mp3')
        pg.mixer.music.play()
        music_started = True
    elif music_paused:
        pg.mixer.music.unpause()
        music_paused = False

def pause_music():
    global music_paused
    pg.mixer.music.pause()
    music_paused = True

def control_music():
    if button_val.get() == 1:
        play_music()
    else:
        pause_music()

button_val = IntVar()
check_button = Checkbutton(window, text="Classical Music", variable=button_val, command=control_music, bg="lightblue", fg="darkblue")
check_button.grid(row=5, column=0, pady=20)

window.mainloop()

