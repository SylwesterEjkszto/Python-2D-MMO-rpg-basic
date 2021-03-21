import socket
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import ctypes
import random
import pickle
from Player import *

# permanent
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.137.1"
ADDR = (SERVER, PORT)
username = ""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
graphics_elements = []
character_customization = []
# main window setup
WIDTH = ctypes.windll.user32.GetSystemMetrics(0)
HEIGHT = ctypes.windll.user32.GetSystemMetrics(1)
root = tk.Tk()
root.state("zoomed")
root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('Samurai no jikan')
clans_dictionary_with_answers = {"Raitoningu": {"firstquestion": 1,
                                                "name":"Raitoningu",
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

clans_list = ['Raitoningu',"Same","Chimamire no kiri","Mizunoken","Tekondō","Jakkaru","Kin'iro no me","Doku","Shibō","Chikaku-teki","Atsuryoku-ten","Inu no tomodachi","Wāmu","Hakushoku hikari","Hen'i-tai","Shinkō","Ningyō","Kusuri","Shadouasashin","Kōri","Ketsueki","Shinrin","Hagane","Maguneshiumu","Kopī","Kage no senshi","Mippei suru","Maindo","Arashi","Taimatsu","Shizen","Kemuri","Hikari","Kumo"]
clans_list_after_first_question = []
clans_list_after_second_question = []
clans_list_after_third_question = []
clans_list_after_fourth_question = []

# tab for change textfield
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return ("break")


# comunication with server
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    #server_respond = (client.recv(2048).decode(FORMAT))
    #print(server_respond)
# character answers based generator
def character_clan_answers_logic(first_question_answer,second_question_answer,third_question_answer,fourth_question_answer):
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
                clans_list_after_second_question.append(clans_dictionary_with_answers[clans_list_after_first_question[i]]["name"])
    if second_question == "2":
        for i in range(len(clans_list_after_first_question)):
            if clans_dictionary_with_answers[clans_list_after_first_question[i]]["secondquestion"] == 2:
                clans_list_after_second_question.append(clans_dictionary_with_answers[clans_list_after_first_question[i]]["name"])
    if third_question == "1":
        for i in range(len(clans_list_after_second_question)):
            if clans_dictionary_with_answers[clans_list_after_second_question[i]]["thirdquestion"] == 1:
                clans_list_after_third_question.append(clans_dictionary_with_answers[clans_list_after_second_question[i]]["name"])
    if third_question == "2":
        for i in range(len(clans_list_after_second_question)):
            if clans_dictionary_with_answers[clans_list_after_second_question[i]]["thirdquestion"] == 2:
                clans_list_after_third_question.append(clans_dictionary_with_answers[clans_list_after_second_question[i]]["name"])
    if fourth_question == "1":
        for i in range(len(clans_list_after_third_question)):
            if clans_dictionary_with_answers[clans_list_after_third_question[i]]["fourthquestion"] == 1:
                clans_list_after_fourth_question.append(clans_dictionary_with_answers[clans_list_after_third_question[i]]["name"])
                character_clan_answers_logic_checker=1
    if fourth_question == "2":
        for i in range(len(clans_list_after_third_question)):
            if clans_dictionary_with_answers[clans_list_after_third_question[i]]["fourthquestion"] == 2:
                clans_list_after_fourth_question.append(clans_dictionary_with_answers[clans_list_after_third_question[i]]["name"])
                character_clan_answers_logic_checker =1

    if character_clan_answers_logic_checker == 1:
        final_first_clan = random.choice(clans_list_after_fourth_question)
        print("your class is: " + final_first_clan)
        send("first clan &" + final_first_clan)
        server_respond = (client.recv(2048))
        smth = pickle.loads(server_respond)
        print(smth)
        somedictionary = (vars(smth))
        print(somedictionary["name"])
# buttons commands
def destroy_graphic_elements():
    for i in range(len(graphics_elements)):
        graphics_elements[i].destroy()
        i += 1

def second_question_window():
    question_menu_background_image = Image.open('assets/character_creation_background_question2.png')
    question_menu_background_image = question_menu_background_image.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
    resized_first_question_background_resized = ImageTk.PhotoImage(question_menu_background_image)
    backgroundFirstQuestionLabel = tk.Label(root, image=resized_first_question_background_resized)
    backgroundFirstQuestionLabel.place(x=0, y=0)
    firstAsnwerButton = Button(root, text="thief", padx=40, pady=9,
                               command=lambda: get_1_answer_2_question_button_command(), bg="#439f9c")
    firstAsnwerButton.pack()
    firstAsnwerButton.place(x=550, y=150)
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
    graphics_elements.append(firstAsnwerButton)
    graphics_elements.append(thirdAnswerButton)
    graphics_elements.append(secondAnswerButton)
    graphics_elements.append(fourthAnswerButton)
    graphics_elements.append(backgroundFirstQuestionLabel)
    root.mainloop()

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
def get_1_answer_1_question_button_command():
    character_customization.append("1")
    destroy_graphic_elements()
    second_question_window()


def get_2_answer_1_question_button_command():
    character_customization.append("2")
    destroy_graphic_elements()
    second_question_window()

def get_3_answer_1_question_button_command():
    character_customization.append("3")
    destroy_graphic_elements()
    second_question_window()

def get_4_answer_1_question_button_command():
    character_customization.append("4")
    destroy_graphic_elements()
    second_question_window()

def get_1_answer_2_question_button_command():
    character_customization.append("1")
    destroy_graphic_elements()
    third_question_window()


def get_2_answer_2_question_button_command():
    character_customization.append("1")
    destroy_graphic_elements()
    third_question_window()

def get_3_answer_2_question_button_command():
    character_customization.append("2")
    destroy_graphic_elements()
    third_question_window()

def get_4_answer_2_question_button_command():
    character_customization.append("2")
    destroy_graphic_elements()
    third_question_window()

def get_1_answer_3_question_button_command():
    character_customization.append("1")
    destroy_graphic_elements()
    fourth_question_window()


def get_2_answer_3_question_button_command():
    character_customization.append("1")
    destroy_graphic_elements()
    fourth_question_window()

def get_3_answer_3_question_button_command():
    character_customization.append("2")
    destroy_graphic_elements()
    fourth_question_window()

def get_4_answer_3_question_button_command():
    character_customization.append("2")
    destroy_graphic_elements()
    fourth_question_window()

def get_1_answer_4_question_button_command():
    character_customization.append("1")
    character_clan_answers_logic(character_customization[0],character_customization[1],character_customization[2],character_customization[3])
    destroy_graphic_elements()


def get_2_answer_4_question_button_command():
    character_customization.append("1")
    character_clan_answers_logic(character_customization[0],character_customization[1],character_customization[2],character_customization[3])
    destroy_graphic_elements()

def get_3_answer_4_question_button_command():
    character_customization.append("2")
    character_clan_answers_logic(character_customization[0],character_customization[1],character_customization[2],character_customization[3])
    destroy_graphic_elements()

def get_4_answer_4_question_button_command():
    character_customization.append("2")
    character_clan_answers_logic(character_customization[0],character_customization[1],character_customization[2],character_customization[3])
    destroy_graphic_elements()
# send(DISCONNECT_MESSAGE)
# Login Button command
def login_button_command(usernameTextBox=None, passwordTextBox=None):
    username = usernameTextBox.get("1.0", "end-1c")
    password = passwordTextBox.get("1.0", "end-1c")
    send(username + "&username " + "`" + password)
    server_respond = (client.recv(2048).decode(FORMAT))
    print(server_respond)
    if server_respond == "you can log in":
        print('funkcja logowania')
        # server_respond = (client.recv(2048).decode(FORMAT))
        # print(server_respond)
    if server_respond == "your account is ready":
        print('funkcja tworzenia postaci')
        destroy_graphic_elements()
        # server_respond = (client.recv(2048).decode(FORMAT))
        # print(server_respond)

        # first question window
        first_question_window()




# Game client
def login_window():
    main_menu_background_image = Image.open('assets/client_background.jpg')
    main_menu_background_image = main_menu_background_image.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
    resized1 = ImageTk.PhotoImage(main_menu_background_image)
    backgroundLabel = tk.Label(root, image=resized1)
    backgroundLabel.place(x=0, y=0)

    # Build buttons
    usernameTextBox = Text(root, width=14, height=1)
    usernameTextBox.pack()
    usernameTextBox.place(x=1035, y=550)
    usernameTextBox.bind("<Tab>", focus_next_widget)
    passwordTextBox = Text(root, width=14, height=1, )
    passwordTextBox.pack()
    passwordTextBox.bind("<Tab>", focus_next_widget)
    passwordTextBox.place(x=1035, y=570)
    myButton = Button(root, text="login", padx=40, pady=9,
                      command=lambda: login_button_command(usernameTextBox, passwordTextBox), bg="#439f9c")
    myButton.pack()
    myButton.place(x=1150, y=550)
    graphics_elements.append(myButton)
    graphics_elements.append(passwordTextBox)
    graphics_elements.append(usernameTextBox)
    graphics_elements.append(backgroundLabel)
    loginInstrucionText = tk.Label(root, padx=40, pady=20, wraplength=180, justify="left",
                                   text="Welcome in Samurai no jikan! \n if you do not have an account, the first login will automatically create an account")
    loginInstrucionText.pack()
    loginInstrucionText.place(x=1025, y=445)
    graphics_elements.append(loginInstrucionText)
    root.mainloop()


login_window()
