import socket
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import ctypes
import random
import pickle
from Player import *
import pygame
from EnemyClass import *
from Attack import *
import time

# permanent
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
# usage in send() function will disconnect from serwer
DISCONNECT_MESSAGE = "!DISCONNECT"
# server ip adress
SERVER = "192.168.137.1"
ADDR = (SERVER, PORT)
# player(account) username for further use
username = ""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
# list of elements to destroy
graphics_elements = []
# List for character creation use
character_customization = []
# dict for sending pickles with class object parameters
player_class_dictionary_global = {}
# main window setup
WIDTH = 1280
HEIGHT = 720
#WIDTH = ctypes.windll.user32.GetSystemMetrics(0)
#HEIGHT = ctypes.windll.user32.GetSystemMetrics(1)
root = tk.Tk()
root.state("zoomed")
root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('Samurai no jikan')
player_object_saver  = {}
# Clans dictionary used for function character_clan_answer_logic which chose class in time of first login
clans_dictionary_with_answers = {"Raitoningu": {"firstquestion": 1,
                                                "name": "Raitoningu",
                                                "secondquestion": 1,
                                                "thirdquestion": 1,
                                                "fourthquestion": 1},
                                 "Same": {"firstquestion": 1,
                                          "name": "Same",
                                          "secondquestion": 1,
                                          "thirdquestion": 2,
                                          "fourthquestion": 1},
                                 "Chimamire no kiri": {"firstquestion": 1,
                                                       "name": "Chimamire no kiri",
                                                       "secondquestion": 1,
                                                       "thirdquestion": 1,
                                                       "fourthquestion": 2},
                                 "Mizunoken": {"firstquestion": 1,
                                               "name": "Mizunoken",
                                               "secondquestion": 1,
                                               "thirdquestion": 2,
                                               "fourthquestion": 2},
                                 "Tekondō": {"firstquestion": 1,
                                             "name": "Tekondō",
                                             "secondquestion": 2,
                                             "thirdquestion": 1,
                                             "fourthquestion": 1},
                                 "Jakkaru": {"firstquestion": 1,
                                             "name": "Jakkaru",
                                             "secondquestion": 2,
                                             "thirdquestion": 2,
                                             "fourthquestion": 1},
                                 "Kin'iro no me": {"firstquestion": 1,
                                                   "name": "Kin'iro no me",
                                                   "secondquestion": 2,
                                                   "thirdquestion": 1,
                                                   "fourthquestion": 2},
                                 "Doku": {"firstquestion": 1,
                                          "name": "Doku",
                                          "secondquestion": 2,
                                          "thirdquestion": 2,
                                          "fourthquestion": 2},
                                 "Shibō": {"firstquestion": 2,
                                           "name": "Shibō",
                                           "secondquestion": 1,
                                           "thirdquestion": 1,
                                           "fourthquestion": 1},
                                 "Chikaku-teki": {"firstquestion": 2,
                                                  "name": "Chikaku-teki",
                                                  "secondquestion": 1,
                                                  "thirdquestion": 2,
                                                  "fourthquestion": 1},
                                 "Atsuryoku-ten": {"firstquestion": 2,
                                                   "name": "Atsuryoku-ten",
                                                   "secondquestion": 1,
                                                   "thirdquestion": 1,
                                                   "fourthquestion": 2},
                                 "Inu no tomodachi": {"firstquestion": 2,
                                                      "name": "Inu no tomodachi",
                                                      "secondquestion": 1,
                                                      "thirdquestion": 2,
                                                      "fourthquestion": 2},
                                 "Hakushoku hikari": {"firstquestion": 2,
                                                      "name": "Hakushoku hikari",
                                                      "secondquestion": 2,
                                                      "thirdquestion": 1,
                                                      "fourthquestion": 1},
                                 "Wāmu": {"firstquestion": 2,
                                          "name": "Wāmu",
                                          "secondquestion": 2,
                                          "thirdquestion": 2,
                                          "fourthquestion": 1},
                                 "Hen'i-tai": {"firstquestion": 2,
                                               "name": "Hen'i-tai",
                                               "secondquestion": 2,
                                               "thirdquestion": 2,
                                               "fourthquestion": 2},
                                 "Shinkō": {"firstquestion": 2,
                                            "name": "Shinkō",
                                            "secondquestion": 2,
                                            "thirdquestion": 1,
                                            "fourthquestion": 2},
                                 "Ningyō": {"firstquestion": 3,
                                            "name": "Ningyō",
                                            "secondquestion": 1,
                                            "thirdquestion": 1,
                                            "fourthquestion": 1},
                                 "Kusuri": {"firstquestion": 3,
                                            "name": "Kusuri",
                                            "secondquestion": 1,
                                            "thirdquestion": 2,
                                            "fourthquestion": 1},
                                 "Shadouasashin": {"firstquestion": 3,
                                                   "name": "Shadouasashin",
                                                   "secondquestion": 1,
                                                   "thirdquestion": 1,
                                                   "fourthquestion": 2},
                                 "Kōri": {"firstquestion": 3,
                                          "name": "Kōri",
                                          "secondquestion": 1,
                                          "thirdquestion": 2,
                                          "fourthquestion": 2},
                                 "Ketsueki": {"firstquestion": 3,
                                              "name": "Ketsueki",
                                              "secondquestion": 2,
                                              "thirdquestion": 1,
                                              "fourthquestion": 1},
                                 "Shinrin": {"firstquestion": 3,
                                             "name": "Shinrin",
                                             "secondquestion": 2,
                                             "thirdquestion": 2,
                                             "fourthquestion": 1},
                                 "Hagane": {"firstquestion": 3,
                                            "name": "Hagane",
                                            "secondquestion": 2,
                                            "thirdquestion": 1,
                                            "fourthquestion": 2},
                                 "Maguneshiumu": {"firstquestion": 3,
                                                  "name": "Maguneshiumu",
                                                  "secondquestion": 2,
                                                  "thirdquestion": 2,
                                                  "fourthquestion": 2},
                                 "Kopī": {"firstquestion": 4,
                                          "name": "Kopī",
                                          "secondquestion": 1,
                                          "thirdquestion": 1,
                                          "fourthquestion": 1},
                                 "Kage no senshi": {"firstquestion": 4,
                                                    "name": "Kage no senshi",
                                                    "secondquestion": 1,
                                                    "thirdquestion": 2,
                                                    "fourthquestion": 1},
                                 "Mippei suru": {"firstquestion": 4,
                                                 "name": "Mippei suru",
                                                 "secondquestion": 1,
                                                 "thirdquestion": 1,
                                                 "fourthquestion": 2},
                                 "Maindo": {"firstquestion": 4,
                                            "name": "Maindo",
                                            "secondquestion": 1,
                                            "thirdquestion": 2,
                                            "fourthquestion": 2},
                                 "Arashi": {"firstquestion": 4,
                                            "name": "Arashi",
                                            "secondquestion": 2,
                                            "thirdquestion": 1,
                                            "fourthquestion": 1},
                                 "Taimatsu": {"firstquestion": 4,
                                              "name": "Taimatsu",
                                              "secondquestion": 2,
                                              "thirdquestion": 2,
                                              "fourthquestion": 1},
                                 "Shizen": {"firstquestion": 4,
                                            "name": "Shizen",
                                            "secondquestion": 2,
                                            "thirdquestion": 1,
                                            "fourthquestion": 2},
                                 "Kemuri": {"firstquestion": 4,
                                            "name": "Kemuri",
                                            "secondquestion": 2,
                                            "thirdquestion": 2,
                                            "fourthquestion": 2},
                                 "Hikari": {"firstquestion": 4,
                                            "name": "Hikari",
                                            "secondquestion": 2,
                                            "thirdquestion": 1,
                                            "fourthquestion": 1},
                                 "Kumo": {"firstquestion": 4,
                                          "name": "Kumo",
                                          "secondquestion": 2,
                                          "thirdquestion": 2,
                                          "fourthquestion": 2},
                                 }

# lists used to choice the class in character_clans_answer_logic
clans_list = ['Raitoningu', "Same", "Chimamire no kiri", "Mizunoken", "Tekondō", "Jakkaru", "Kin'iro no me", "Doku",
              "Shibō", "Chikaku-teki", "Atsuryoku-ten", "Inu no tomodachi", "Wāmu", "Hakushoku hikari", "Hen'i-tai",
              "Shinkō", "Ningyō", "Kusuri", "Shadouasashin", "Kōri", "Ketsueki", "Shinrin", "Hagane", "Maguneshiumu",
              "Kopī", "Kage no senshi", "Mippei suru", "Maindo", "Arashi", "Taimatsu", "Shizen", "Kemuri", "Hikari",
              "Kumo"]
clans_list_after_first_question = []
clans_list_after_second_question = []
clans_list_after_third_question = []
clans_list_after_fourth_question = []


# thanks to that using "tab" change the widget insted of making space
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return ("break")


# comunication with server sending message and comented line is for taking responds
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    # server_respond = (client.recv(2048).decode(FORMAT))
    # print(server_respond)


# first time login - character class choice system
def character_clan_answers_logic(first_question_answer, second_question_answer, third_question_answer,
                                 fourth_question_answer):
    # dependence of user choice in 4 questions, funcion will update lists and make choice of final clan
    character_clan_answers_logic_checker = 0
    first_question = first_question_answer
    second_question = second_question_answer
    third_question = third_question_answer
    fourth_question = fourth_question_answer
    if first_question == "1":
        for i in range(len(clans_list)):
            if clans_dictionary_with_answers[clans_list[i]]["firstquestion"] == 1:
                clans_list_after_first_question.append(clans_dictionary_with_answers[clans_list[i]]["name"])
    if first_question == "2":
        for i in range(len(clans_list)):
            if clans_dictionary_with_answers[clans_list[i]]["firstquestion"] == 2:
                clans_list_after_first_question.append(clans_dictionary_with_answers[clans_list[i]]["name"])
    if first_question == "3":
        for i in range(len(clans_list)):
            if clans_dictionary_with_answers[clans_list[i]]["firstquestion"] == 3:
                clans_list_after_first_question.append(clans_dictionary_with_answers[clans_list[i]]["name"])
    if first_question == "4":
        for i in range(len(clans_list)):
            if clans_dictionary_with_answers[clans_list[i]]["firstquestion"] == 4:
                clans_list_after_first_question.append(clans_dictionary_with_answers[clans_list[i]]["name"])
    if second_question == "1":
        for i in range(len(clans_list_after_first_question)):
            if clans_dictionary_with_answers[clans_list_after_first_question[i]]["secondquestion"] == 1:
                clans_list_after_second_question.append(
                    clans_dictionary_with_answers[clans_list_after_first_question[i]]["name"])
    if second_question == "2":
        for i in range(len(clans_list_after_first_question)):
            if clans_dictionary_with_answers[clans_list_after_first_question[i]]["secondquestion"] == 2:
                clans_list_after_second_question.append(
                    clans_dictionary_with_answers[clans_list_after_first_question[i]]["name"])
    if third_question == "1":
        for i in range(len(clans_list_after_second_question)):
            if clans_dictionary_with_answers[clans_list_after_second_question[i]]["thirdquestion"] == 1:
                clans_list_after_third_question.append(
                    clans_dictionary_with_answers[clans_list_after_second_question[i]]["name"])
    if third_question == "2":
        for i in range(len(clans_list_after_second_question)):
            if clans_dictionary_with_answers[clans_list_after_second_question[i]]["thirdquestion"] == 2:
                clans_list_after_third_question.append(
                    clans_dictionary_with_answers[clans_list_after_second_question[i]]["name"])
    if fourth_question == "1":
        for i in range(len(clans_list_after_third_question)):
            if clans_dictionary_with_answers[clans_list_after_third_question[i]]["fourthquestion"] == 1:
                clans_list_after_fourth_question.append(
                    clans_dictionary_with_answers[clans_list_after_third_question[i]]["name"])
                character_clan_answers_logic_checker = 1
    if fourth_question == "2":
        for i in range(len(clans_list_after_third_question)):
            if clans_dictionary_with_answers[clans_list_after_third_question[i]]["fourthquestion"] == 2:
                clans_list_after_fourth_question.append(
                    clans_dictionary_with_answers[clans_list_after_third_question[i]]["name"])
                character_clan_answers_logic_checker = 1
    # when everything works fine that is final step which generate final class and send information to server
    if character_clan_answers_logic_checker == 1:
        # chose finall class
        final_first_clan = random.choice(clans_list_after_fourth_question)
        print("your class is: " + final_first_clan)
        # send class to the server
        send("first clan &" + final_first_clan)
        # take respond from server which provide full Player object for this client(username)
        server_respond = (client.recv(2048))
        smth = pickle.loads(server_respond)
        player_object_saver["player"] = smth
        print(smth)
        # save loaded player object values in dictionary for further use
        player_class_dictionary = (vars(smth))
        print(player_class_dictionary)
        print(player_class_dictionary["map"])
        # destroy the graphic window
        root.quit()
        root.destroy()
        # fill the player_class_dictionary_global with recived class object dictionary
        for key in player_class_dictionary:
            player_class_dictionary_global[key] = player_class_dictionary[key]
        print(player_class_dictionary_global)
        # open main game loop
        #main_game_loop()



# destroy graphics elements included in graphics_elemts list
def destroy_graphic_elements():
    for i in range(len(graphics_elements)):
        graphics_elements[i].destroy()
        i += 1


# open second question window in character creation
def second_question_window():
    question_menu_background_image = Image.open('assets/character_creation_background_question2.png')
    question_menu_background_image = question_menu_background_image.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
    resized_first_question_background_resized = ImageTk.PhotoImage(question_menu_background_image)
    background_first_question_label = tk.Label(root, image=resized_first_question_background_resized)
    background_first_question_label.place(x=0, y=0)
    first_asnwer_button = Button(root, text="thief", padx=40, pady=9,
                               command=lambda: get_1_answer_2_question_button_command(), bg="#439f9c")
    first_asnwer_button.pack()
    first_asnwer_button.place(x=550, y=150)
    secondAnswerButton = Button(root, text="dog trainer", padx=40, pady=9,
                                command=lambda: get_2_answer_2_question_button_command(), bg="#439f9c")
    secondAnswerButton.pack()
    secondAnswerButton.place(x=550, y=250)
    thirdAnswerButton = Button(root, text="medical assistant", padx=40, pady=9,
                               command=lambda: get_3_answer_2_question_button_command(), bg="#439f9c")
    thirdAnswerButton.pack()
    thirdAnswerButton.place(x=550, y=350)
    fourthAnswerButton = Button(root, text="herbal merchant", padx=40, pady=9,
                                command=lambda: get_4_answer_2_question_button_command(), bg="#439f9c")
    fourthAnswerButton.pack()
    fourthAnswerButton.place(x=550, y=450)
    graphics_elements.append(first_asnwer_button)
    graphics_elements.append(thirdAnswerButton)
    graphics_elements.append(secondAnswerButton)
    graphics_elements.append(fourthAnswerButton)
    graphics_elements.append(background_first_question_label)
    root.mainloop()


# open first question window in character creation
def first_question_window():
    question_menu_background_image = Image.open('assets/character_creation_background_question1.png')
    question_menu_background_image = question_menu_background_image.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
    resized_first_question_background_resized = ImageTk.PhotoImage(question_menu_background_image)
    backgroundFirstQuestionLabel = tk.Label(root, image=resized_first_question_background_resized)
    backgroundFirstQuestionLabel.place(x=0, y=0)
    firstAsnwerButton = Button(root, text="samurai", padx=40, pady=9,
                               command=lambda: get_1_answer_1_question_button_command(), bg="#439f9c")
    firstAsnwerButton.pack()
    firstAsnwerButton.place(x=550, y=150)
    secondAnswerButton = Button(root, text="assasyn", padx=40, pady=9,
                                command=lambda: get_2_answer_1_question_button_command(), bg="#439f9c")
    secondAnswerButton.pack()
    secondAnswerButton.place(x=550, y=250)
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
    graphics_elements.append(backgroundFirstQuestionLabel)
    root.mainloop()


# open third question window in character creation
def third_question_window():
    question_menu_background_image = Image.open('assets/character_creation_background_question3.png')
    question_menu_background_image = question_menu_background_image.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
    resized_first_question_background_resized = ImageTk.PhotoImage(question_menu_background_image)
    backgroundFirstQuestionLabel = tk.Label(root, image=resized_first_question_background_resized)
    backgroundFirstQuestionLabel.place(x=0, y=0)
    firstAsnwerButton = Button(root, text=" trained in sword fighting", padx=40, pady=9,
                               command=lambda: get_1_answer_3_question_button_command(), bg="#439f9c")
    firstAsnwerButton.pack()
    firstAsnwerButton.place(x=550, y=250)
    secondAnswerButton = Button(root, text="practiced martial arts", padx=40, pady=9,
                                command=lambda: get_2_answer_3_question_button_command(), bg="#439f9c")
    secondAnswerButton.pack()
    secondAnswerButton.place(x=550, y=350)
    thirdAnswerButton = Button(root, text="played with animals", padx=40, pady=9,
                               command=lambda: get_3_answer_3_question_button_command(), bg="#439f9c")
    thirdAnswerButton.pack()
    thirdAnswerButton.place(x=550, y=450)
    fourthAnswerButton = Button(root, text="set fire to houses in a neighboring village", padx=40, pady=9,
                                command=lambda: get_4_answer_3_question_button_command(), bg="#439f9c")
    fourthAnswerButton.pack()
    fourthAnswerButton.place(x=550, y=550)
    graphics_elements.append(firstAsnwerButton)
    graphics_elements.append(thirdAnswerButton)
    graphics_elements.append(secondAnswerButton)
    graphics_elements.append(fourthAnswerButton)
    graphics_elements.append(backgroundFirstQuestionLabel)
    root.mainloop()


# open fourth question window in character creation
def fourth_question_window():
    question_menu_background_image = Image.open('assets/character_creation_background_question4.png')
    question_menu_background_image = question_menu_background_image.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
    resized_first_question_background_resized = ImageTk.PhotoImage(question_menu_background_image)
    backgroundFirstQuestionLabel = tk.Label(root, image=resized_first_question_background_resized)
    backgroundFirstQuestionLabel.place(x=0, y=0)
    firstAsnwerButton = Button(root, text="A skilled warrior", padx=40, pady=9,
                               command=lambda: get_1_answer_4_question_button_command(), bg="#439f9c")
    firstAsnwerButton.pack()
    firstAsnwerButton.place(x=550, y=150)
    secondAnswerButton = Button(root, text="banished", padx=40, pady=9,
                                command=lambda: get_2_answer_4_question_button_command(), bg="#439f9c")
    secondAnswerButton.pack()
    secondAnswerButton.place(x=550, y=250)
    thirdAnswerButton = Button(root, text="traveler", padx=40, pady=9,
                               command=lambda: get_3_answer_4_question_button_command(), bg="#439f9c")
    thirdAnswerButton.pack()
    thirdAnswerButton.place(x=550, y=350)
    fourthAnswerButton = Button(root, text="monk", padx=40, pady=9,
                                command=lambda: get_4_answer_4_question_button_command(), bg="#439f9c")
    fourthAnswerButton.pack()
    fourthAnswerButton.place(x=550, y=450)
    graphics_elements.append(firstAsnwerButton)
    graphics_elements.append(thirdAnswerButton)
    graphics_elements.append(secondAnswerButton)
    graphics_elements.append(fourthAnswerButton)
    graphics_elements.append(backgroundFirstQuestionLabel)
    root.mainloop()


# button applaying value of 1 answer in first question
def get_1_answer_1_question_button_command():
    character_customization.append("1")
    destroy_graphic_elements()
    second_question_window()


# button applaying value of 2 answer in first question
def get_2_answer_1_question_button_command():
    character_customization.append("2")
    destroy_graphic_elements()
    second_question_window()


# button applaying value of 3 answer in first question
def get_3_answer_1_question_button_command():
    character_customization.append("3")
    destroy_graphic_elements()
    second_question_window()


# button applaying value of 4 answer in first question
def get_4_answer_1_question_button_command():
    character_customization.append("4")
    destroy_graphic_elements()
    second_question_window()


# button applaying value of 1 answer in second question
def get_1_answer_2_question_button_command():
    character_customization.append("1")
    destroy_graphic_elements()
    third_question_window()


# button applaying value of 2 answer in second question

def get_2_answer_2_question_button_command():
    character_customization.append("1")
    destroy_graphic_elements()
    third_question_window()


# button applaying value of 3 answer in second question

def get_3_answer_2_question_button_command():
    character_customization.append("2")
    destroy_graphic_elements()
    third_question_window()


# button applaying value of 4 answer in second question

def get_4_answer_2_question_button_command():
    character_customization.append("2")
    destroy_graphic_elements()
    third_question_window()


# button applaying value of 1 answer in third question

def get_1_answer_3_question_button_command():
    character_customization.append("1")
    destroy_graphic_elements()
    fourth_question_window()


# button applaying value of 2 answer in third question

def get_2_answer_3_question_button_command():
    character_customization.append("1")
    destroy_graphic_elements()
    fourth_question_window()


# button applaying value of 3 answer in third question

def get_3_answer_3_question_button_command():
    character_customization.append("2")
    destroy_graphic_elements()
    fourth_question_window()


# button applaying value of 4  answer in third question

def get_4_answer_3_question_button_command():
    character_customization.append("2")
    destroy_graphic_elements()
    fourth_question_window()


# button applaying value of 1 answer in fourth question

def get_1_answer_4_question_button_command():
    character_customization.append("1")
    character_clan_answers_logic(character_customization[0], character_customization[1], character_customization[2],
                                 character_customization[3])
    destroy_graphic_elements()


# button applaying value of 2 answer in fourth question

def get_2_answer_4_question_button_command():
    character_customization.append("1")
    character_clan_answers_logic(character_customization[0], character_customization[1], character_customization[2],
                                 character_customization[3])
    destroy_graphic_elements()


# button applaying value of 3 answer in fourth question

def get_3_answer_4_question_button_command():
    character_customization.append("2")
    character_clan_answers_logic(character_customization[0], character_customization[1], character_customization[2],
                                 character_customization[3])
    destroy_graphic_elements()


# button applaying value of 4 answer in fourth question

def get_4_answer_4_question_button_command():
    character_customization.append("2")
    character_clan_answers_logic(character_customization[0], character_customization[1], character_customization[2],
                                 character_customization[3])
    destroy_graphic_elements()


# Login Button command
def login_button_command(usernameTextBox=None, passwordTextBox=None):
    # get username and surename from login screen
    username = usernameTextBox.get("1.0", "end-1c")
    password = passwordTextBox.get("1.0", "end-1c")
    # send username and password to server if those parameters exist in db player will login otherwise server will make a new account and character
    send(username + "&username " + "`" + password)
    server_respond = (client.recv(2048).decode(FORMAT))
    print(server_respond)
    # login function
    if server_respond == "you can log in":
        destroy_graphic_elements()
        # server_respond = (client.recv(2048).decode(FORMAT))
        # print(server_respond)
        send("I can login")
        # take respond from server which provide full Player object for this client(username)
        server_first_pickle = (client.recv(2048))
        server_first_pickle_recived = pickle.loads(server_first_pickle)
        player_object_saver["player"] = server_first_pickle_recived
        fist_pickle_in_dict = vars(server_first_pickle_recived)
        root.quit()
        root.destroy()
        for key in fist_pickle_in_dict:
            player_class_dictionary_global[key] = fist_pickle_in_dict[key]


    # account creation function start
    if server_respond == "your account is ready":
        print('funkcja tworzenia postaci')
        destroy_graphic_elements()
        # first question of champion creation
        first_question_window()

# Game client
def login_window():
    main_menu_background_image = Image.open('assets/client_background.jpg')
    main_menu_background_image = main_menu_background_image.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
    resized1 = ImageTk.PhotoImage(main_menu_background_image)
    backgroundLabel = tk.Label(root, image=resized1)
    backgroundLabel.place(x=0, y=0)

    # Build buttons
    # username box setup
    usernameTextBox = Text(root, width=14, height=1)
    usernameTextBox.pack()
    usernameTextBox.place(x=1035, y=550)
    usernameTextBox.bind("<Tab>", focus_next_widget)
    usernameTextBox.bind("<Return>", focus_next_widget)

    # password box setup
    passwordTextBox = Text(root, width=14, height=1, )
    passwordTextBox.pack()
    passwordTextBox.bind("<Tab>", focus_next_widget)
    passwordTextBox.bind("<Return>", focus_next_widget)
    passwordTextBox.place(x=1035, y=570)
    # login button setup
    login_button = Button(root, text="login", padx=40, pady=9,
                      command=lambda: login_button_command(usernameTextBox, passwordTextBox), bg="#439f9c")
    login_button.pack()
    login_button.place(x=1150, y=550)
    # add elements to destroy list
    graphics_elements.append(login_button)
    graphics_elements.append(passwordTextBox)
    graphics_elements.append(usernameTextBox)
    graphics_elements.append(backgroundLabel)
    # login instruction textbox
    loginInstrucionText = tk.Label(root, padx=40, pady=20, wraplength=180, justify="left",
                                   text="Welcome in Samurai no jikan! \n if you do not have an account, the first login will automatically create an account")
    loginInstrucionText.pack()
    loginInstrucionText.place(x=1025, y=445)
    graphics_elements.append(loginInstrucionText)
    root.mainloop()


# start of program
login_window()
active_players = {}
transparent = (0,0,0,0)
# End of tkinter start of pygame

# camera customization
class Camera:
   def __init__(self, x, y):
       self.x = x
       self.y = y
cameraObject = Camera(0,0)


#camra blocakde
def clamp(value, minimum=0.0, maximum=1.0):
    return minimum if value < minimum else maximum if value > maximum else value


#camera movement
def slide_to(camera, destination, dt, speed_factor=0.5, anchor_point=None):
    if anchor_point is None:
        anchor_point = (0, 0)
    else:
        anchor_point = tuple(anchor_point)

    fac = clamp(speed_factor * dt)

    camera.x += (destination[0] - camera.x - anchor_point[0]) * fac
    camera.y += (destination[1] - camera.y - anchor_point[1]) * fac

# map object loader
def map_object_load(string_path_to_image,x_position,y_position,x_fix,y_fix,texture_hitbox_width,texture_hitbox_height):
    texture_name = pygame.image.load(string_path_to_image)
    win.blit(texture_name, (x_position - cameraObject.x, y_position - cameraObject.y))
    texture_hitbox = (x_position + x_fix - cameraObject.x, y_position + y_fix - cameraObject.y,texture_hitbox_width,texture_hitbox_height)
    pygame.draw.rect(win, (255, 0, 0), texture_hitbox, 2)

# make object for collision
def collision_maker(x_position,y_position,x_fix,y_fix,hitbox_width,htibox_height,dict_name,dict_key_string):
    texture_hitbox = (x_position + x_fix - cameraObject.x, y_position + y_fix - cameraObject.y,hitbox_width,htibox_height)
    collision_box = pygame.Rect(texture_hitbox)
    dict_name[dict_key_string] = collision_box

# update screen images
def redrawGameWindow():
    global walkCount
    #background draw
    win.blit(bg, (0 - cameraObject.x, 0-cameraObject.y))

    #server communication
    send(f"update &{player_class_dictionary_global['x_coordinate']} & {player_class_dictionary_global['y_coordinate']} & {player_class_dictionary_global['map']}")
    server_respond_for_redraw = (client.recv(2048))
    pickle_from_server_update = pickle.loads(server_respond_for_redraw)
    # activity on server checker

    # players update
    for key in pickle_from_server_update:
        active_players[key] = (pickle_from_server_update[key])
    # Drawing function
    def first_map_draw_function():
        map_object_load('assets/temple.png',230,0,0,0,600,360)
        for key in active_players:
            if active_players[key]['active'] == "active":
                if 'assets/pierwszamapa.png' in active_players[key]["map"]:
                    char = pygame.image.load(active_players[key]["asset"])
                    win.blit(char, (int(active_players[key]['x_coordinate']) - cameraObject.x,int(active_players[key]['y_coordinate']) - cameraObject.y))
        map_object_load("map_elements/drzwi.png",1420,1390,20,15,55,64)
        map_object_load("map_elements/drzwi.png",1470,1390,20,15,55,64)

        player_hitbox = (player_class_dictionary_global['x_coordinate'] + 17 - cameraObject.x, player_class_dictionary_global['y_coordinate'] + 11 - cameraObject.y, 29, 52)
        pygame.draw.rect(win, (255, 0, 0), player_hitbox, 2)
        goblin_text = pygame.image.load(f'{goblin.asset}')
        win.blit(goblin_text,(goblin.x-cameraObject.x,goblin.y-cameraObject.y))
        goblin.hitbox = (goblin.x - cameraObject.x + 17, goblin.y - cameraObject.y + 2, 31, 57)
        pygame.draw.rect(win, (255, 0, 0), goblin.hitbox, 2)
        Howa.collision_redbox_draw()
        Jiba.collision_redbox_draw()
    if "assets/pierwszamapa.png" in player_class_dictionary_global["map"]:
        first_map_draw_function()
    pygame.display.update()

#Collisions
def collision_first_map():
    goblin.hitbox = (goblin.x - cameraObject.x + 17, goblin.y - cameraObject.y + 2, 31, 57)
    goblin_test = pygame.Rect(goblin.hitbox)
    first_map_colision_dict["1"] = goblin_test
    collision_maker(230,0,0,0,600,360,first_map_colision_dict,"2")
    collision_maker(1420,1390,20,15,55,64,first_map_colision_dict,"portal1")
    collision_maker(1470,1390,20,15,55,64,first_map_colision_dict,"portal2")

#Attacks
class Attack():
    def __init__(self,width_and_hight_of_skill_area,name,dmg,texture):
        self.hitbox = width_and_hight_of_skill_area
        self.name = name
        self.dmg = dmg
        self.description = ""
        self.texture = texture
    # For enginge collisions
    def attack_collision_maker(name):
        x_fix = (name.hitbox / 4) - 35
        y_fix = (name.hitbox /4) - 40
        parameter = name.hitbox / 2
        attack_hitbox = ((int(player_class_dictionary_global["x_coordinate"])) - cameraObject.x - int(x_fix),
                         (int(player_class_dictionary_global["y_coordinate"]) - cameraObject.y - int(y_fix)), int(parameter),
                         int(parameter))
        pygame.draw.rect(win, (255, 0, 0), attack_hitbox, 2)
        attack_collision = pygame.Rect(attack_hitbox)
        if attack_collision.colliderect(first_map_colision_dict["1"]):
            print("hit")
    # Draw visual for checking
    def collision_redbox_draw(name):
        x_fix = (name.hitbox / 4) - 35
        y_fix = (name.hitbox /4) -40
        parameter = name.hitbox / 2
        attack_hitbox = ((int(player_class_dictionary_global["x_coordinate"])) - cameraObject.x - int(x_fix),
                         (int(player_class_dictionary_global["y_coordinate"]) - cameraObject.y - int(y_fix)),
                         int(parameter),
                         int(parameter))
        pygame.draw.rect(win, (255, 0, 0), attack_hitbox, 2)

# Attacks declarations
Jiba = Attack(400,"Jiba",1,"assets/jiba1.png")
Howa = Attack(200,"Howa",0,"assets/jiba.png")
attacks_list = [Jiba,Howa]

#Collisions dicts
first_map_colision_dict ={}
list_of_map_colisions = [first_map_colision_dict]

# pygame window basic setup
run_pygame = "1"
bg = pygame.image.load("assets/pierwszamapa.png")
clock = pygame.time.Clock()
left = False
right = False
attack_now = False
walkCount = 0

# velocity - speed of movement
vel = 5
pygame.init()
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Samurai no jikan")

# cd for attack timer
attack_cd= time.time()

# Variable for collision checker
last_used_move_key = ""

# main game loop
while run_pygame == "1":
    clock.tick(30)

    # collisions quick setup
    player_hitbox = (player_class_dictionary_global['x_coordinate'] + 17 - cameraObject.x, player_class_dictionary_global['y_coordinate'] + 11 - cameraObject.y, 29, 52)
    player_collision_rect = pygame.Rect(player_hitbox)
    if 'assets/pierwszamapa.png' in player_class_dictionary_global["map"]:
        collision_first_map()

    # Keys events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    # movement right left up down events

    if keys[pygame.K_LEFT]: #and int(player_class_dictionary_global["x_coordinate"]) -vel > 0:
        #update player position data
        last_used_move_key = "left"
        collision_count = 0
        for key in first_map_colision_dict:
            if player_collision_rect.colliderect(first_map_colision_dict[key]):
                collision_count += 1
                player_class_dictionary_global["x_coordinate"] += vel
        if collision_count == 0 and keys[pygame.K_RIGHT] == False:
            player_class_dictionary_global["x_coordinate"] -=  vel
    elif keys[pygame.K_RIGHT]:#and int(player_class_dictionary_global["x_coordinate"]) + vel < 2950:
        #update player position data
        last_used_move_key = "right"
        collision_count = 0
        for key in first_map_colision_dict:
            if player_collision_rect.colliderect(first_map_colision_dict[key]):
                collision_count += 1
                player_class_dictionary_global["x_coordinate"] -= vel
        if collision_count ==0 and keys[pygame.K_LEFT] == False:
            player_class_dictionary_global["x_coordinate"] += vel


    if keys[pygame.K_UP]: #and int(player_class_dictionary_global["y_coordinate"]) - vel > 0:
        #update player position data
        last_used_move_key = "up"
        collision_count = 0
        for key in first_map_colision_dict:
            if player_collision_rect.colliderect(first_map_colision_dict[key]):
                collision_count += 1
                player_class_dictionary_global["y_coordinate"] += 10
        if collision_count == 0 and keys[pygame.K_DOWN] == False:
            player_class_dictionary_global["y_coordinate"] -=  vel
    elif keys[pygame.K_DOWN]: #and int(player_class_dictionary_global["y_coordinate"]) + vel < 2935:
        #update player position data
        last_used_move_key = "down"
        collision_count = 0
        for key in first_map_colision_dict:
            if player_collision_rect.colliderect(first_map_colision_dict[key]):
                collision_count += 1
                player_class_dictionary_global["y_coordinate"] -= 10
        if collision_count == 0 and keys[pygame.K_UP] == False:
            player_class_dictionary_global["y_coordinate"] += vel

    # portal logic setup
    if player_collision_rect.colliderect(first_map_colision_dict["portal1"]) or player_collision_rect.colliderect(first_map_colision_dict["portal2"]):
        player_class_dictionary_global["map"] = "assets/bg.jpg"
        player_class_dictionary_global["x_coordinate"] = 5
        player_class_dictionary_global["y_coordinate"] = 5
        bg = pygame.image.load("assets/bg.jpg")

    #collision fixer
    collision_count = 0
    for key in first_map_colision_dict:
        if player_collision_rect.colliderect(first_map_colision_dict[key]):
            collision_count += 1
    if last_used_move_key == "up" and collision_count >0:
            player_class_dictionary_global["y_coordinate"] += 10
    if last_used_move_key == "down" and collision_count >0:
            player_class_dictionary_global["y_coordinate"] -= 10
    if last_used_move_key == "left" and collision_count >0:
            player_class_dictionary_global["x_coordinate"] += 10
    if last_used_move_key == "right" and collision_count >0:
            player_class_dictionary_global["x_coordinate"] -= 10

    #attack_collision_maker(Jiba)
    Jiba.attack_collision_maker()

    # X and Y checker
    if keys[pygame.K_SPACE]:
        #test of cooldowns
        if time.time() - attack_cd > 3:  # if its been 1 second
            attack_now = True
            attack_cd = time.time()
            print(player_class_dictionary_global["x_coordinate"])
            print(player_class_dictionary_global["y_coordinate"])


    #refreshing the camera view
    slide_to(cameraObject,(int(player_class_dictionary_global["x_coordinate"]), int(player_class_dictionary_global["y_coordinate"])), 1/(clock.get_fps() + 1e-07), 7, (WIDTH/2, HEIGHT/2))

    # camera lock to prevent the camera from going off the map
    cameraObject.x = clamp(cameraObject.x, 0, 1720)
    cameraObject.y = clamp(cameraObject.y, 0, 780)

    # window graphic update
    redrawGameWindow()

send(DISCONNECT_MESSAGE)
pygame.quit()