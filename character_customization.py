from tkinter import *
import tkinter as tk
import ctypes
from PIL import Image, ImageTk
character_customization = []
graphics_elements = []
klan_list = []
def destroy_graphic_elements():
    for i in range(len(graphics_elements)):
        graphics_elements[i].destroy()
        i += 1
def get_1_answer_1_question_button_command():
    character_customization.append("samurai")
    destroy_graphic_elements()
def get_2_answer_1_question_button_command():
    character_customization.append("assasyn")
    destroy_graphic_elements()
def get_3_answer_1_question_button_command():
    character_customization.append("monk")
    destroy_graphic_elements()
def get_4_answer_1_question_button_command():
    character_customization.append("fisherman")
    destroy_graphic_elements()
WIDTH = ctypes.windll.user32.GetSystemMetrics(0)
HEIGHT = ctypes.windll.user32.GetSystemMetrics(1)
root = tk.Tk()
root.state("zoomed")
root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('Samurai no jikan')
question_menu_background_image = Image.open('assets/character_creation_background_question1.png')
question_menu_background_image = question_menu_background_image.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
resized1 = ImageTk.PhotoImage(question_menu_background_image)
backgroundLabel = tk.Label(root, image=resized1)
backgroundLabel.place(x=0, y=0)
firstAsnwerButton = Button(root, text="samurai", padx=40, pady=9,
                           command=lambda: get_1_answer_1_question_button_command(), bg="#439f9c")
firstAsnwerButton.pack()
firstAsnwerButton.place(x=550, y=250)
secondAnswerButton = Button(root, text="assasyn", padx=40, pady=9,
                            command=lambda: get_2_answer_1_question_button_command(), bg="#439f9c")
secondAnswerButton.pack()
secondAnswerButton.place(x=550, y=150)
thirdAnswerButton = Button(root, text="monk", padx=40, pady=9,
                            command=lambda: get_3_answer_1_question_button_command(), bg="#439f9c")
thirdAnswerButton.pack()
thirdAnswerButton.place(x=550, y=350)
fourthAnswerButton = Button(root, text="fisherman", padx=40, pady=9,
                            command=lambda: get_4_answer_1_question_button_command(), bg="#439f9c")
fourthAnswerButton.pack()
fourthAnswerButton.place(x=550, y=450)
graphics_elements.append(firstAsnwerButton)
graphics_elements.append(thirdAnswerButton)
graphics_elements.append(secondAnswerButton)
graphics_elements.append(fourthAnswerButton)
graphics_elements.append(backgroundLabel)
root.mainloop()

