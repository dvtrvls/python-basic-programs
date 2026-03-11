import pygame as pg
import os
from tkinter import *

working_directory = os.getcwd()

def display_musics(music_list):
    lines = ["Available Music:"]
    
    for i, music in enumerate(music_list, start=1):
        lines.append(f"[{i}]. {music}")
    
    return "\n".join(lines)

def validate_user_input(user_input, music_list):
    if user_input is None:
        return False
    if 1 <= user_input <= len(music_list):
        return True
    print("Please enter a number corresponding to the music list.")
    return False

def get_user_input():
    try:
        usr = int(input("Enter the number of the music you want to play: "))
        return usr
    except ValueError:
        print("Please enter a valid number.")
        return None


def get_music_files(folder_name):
    music_path = os.path.join(working_directory, folder_name)
    os.chdir(music_path)
    music_files = []
    for file in os.listdir():
        if file.endswith(".mp3") or file.endswith(".wav"):
            music_files.append(file)
    return music_files

def get_music_choice(music_list):
    while True:
        user_input = get_user_input()
        if validate_user_input(user_input, music_list):
            return music_list[user_input - 1]

def play_music(music_file):
    try:
        pg.mixer.music.load(music_file)
        pg.mixer.music.play()
        print(f"Now playing: {music_file}")
    except pg.error as e:
        print(f"Error playing music: {e}")

def pause_music():
    pg.mixer.music.pause()
    print("Music paused.")

def resume_music():
    pg.mixer.music.unpause()
    print("Music resumed.")


def next_music(music_list, current_music):

    if current_music not in music_list:
        print("Current music is not in the music list.")
        return None
    
    current_index = music_list.index(current_music)
    next_index = (current_index + 1) % len(music_list)
    return music_list[next_index]
def previous_music(music_list, current_music):
    if current_music not in music_list:
        print("Current music is not in the music list.")
        return None
     
    current_index = music_list.index(current_music)
    previous_index = (current_index - 1) % len(music_list)
    return music_list[previous_index]

def main():
    try:
        pg.mixer.init()
    except  pg.error as e:
        print("There is a problem initializing pygame mixer:", e)
        return
    music_list = get_music_files("music")
    if not music_list:
        print("No music files found in the 'music' folder.")
        return
    print(display_musics(music_list))
    music_choice = get_music_choice(music_list) 
    play_music(music_choice)
    while True:
        command = input("Enter 'stop' to stop music, 'resume' to resume music, or 'exit' to quit or 'next'/'previous' to navigate: ").strip().lower()
        if command == 'stop':
            pause_music()
        elif command == 'resume':
            resume_music()
        elif command == 'exit':
            pause_music()
            print("Exiting the music player.")
            break
        elif command == 'next':
            music_choice = next_music(music_list, music_choice)
            play_music(music_choice)
        elif command == 'previous':
            music_choice = previous_music(music_list, music_choice)
            play_music(music_choice)
        else:
            print("Invalid command. Please enter 'stop', 'resume', or 'exit'.")


def gui_main():
    pg.mixer.init()
    screen = Tk()
    screen.title("Music Player")
    screen_width = 500
    screen_height = 700

    # get screen's width and height
    window_width = screen.winfo_screenwidth()
    window_height = screen.winfo_screenheight()

    # calculate x and y coordinates for the window
    x = (window_width // 2) - (screen_width // 2)
    y = (window_height // 2) - (screen_height // 2)

    # set geometry with position
    screen.geometry(f"{screen_width}x{screen_height}+{x}+{y}")
    screen.configure(bg="lightblue")

    label = Label(screen, text="Welcome to the Music Player!", font=("Consolas", 16), bg="lightblue", fg="darkblue")
    label.grid(row=0, column=0, padx=80, pady=(20, 5))

    text_box = Label(screen, text=display_musics(get_music_files("music")), width=40, height=10, font=("Consolas", 12), bg="lightblue", fg="darkblue")
    text_box.grid(row=1, column=0, padx=10, pady=5)

    user_choice = StringVar()

    user_input = Entry(screen, width=1, font=("Consolas", 12), fg="royalblue",text="choice", textvariable=user_choice)
    user_input.grid(row=3, column=0, padx=10, pady=5)

    input_label = Label(screen, text="Enter the number of the music you want to play:", font=("Consolas", 12), bg="lightblue", fg="darkblue")
    input_label.grid(row=2, column=0, padx=10, pady=5)

    submit_button = Button(screen, text="Submit", font=("Consolas", 12), bg="royalblue", fg="white", command=lambda: on_submit())
    submit_button.grid(row=4, column=0, padx=10, pady=5)

    feedback_var = StringVar()
    feedback_label = Label(screen, text="", font=("Consolas", 12), bg="lightblue", fg="darkred", textvariable=feedback_var)
    feedback_label.grid(row=5, column=0, padx=10, pady=5)

    play_pause_button = Button(screen, text="Pause/Resume", font=("Consolas", 12), bg="royalblue", fg="white", command=lambda: pause_music() if pg.mixer.music.get_busy() else resume_music())
    play_pause_button.grid(row=7, column=0, padx=10, pady=5)

    previous_music_button = Button(screen, text="Previous", font=("Consolas", 12), bg="royalblue", fg="white", command=lambda: previous())
    previous_music_button.grid(row=6,padx=10, column=0, pady=5)

    next_music_button = Button(screen, text="Next", font=("Consolas", 12), bg="royalblue", fg="white", command=lambda: next())
    next_music_button.grid(row=8, column=0, padx=10, pady=5)

    def on_submit():
        music_no = user_choice.get()
        if music_no.isdigit():
            music_no = int(music_no)
            music_list = get_music_files("music")
            feedback_var.set("Choice submitted successfully!")
            if validate_user_input(music_no, music_list):
                play_music(music_list[music_no - 1])
            else:
                feedback_var.set("Please enter a valid number.")
        else:
            feedback_var.set("Please enter a valid number.")
        
    def get_current_music():
         music_no = user_choice.get()
         if music_no.isdigit():
            music_no = int(music_no)
            music_list = get_music_files("music")
            feedback_var.set("Choice submitted successfully!")
            if validate_user_input(music_no, music_list):
                return music_list[music_no - 1]
            
    
        
    def next():
        play_music(next_music(get_music_files("music"), get_current_music()))
        if not user_choice.get().isdigit():
            user_choice.set("1")
        current_music_no = user_choice.get()
        user_choice.set(str(int(current_music_no) + 1 if int(current_music_no) < len(get_music_files("music")) else 1))

    def previous():
        play_music(previous_music(get_music_files("music"), get_current_music()))
        if not user_choice.get().isdigit():
            user_choice.set("1")
        current_music_no = user_choice.get()
        user_choice.set(str(int(current_music_no) - 1 if int(current_music_no) > 1 else len(get_music_files("music"))))

    screen.mainloop()

gui_main()









