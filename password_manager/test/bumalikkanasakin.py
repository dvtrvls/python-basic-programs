import pygame as pg
import os
import tkinter as tk
import random

pg.mixer.init()

working_directory = os.getcwd()
folder_name = "music"
folder_path = os.path.join(working_directory, folder_name)  
music_name = "kungmagingakinka.mp3"
music_path = os.path.join(folder_path, music_name)


def click_yes(music_path):
    label["text"] = "YOWN NICE ONE YAHOO SCOOBY DOO BI DOO"
    label2["text"] = ""

    try: 
        pg.mixer.music.load(music_path)
        pg.mixer.music.play()
        print(f"Now playing: {music_path}")
    except pg.error as e:
        print(f"Error playing music: {e}")


def click_no():
    label2["text"] = random.choice(random_texts)
    x = random.randint(0, 400)
    y = random.randint(0, 400)

    # get current size
    current_width = yes_button.cget("width")
    current_height = yes_button.cget("height")

    # increase size
    yes_button.config(width=current_width + 15, height=current_height + 2)

    no_button.place(x=x, y=y)

screen = tk.Tk()
screen.geometry("500x500")
screen.title("Can you be my lover?")
screen.configure(bg="lightpink")

label = tk.Label(screen, text="Pwede bang bumalik ka na sa akin?", font=("Consolas", 18), bg="lightpink", fg="red" )
label.pack(pady=(100, 50))

label2 = tk.Label(screen, text="", font=("Consolas", 15), bg="lightpink", fg="red")
label2.pack(pady=(0, 20))

no_button = tk.Button(screen, text="No", font=("Consolas", 12), bg="lightblue", fg="darkblue",command=click_no)   
no_button.pack(side= "left", pady=10, padx=(50, 10))

yes_button = tk.Button(screen, text="Yes", font=("Consolas", 12), bg="lightblue", fg="darkblue", command=lambda: click_yes(music_path))
yes_button.pack(side="right", pady=10, padx=(10, 50))


random_texts = ["sure ka na ba diyan", "ayaw mo na ba talaga?", "baka magbago isip mo", "cge n plz", "pag-isipan mo pls", "luh parang others naman"]

screen.mainloop()




