from tkinter import *

# CONSTANT
PHOTO_FILE_NAME = "tomato.png"
CHECK_FILE_NAME = "check.png"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# COLOR PALETTE OF THE PROGRAM

BIEGE = "#fff2c6"
LIGHTER_BIEGE = "#FFF8DE"
PASTEL_GREEN = "#6FAF4F"
SKY_BLUE = "#8ca9ff"
SWEET_RED = "#FA5C5C"

#status

is_work_mode = True
session_finished = 0
countdown_func = None
is_started = False

#gui

screen = Tk()
screen.title("Pomodoro Ver 2")
screen.config(bg=BIEGE, padx=20, pady=20)
screen.resizable(False, False)

timer_label = Label(screen, text= "T I M E R", font=("Consolas", 30, "bold"), bg=BIEGE, fg=SWEET_RED)
timer_label.pack()

check_xcoordinates = (210, 240, 270)
check_images = []

tomato_photo = PhotoImage(file=PHOTO_FILE_NAME)
check_photo = PhotoImage(file=CHECK_FILE_NAME)
canvas = Canvas(screen, width=500, height=500, bg=BIEGE, highlightthickness=0)
canvas.create_image(260 , 220, image=tomato_photo)
canvas.pack(anchor=CENTER)

#time_left_in_seconds = WORK_MIN * 60
time_left_in_seconds = 5
hours = time_left_in_seconds // 3600
minutes = (time_left_in_seconds % 3600) // 60
seconds = time_left_in_seconds % 60

def update():
    global time_left_in_seconds, countdown_func, is_work_mode, session_finished
    hours = time_left_in_seconds // 3600
    minutes = (time_left_in_seconds % 3600) // 60
    seconds = time_left_in_seconds % 60
    canvas.itemconfig(timetext_id, text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    time_left_in_seconds -= 1

    if time_left_in_seconds < 0:
        show_window()
        if is_work_mode:
            is_work_mode = False
            chck_img =  canvas.create_image(check_xcoordinates[session_finished], 350, image=check_photo)
            check_images.append(chck_img)         
            session_finished += 1
            
            if session_finished < 3:
                canvas.itemconfig(statustext_id, text=f"BREAK TIME")
                time_left_in_seconds = 3
            else:
                screen.after(1000, long_breaks)

        else:
            is_work_mode = True
            canvas.itemconfig(statustext_id, text=f"WORK MODE")
            time_left_in_seconds = 5

    countdown_func = screen.after(1000, update)


def long_breaks():
   global time_left_in_seconds, session_finished
   for img in check_images:
        canvas.delete(img)
        canvas.itemconfig(statustext_id, text=f"LONG BREAK TIME")
        time_left_in_seconds = 10
        session_finished = 0
    

timetext_id = canvas.create_text(250, 250, text=f"{hours:02d}:{minutes:02d}:{seconds:02d}", font=(FONT_NAME, 48, "bold"), fill=LIGHTER_BIEGE)
statustext_id = canvas.create_text(250, 285, text="START", font=(FONT_NAME, 24, "bold"), fill=PASTEL_GREEN)

start_button = Button(screen, text="Start", font=(FONT_NAME, 20, "bold"), bg=SWEET_RED, command=lambda: start_countdown())
start_button.pack(side=LEFT, padx=30, pady=(20, 20))

reset_button = Button(screen, text="Reset", font=(FONT_NAME, 20, "bold"), bg=PASTEL_GREEN, command=lambda: reset_button_func())
reset_button.pack(side=RIGHT, padx=30, pady=(20, 20))

def start_countdown():
    global is_started, countdown_func
    if not is_started:
        is_started = True
        countdown_func = screen.after(100, update)
        canvas.itemconfig(statustext_id, text=f"WORK MODE")

def reset_button_func():
    global time_left_in_seconds
    time_left_in_seconds = WORK_MIN * 60

def show_window():
    screen.deiconify()
    screen.lift()
    screen.focus_force()      
screen.mainloop()













