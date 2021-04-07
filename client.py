import socket
import tkinter as tk
from PIL import ImageTk
import random
import pickle
from Player import *
import pygame
from Attack import *
import time
import ast
list_of_enemies = []
dict_of_enemies = {}

class Enemy():
    def __init__(self,name, map_img,map_number, x, y, x_fix, y_fix, width, height, hp, xp,dmg):
        self.name = name
        self.respawn_timer = time.time()
        self.attack_cd = time.time()
        self.attack = True
        self.attack_range_tuple = (0,0,0,0)
        self.attack_range = 0
        self.dmg = dmg
        self.map = map_img
        self.map_number = map_number
        self.hp = hp
        self.max_hp = hp
        self.xp = xp
        self.asset = "assets/L1E.png"
        self.speed = 3
        self.spawn_x = x
        self.spawn_y = y
        self.previous_x = 0
        self.previous_y = 0
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_fix = x_fix
        self.y_fix = y_fix
        self.hitbox = (0, 0, 0, 0)
        self.collision = 0
        self.collisions_append()
        self.live = True
        self.view_rect = (0,0,0,0)
        self.view = 0
        self.following = False
        self.player_to_follow = "0"
        self.respawn = 0
    def hitbox_update(self):
        self.collision = pygame.Rect(self.hitbox)
        self.hitbox = (
            self.x - cameraObject.x + self.x_fix, self.y - cameraObject.y + self.y_fix, self.width, self.height)
        self.view_rect = (self.x - cameraObject.x - 150 , self.y - cameraObject.y - 155, 350, 350)
        self.view = pygame.Rect(self.view_rect)
        self.attack_range_tuple = (self.x - cameraObject.x -40 , self.y - cameraObject.y -40 , 150, 150)
        self.attack_range = pygame.Rect(self.attack_range_tuple)

    #draw view range and attack range into the screen as green and blue square
    def view_attack_box(self):
        pygame.draw.rect(win, (0, 255, 0), self.view_rect, 2)
        pygame.draw.rect(win, (0,0,255), self.attack_range_tuple, 2)

    # change live parameter and set respawn time to start measuring time
    def live_update(self):
        self.live = not self.live
        self.respawn_timer = time.time()

    #change attack atribute to false and set coldoown timer
    def attack_update_false(self):
        self.attack = False
        self.attack_cd = time.time()

    # check respawn timer, while true respawn enemy with full hp in spawn position
    def respawn_check(self):
        if time.time() - self.respawn_timer >5 and self.live == False:
            self.live = True
            self.previous_x = self.x
            self.previous_y = self.y
            self.x = self.spawn_x
            self.y = self.spawn_y
            self.hp = self.max_hp
            self.following = False
            self.respawn = 1

    # do this when object get hit, update live,hp and player xp
    def hit(self,attack):
        if self.live == True:
            print('ojojojoj')
            self.hp -= attack.dmg
            print(self.hp)
            if self.hp < 1:
                player_object_saver['player'].xp = player_object_saver['player'].xp + self.xp
                self.live_update()
                self.following = False
                self.player_to_follow = "0"
                self.respawn = 0
    # add enemies to list
    def collisions_append(self):
        list_of_enemies.append(self)
    # following the player method and also attack method
    def move(self):
        if self.player_to_follow =="0":
            for key in active_players:
                if active_players[key]["collision_rect"].colliderect(self.view):
                    self.following = True
                    self.player_to_follow = active_players[key]["name"]
                    break
        #print(self.player_to_follow)
        if self.attack == True and player_object_saver["player"].collision_rect.colliderect(self.attack_range) and self.live:
            player_object_saver["player"].hp -= self.dmg
            self.attack_update_false()
        if self.attack == False:
            if time.time() - self.attack_cd > 1.5:
                self.attack = True
        if self.player_to_follow != "0":
            if self.live and self.following == True:
                if self.x-50 > active_players[self.player_to_follow]["x"]:
                    self.previous_x = self.x
                    self.x -= self.speed
                elif self.x + 50 < active_players[self.player_to_follow]["x"]:
                    self.previous_x = self.x
                    self.x += self.speed
                if self.y +50 < active_players[self.player_to_follow]["y"]:
                    self.previous_y = self.y
                    self.y += self.speed
                elif self.y - 50 >  active_players[self.player_to_follow]["y"]:
                    self.previous_y = self.y
                    self.y -= self.speed
list_of_npc = []
class Npc():
    def __init__(self,name,asset,map,x,x_fix,y,y_fix,width,height,tekst):
        self.name = name
        self.asset= asset
        self.map = map
        self.x  = x
        self.x_fix = x_fix
        self.y = y
        self.y_fix = y_fix
        self.width = width
        self.height = height
        self.tekst = tekst
        self.dialogue_visibility = False
        self.live = True
        self.append_list_of_npc()
        self.hitbox = 0
        self.collision = 0

    def dialogue_visibility_update(self):
        self.dialogue_visibility = not self.dialogue_visibility

    def append_list_of_npc(self):
        list_of_npc.append(self)

    def collision_maker(self):
        self.hitbox = (self.x - cameraObject.x + self.x_fix, self.y - cameraObject.y + self.y_fix, self.width, self.height)
        self.collision = pygame.Rect(self.hitbox)

# permament network variables
HEADER = 2048
PORT = 5050
FORMAT = 'utf-8'
# usage in send() function will disconnect from serwer
DISCONNECT_MESSAGE = "!DISCONNECT"
# server ip adress
SERVER ="192.168.137.1"
ADDR = (SERVER, PORT)
# player(account) username for further use
username = ""
# network setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
# list of elements to destroy
graphics_elements = []
# List for character creation use
character_customization = []
# dict for sending pickles with class object parameters
player_class_dictionary_global = {}
#Enemies declaration
goblin = Enemy("goblin",'assets/testmap.png',1, 1235, 580, 17, 2, 31, 57, 1, 500,5)
goblin1 = Enemy("goblin1",'assets/testmap.png',1, 1435, 580, 17, 2, 31, 57, 1, 500,5)

#npc declaration
Hikori = Npc("Hikroi",'npc_png/first_npc.png',1,515,17,450,11,29,52,"hori")

# main window setup
WIDTH = 1280
HEIGHT = 720
root = tk.Tk()
root.state("zoomed")
root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('Samurai no jikan')
# Storage for first server communication
player_object_saver = {}
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
def focus_next_widget(tkinter_event):
    tkinter_event.widget.tk_focusNext().focus()
    return "break"


# comunication with server sending message and comented line is for taking responds
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


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
        for acctual_i in range(len(clans_list)):
            if clans_dictionary_with_answers[clans_list[acctual_i]]["firstquestion"] == 1:
                clans_list_after_first_question.append(clans_dictionary_with_answers[clans_list[acctual_i]]["name"])
    if first_question == "2":
        for acctual_i in range(len(clans_list)):
            if clans_dictionary_with_answers[clans_list[acctual_i]]["firstquestion"] == 2:
                clans_list_after_first_question.append(clans_dictionary_with_answers[clans_list[acctual_i]]["name"])
    if first_question == "3":
        for acctual_i in range(len(clans_list)):
            if clans_dictionary_with_answers[clans_list[acctual_i]]["firstquestion"] == 3:
                clans_list_after_first_question.append(clans_dictionary_with_answers[clans_list[acctual_i]]["name"])
    if first_question == "4":
        for acctual_i in range(len(clans_list)):
            if clans_dictionary_with_answers[clans_list[acctual_i]]["firstquestion"] == 4:
                clans_list_after_first_question.append(clans_dictionary_with_answers[clans_list[acctual_i]]["name"])
    if second_question == "1":
        for acctual_i in range(len(clans_list_after_first_question)):
            if clans_dictionary_with_answers[clans_list_after_first_question[acctual_i]]["secondquestion"] == 1:
                clans_list_after_second_question.append(
                    clans_dictionary_with_answers[clans_list_after_first_question[acctual_i]]["name"])
    if second_question == "2":
        for acctual_i in range(len(clans_list_after_first_question)):
            if clans_dictionary_with_answers[clans_list_after_first_question[acctual_i]]["secondquestion"] == 2:
                clans_list_after_second_question.append(
                    clans_dictionary_with_answers[clans_list_after_first_question[acctual_i]]["name"])
    if third_question == "1":
        for acctual_i in range(len(clans_list_after_second_question)):
            if clans_dictionary_with_answers[clans_list_after_second_question[acctual_i]]["thirdquestion"] == 1:
                clans_list_after_third_question.append(
                    clans_dictionary_with_answers[clans_list_after_second_question[acctual_i]]["name"])
    if third_question == "2":
        for acctual_i in range(len(clans_list_after_second_question)):
            if clans_dictionary_with_answers[clans_list_after_second_question[acctual_i]]["thirdquestion"] == 2:
                clans_list_after_third_question.append(
                    clans_dictionary_with_answers[clans_list_after_second_question[acctual_i]]["name"])
    if fourth_question == "1":
        for acctual_i in range(len(clans_list_after_third_question)):
            if clans_dictionary_with_answers[clans_list_after_third_question[acctual_i]]["fourthquestion"] == 1:
                clans_list_after_fourth_question.append(
                    clans_dictionary_with_answers[clans_list_after_third_question[acctual_i]]["name"])
                character_clan_answers_logic_checker = 1
    if fourth_question == "2":
        for acctual_i in range(len(clans_list_after_third_question)):
            if clans_dictionary_with_answers[clans_list_after_third_question[acctual_i]]["fourthquestion"] == 2:
                clans_list_after_fourth_question.append(
                    clans_dictionary_with_answers[clans_list_after_third_question[acctual_i]]["name"])
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
        # main_game_loop()


# destroy graphics elements included in graphics_elemts list
def destroy_graphic_elements():
    for graphic_element in range(len(graphics_elements)):
        graphics_elements[graphic_element].destroy()
        graphic_element += 1


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
    second_answer_button = Button(root, text="dog trainer", padx=40, pady=9,
                                  command=lambda: get_2_answer_2_question_button_command(), bg="#439f9c")
    second_answer_button.pack()
    second_answer_button.place(x=550, y=250)
    third_answer_button = Button(root, text="medical assistant", padx=40, pady=9,
                                 command=lambda: get_3_answer_2_question_button_command(), bg="#439f9c")
    third_answer_button.pack()
    third_answer_button.place(x=550, y=350)
    fourth_answer_button = Button(root, text="herbal merchant", padx=40, pady=9,
                                  command=lambda: get_4_answer_2_question_button_command(), bg="#439f9c")
    fourth_answer_button.pack()
    fourth_answer_button.place(x=550, y=450)
    graphics_elements.append(first_asnwer_button)
    graphics_elements.append(third_answer_button)
    graphics_elements.append(second_answer_button)
    graphics_elements.append(fourth_answer_button)
    graphics_elements.append(background_first_question_label)
    root.mainloop()


# open first question window in character creation
def first_question_window():
    question_menu_background_image = Image.open('assets/character_creation_background_question1.png')
    question_menu_background_image = question_menu_background_image.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
    resized_first_question_background_resized = ImageTk.PhotoImage(question_menu_background_image)
    background_first_question_label = tk.Label(root, image=resized_first_question_background_resized)
    background_first_question_label.place(x=0, y=0)
    first_asnwer_button = Button(root, text="samurai", padx=40, pady=9,
                                 command=lambda: get_1_answer_1_question_button_command(), bg="#439f9c")
    first_asnwer_button.pack()
    first_asnwer_button.place(x=550, y=150)
    second_answer_button = Button(root, text="assasyn", padx=40, pady=9,
                                  command=lambda: get_2_answer_1_question_button_command(), bg="#439f9c")
    second_answer_button.pack()
    second_answer_button.place(x=550, y=250)
    third_answer_button = Button(root, text="monk", padx=40, pady=9,
                                 command=lambda: get_3_answer_1_question_button_command(), bg="#439f9c")
    third_answer_button.pack()
    third_answer_button.place(x=550, y=350)
    fourth_answer_button = Button(root, text="fisherman", padx=40, pady=9,
                                  command=lambda: get_4_answer_1_question_button_command(), bg="#439f9c")
    fourth_answer_button.pack()
    fourth_answer_button.place(x=550, y=450)
    graphics_elements.append(first_asnwer_button)
    graphics_elements.append(third_answer_button)
    graphics_elements.append(second_answer_button)
    graphics_elements.append(fourth_answer_button)
    graphics_elements.append(background_first_question_label)
    root.mainloop()


# open third question window in character creation
def third_question_window():
    question_menu_background_image = Image.open('assets/character_creation_background_question3.png')
    question_menu_background_image = question_menu_background_image.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
    resized_first_question_background_resized = ImageTk.PhotoImage(question_menu_background_image)
    background_first_question_label = tk.Label(root, image=resized_first_question_background_resized)
    background_first_question_label.place(x=0, y=0)
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
    graphics_elements.append(background_first_question_label)
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
    # send username and password to server if those parameters exist in db player will login otherwise server will
    # make a new account and character
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
        #print(server_first_pickle)
        # active players recived from server and transfomred into dictionary
        server_second_pickle = (client.recv(2048))
        server_second_pickle_recived = pickle.loads(server_second_pickle)
        #print(server_second_pickle_recived)

        # Enemies update
        for i in range(len(list_of_enemies)):
            name_of_enemy = list_of_enemies[i].name
            #print(list_of_enemies[i].x)
            list_of_enemies[i].x = server_second_pickle_recived[name_of_enemy]["x"]
            list_of_enemies[i].y = server_second_pickle_recived[name_of_enemy]["y"]
        ###
        #server_first_pickle_recived = pickle.loads(server_first_pickle)
        #player_object_saver["player"] = server_first_pickle_recived
        #fist_pickle_in_dict = vars(server_first_pickle_recived)
        root.quit()
        root.destroy()


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
                                   text="Welcome in Samurai no jikan! \n if you do not have an account, the first "
                                        "login will automatically create an account")
    loginInstrucionText.pack()
    loginInstrucionText.place(x=1025, y=445)
    graphics_elements.append(loginInstrucionText)
    root.mainloop()


# start of program
login_window()

# End of tkinter login client start of pygame


# dict for update players connected with server
active_players = {}


# camera customization
class Camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# declaration of camera object
cameraObject = Camera(0, 0)


# camra blocakde
def clamp(value, minimum=0.0, maximum=1.0):
    return minimum if value < minimum else maximum if value > maximum else value


# camera movement
def slide_to(camera, destination, dt, speed_factor=0.5, anchor_point=None):
    if anchor_point is None:
        anchor_point = (0, 0)
    else:
        anchor_point = tuple(anchor_point)

    fac = clamp(speed_factor * dt)

    camera.x += (destination[0] - camera.x - anchor_point[0]) * fac
    camera.y += (destination[1] - camera.y - anchor_point[1]) * fac


# map object loader
def map_object_load(string_path_to_image, x_position, y_position, x_fix, y_fix, texture_hitbox_width,
                    texture_hitbox_height):
    texture_name = pygame.image.load(string_path_to_image)
    win.blit(texture_name, (x_position - cameraObject.x, y_position - cameraObject.y))
    texture_hitbox = (x_position + x_fix - cameraObject.x, y_position + y_fix - cameraObject.y, texture_hitbox_width,
                      texture_hitbox_height)
    pygame.draw.rect(win, (255, 0, 0), texture_hitbox, 2)


# draw enemies
def map_enemy_load(object):
    texture_name = pygame.image.load(object.asset)
    if object.live == False:
        texture_name = pygame.transform.rotate(texture_name, 90)
    win.blit(texture_name, (object.x - cameraObject.x, object.y - cameraObject.y))
    texture_hitbox = (object.x + object.x_fix - cameraObject.x, object.y + object.y_fix - cameraObject.y, object.width,
                      object.height)
    pygame.draw.rect(win, (255, 0, 0), texture_hitbox, 2)
    #if object.live == False:
        #rotated_image = pygame.transform.rotate(texture_name, 90)
        #new_rect = rotated_image.get_rect(center=texture_name.get_rect().center)
        #win.blit(rotated_image,(object.x - cameraObject.x, object.y - cameraObject.y ))


# make object for collision
def collision_maker(x_position, y_position, x_fix, y_fix, hitbox_width, htibox_height, dict_name, dict_key_string):
    texture_hitbox = (
        x_position + x_fix - cameraObject.x, y_position + y_fix - cameraObject.y, hitbox_width, htibox_height)
    collision_box = pygame.Rect(texture_hitbox)
    dict_name[dict_key_string] = collision_box

def blitRotateCenter(surf, image, topleft,):

    rotated_image = pygame.transform.rotate(image, 90)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)
# update screen images
def redraw_game_window():
    # background draw
    win.blit(bg, (0 - cameraObject.x, 0 - cameraObject.y))
    def user_interface():
        skills_icon = pygame.image.load("icons/skills.png")
        skills_menu.draw(win)
        win.blit(skills_icon, (1146, 670))
        #skills icon border
        pygame.draw.rect(win, (255, 0, 0), (1146, 670, 40, 40), 2)
        hp_bar_text = font.render('HP: ' + str(player_object_saver["player"].hp)  + "/" + str(player_object_saver['player'].max_hp),True,(0,0,0))
        pygame.draw.rect(win, (255, 0, 0), (0,0,200,25))
        acctual_hp_math = 200 / int(player_object_saver['player'].max_hp)
        pygame.draw.rect(win, (0, 255, 0), (0, 0,( int(player_object_saver['player'].hp * acctual_hp_math)), 25))
        win.blit(hp_bar_text, (70,5))
        energy_bar_text = font.render(
            'EP: ' + str(player_object_saver["player"].energy) + "/" + str(player_object_saver['player'].max_energy), True,
            (0, 0, 0))
        pygame.draw.rect(win, (0, 0, 0), (0, 25, 200, 25))
        acctual_energy_math = 200 / int(player_object_saver['player'].max_energy)
        pygame.draw.rect(win, (0, 0, 255), (0, 25, (int(player_object_saver['player'].energy * acctual_energy_math)), 25))
        win.blit(energy_bar_text, (70, 30))
        lvl_text = font.render("lvl: " + str(player_object_saver["player"].lvl), True,(0,0,0))
        pygame.draw.rect(win,(255,215,0),(0,50,200,25))
        win.blit(lvl_text,(70,55))
        xp_text = font.render("xp: " + str(player_object_saver["player"].xp) + '/' + str(player_object_saver['player'].next_lvl),True,(255,255,255))
        pygame.draw.rect(win, (0, 0, 0), (0, 75, 200, 25))
        acctual_xp_math = 200 / int(player_object_saver['player'].next_lvl)
        pygame.draw.rect(win, (218,165,32),
                         (0, 75, (int(player_object_saver['player'].xp * acctual_xp_math)), 25))
        win.blit(xp_text, (70, 80))
        skill_quick_use.draw(win)
        first = quick_use_font.render(("1"), True,(0,0,0))
        win.blit(first,(460,695))
        first = quick_use_font.render(("2"), True, (0, 0, 0))
        win.blit(first, (505, 695))
        first = quick_use_font.render(("3"), True, (0, 0, 0))
        win.blit(first, (550, 695))
        first = quick_use_font.render(("4"), True, (0, 0, 0))
        win.blit(first, (595, 695))
        first = quick_use_font.render(("5"), True, (0, 0, 0))
        win.blit(first, (635, 695))
        first = quick_use_font.render(("6"), True, (0, 0, 0))
        win.blit(first, (675, 695))
        first = quick_use_font.render(("7"), True, (0, 0, 0))
        win.blit(first, (720, 695))
        first = quick_use_font.render(("8"), True, (0, 0, 0))
        win.blit(first, (760, 695))
        first = quick_use_font.render(("9"), True, (0, 0, 0))
        win.blit(first, (800, 695))


    # server communication
    #append directory of enemies with thins i need to send to all users
    for i in range(len(list_of_enemies)):
        dict_of_enemies[list_of_enemies[i].name] = {"x":list_of_enemies[i].x,"y":list_of_enemies[i].y,"hp":list_of_enemies[i].hp,"player_to_follow":list_of_enemies[i].player_to_follow, "max_hp":list_of_enemies[i].max_hp,"respawn":list_of_enemies[i].respawn,"previous_x":list_of_enemies[i].previous_x,"previous_y":list_of_enemies[i].previous_y}
    #print(dict_of_enemies)
    send(
        f"update &{player_object_saver['player'].x} & {player_object_saver['player'].y} & {player_object_saver['player'].map}  & {int(player_object_saver['player'].walk_count)}  & {player_object_saver['player'].last_used_movement_direction} & {player_object_saver['player'].lvl} & {player_object_saver['player'].xp} & {player_object_saver['player'].next_lvl} & {dict_of_enemies}  & {player_object_saver['player'].hitbox}")
    for i in range(len(list_of_enemies)):
        list_of_enemies[i].respawn = 0
    server_respond_for_redraw = (client.recv(8192))
    # split the mesege for usefull directiores
    server_respond_for_redraw_split = server_respond_for_redraw.decode(FORMAT).split('&')
    # active players recived from server and transfomred into dictionary
    res = ast.literal_eval(server_respond_for_redraw_split[0])
    # enemies recived from server striped for delete whitespaces and transformed into dictionary
    res_enemy = ast.literal_eval(server_respond_for_redraw_split[2].strip())
    #print(res_enemy)
    # players update
    for key in res:
        active_players[key] = res[key]
        active_players[key]["collision_rect"] = pygame.Rect(active_players[key]["hitbox"])
    for i in range(len(list_of_enemies)):
        name_of_enemy = list_of_enemies[i].name
        list_of_enemies[i].x = res_enemy[name_of_enemy]["x"]
        list_of_enemies[i].y = res_enemy[name_of_enemy]["y"]
        list_of_enemies[i].player_to_follow = res_enemy[name_of_enemy]["player_to_follow"]
        list_of_enemies[i].hp = res_enemy[name_of_enemy]["hp"]
        list_of_enemies[i].live = res_enemy[name_of_enemy]["live"]






    # Drawing function
    def first_map_draw_function():
        map_object_load('assets/temple.png', 230, 0, 0, 0, 600, 360)
        for key in active_players:
            if active_players[key]['active'] == "active":
                if 1 == active_players[key]["map"]:
                    pygame.draw.rect(win,(255,0,0),(int(active_players[key]["x"]) + 5 - cameraObject.x, int(active_players[key]['y']) - cameraObject.y,int(active_players[key]['max_hp']),8),0,5)
                    pygame.draw.rect(win,(0,255,0),(int(active_players[key]["x"]) + 5- cameraObject.x, int(active_players[key]['y'])  - cameraObject.y,int(active_players[key]['hp']),8),0,5)
                    character_name = font.render(str(active_players[key]["name"]),True,(0,0,0))
                    win.blit(character_name,(int(active_players[key]['x']) + 10 - cameraObject.x,int(active_players[key]['y']) - 18 - cameraObject.y))
                    if active_players[key]["last_used_movement_direction"] == 1:
                        char = pygame.image.load(active_players[key]["walkLeft"][active_players[key]["walk_count"]])
                    elif active_players[key]["last_used_movement_direction"] == 2:
                        char = pygame.image.load(active_players[key]["walkRight"][active_players[key]["walk_count"]])
                    elif active_players[key]["last_used_movement_direction"] == 3:
                        char = pygame.image.load(active_players[key]["walkDown"][active_players[key]["walk_count"]])
                    else:
                        char = pygame.image.load(active_players[key]["walkUp"][active_players[key]["walk_count"]])
                    #else:
                        #char = pygame.image.load(active_players[key]["asset"])
                    win.blit(char, (int(active_players[key]['x']) - cameraObject.x,
                                    int(active_players[key]['y']) - cameraObject.y))
        map_object_load("map_elements/drzwi.png", 1420, 1390, 20, 15, 55, 64)
        map_object_load("map_elements/drzwi.png", 1470, 1390, 20, 15, 55, 64)

        player_hitbox = (player_object_saver['player'].x + 17 - cameraObject.x,
                         player_object_saver['player'].y + 11 - cameraObject.y, 29, 52)
        pygame.draw.rect(win, (255, 0, 0), player_hitbox, 2)
        for i in range(len(list_of_npc)):
            if list_of_npc[i].map == 1:
                map_enemy_load(list_of_npc[i])
        for i in range(len(list_of_enemies)):
            if list_of_enemies[i].map_number == 1:
                map_enemy_load(list_of_enemies[i])
        #map_enemy_load(goblin)
        # Howa.collision_redbox_draw()
        Jiba.collision_redbox_draw()
        goblin.view_attack_box()
        goblin1.view_attack_box()
        if player_object_saver['player'].skill_used != 0:
            print("no co jest")
            player_object_saver['player'].skill_used.attack_draw()
        user_interface()

    if 1== player_object_saver['player'].map:
        first_map_draw_function()
    pygame.display.update()



# Collisions
def collision_first_map():
    for i in range(len(list_of_enemies)):
        if list_of_enemies[i].map_number == 1:
            list_of_enemies[i].hitbox_update()
            first_map_colision_dict[list_of_enemies[i].name] = list_of_enemies[i].collision

    for i in range(len(list_of_npc)):
        if list_of_npc[i].map ==1:
            list_of_npc[i].collision_maker()
            first_map_colision_dict[list_of_npc[i].name] = list_of_npc[i].collision
    collision_maker(230, 0, 0, 0, 600, 360, first_map_colision_dict, "2")
    collision_maker(1420, 1390, 20, 15, 55, 64, first_map_colision_dict, "portal1")
    collision_maker(1470, 1390, 20, 15, 55, 64, first_map_colision_dict, "portal2")


# Skills menu
class SkillsMenu:
    def __init__(self, rows, cols):
        self.skill_slots = []
        self.display_skills_menu = False
        self.rows = rows
        self.cols = cols
        self.total_slots = self.rows * self.cols
        # for mouse events
        self.slots_collisions = []
        self.append_slots()
        # background of menu
        self.menu_image = "map_elements/skills_menu.png"

    def toggle_skill_menu(self):
        self.display_skills_menu = not self.display_skills_menu

    # First time slots in menu builder
    def append_slots(self):
        while len(self.skill_slots) != self.total_slots:
            for x in range(2000 // 2 - ((40 + 2) * self.cols) // 2,
                           2000 // 2 + ((40 + 2) * self.cols) // 2, 40 + 2):
                for y in range(400, 400 + 40 * self.rows, 40 + 2):
                    self.skill_slots.append(SkillSlot(x, y))
                    self.slots_collisions.append(pygame.Rect(x, y, 40, 40))

    def draw(self, screen):
        if self.display_skills_menu:
            skill_menu_img = pygame.image.load("map_elements/skills_menu.png")
            screen.blit(skill_menu_img, (865, 370))
            for slot in self.skill_slots:
                slot.draw(screen)
            for slot in self.skill_slots:
                slot.draw_items(screen)

    def add_skill(self, item, slot=None):
        if slot is None:
            for slots in self.skill_slots:
                if slots.skill is None:
                    slots.skill = item
                    break
class SkillsDownQuickUse:
    def __init__(self, rows, cols):
        self.skill_slots = []
        self.rows = rows
        self.cols = cols
        self.total_slots = self.rows * self.cols
        # for mouse events
        self.slots_collisions = []
        self.append_slots()
        # background of menu
        #self.menu_image = "map_elements/skills_menu.png"
    # First time slots in menu builder
    def append_slots(self):
        while len(self.skill_slots) != self.total_slots:
            for x in range(1300 // 2 - ((40 + 2) * self.cols) // 2,
                           1300 // 2 + ((40 + 2) * self.cols) // 2, 40 + 2):
                for y in range(670, 670 + 40 * self.rows, 40 + 2):
                    self.skill_slots.append(SkillSlot(x, y))
                    self.slots_collisions.append(pygame.Rect(x, y, 40, 40))

    def draw(self, screen):
        #skill_menu_img = pygame.image.load("map_elements/skills_menu.png")
        #screen.blit(skill_menu_img, (865, 370))
        for slot in self.skill_slots:
            slot.draw(screen)
        for slot in self.skill_slots:
            slot.draw_items(screen)

    def add_skill(self, item, slot=None):
        for slots in self.skill_slots:
            slots.skill = item
            break


# Slots for skills in skills menu
class SkillSlot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.skill = None

    def draw(self, screen):
        return pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 40, 40))

    def draw_items(self, screen):
        if self.skill is not None and not self.skill.is_moving:
            self.image = pygame.image.load(self.skill.img).convert_alpha()
            screen.blit(self.image, (self.x, self.y))
        if self.skill is not None and self.skill.is_moving:
            mousepos1 = pygame.mouse.get_pos()
            self.image = pygame.image.load(self.skill.img).convert_alpha()
            screen.blit(self.image, (mousepos1[0] - 20, mousepos1[1] - 20))

skill_quick_use = SkillsDownQuickUse(1,9)

# Enemy Class

list_of_attacks = []

# Attacks
class Attack:
    def __init__(self, width_and_hight_of_skill_area, name, dmg, texture, image):
        self.hitbox = width_and_hight_of_skill_area
        self.name = name
        self.dmg = dmg
        self.description = ""
        self.texture = texture
        self.img = image
        self.is_moving = False
        self.list_of_attacks_append()

    def list_of_attacks_append(self):
        list_of_attacks.append(self)

    # For enginge collisions attack method firs step
    def attack_collision_maker(self):
        x_fix = (self.hitbox / 4) - 35
        y_fix = (self.hitbox / 4) - 40
        parameter = self.hitbox / 2
        attack_hitbox = (player_object_saver['player'].x - cameraObject.x - int(x_fix),
                         player_object_saver['player'].y - cameraObject.y - int(y_fix),
                         int(parameter),
                         int(parameter))
        pygame.draw.rect(win, (255, 0, 0), attack_hitbox, 2)
        attack_collision = pygame.Rect(attack_hitbox)
        player_object_saver['player'].skill_used = self
        print(player_object_saver['player'].skill_used)
        for i in range(len(list_of_enemies)):
            if attack_collision.colliderect(list_of_enemies[i].collision):
                list_of_enemies[i].hit(self)

    # Draw visual for checking
    def collision_redbox_draw(name):
        x_fix = (name.hitbox / 4) - 35
        y_fix = (name.hitbox / 4) - 40
        parameter = name.hitbox / 2
        attack_hitbox = (player_object_saver['player'].x - cameraObject.x - int(x_fix),
                         player_object_saver['player'].y - cameraObject.y - int(y_fix),
                         int(parameter),
                         int(parameter))
        pygame.draw.rect(win, (255, 0, 0), attack_hitbox, 2)

    def attack_draw(self):
        attack_texture = pygame.image.load(self.texture)
        win.blit(attack_texture,(player_object_saver['player'].x - cameraObject.x, player_object_saver['player'].y - cameraObject.y))
# Attacks declarations
Jiba = Attack(400, "Jiba", 1, "assets/jiba1.png", "icons/jiba.png")
Howa = Attack(200, "Howa", 0, "assets/jiba.png", "icons/jiba.png")
attacks_list = [Jiba, Howa]

# Skills menu declaration
skills_menu = SkillsMenu(5, 5)
skills_menu.add_skill(Jiba)

# Collisions dicts
first_map_colision_dict = {}
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

# main window setup
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Samurai no jikan")
font = pygame.font.SysFont('arial',15,False,False)
quick_use_font = pygame.font.SysFont('arial',12,False,False)
skill_first_check = False
# cd for attack timer
attack_cd = time.time()

# Variable for collision checker
last_used_move_key = ""
previous_x = 0
previous_y = 0
# main game loop
while run_pygame == "1":
    clock.tick(30)
    skills_menu_collision = pygame.Rect((1146, 670, 40, 40))
    # collisions quick setup
    #player_hitbox = (player_object_saver['player'].x + 17 - cameraObject.x,
                     #player_object_saver['player'].y + 11 - cameraObject.y, 29, 52)
    #player_collision_rect = pygame.Rect(player_hitbox)
    player_object_saver['player'].update_hitbox(cameraObject.x,cameraObject.y)
    if 1 == player_object_saver['player'].map:
        collision_first_map()
    # Enemies Setup
    for enemies_object in range(len(list_of_enemies)):
        list_of_enemies[enemies_object].move()
        list_of_enemies[enemies_object].respawn_check()
    #print(player_object_saver['player'].xp)
    #experience update
    while player_object_saver['player'].xp >= player_object_saver['player'].next_lvl:
        player_object_saver['player'].lvl = player_object_saver['player'].lvl + 1
        #print(player_object_saver['player'].lvl)
        player_object_saver['player'].xp = player_object_saver['player'].xp - player_object_saver['player'].next_lvl
        player_object_saver['player'].next_lvl = round(player_object_saver['player'].next_lvl * 1.5) * player_object_saver['player'].ability_to_learn
    # Keys events
    pos = pygame.mouse.get_pos()
    x_mouse_pos = pos[0]
    y_mouse_pos = pos[1]
    mouse_collision = pygame.Rect(x_mouse_pos, y_mouse_pos, 1, 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v:
                skills_menu.toggle_skill_menu()
            if event.key == pygame.K_1 and skill_first_check:
                #print(skill_quick_use.skill_slots[0].skill)
                skill_quick_use.skill_slots[0].skill.attack_collision_maker()
               # except:
                #    print(skill_quick_use.skill_slots[1])
                #    print("wtf")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                pos = pygame.mouse.get_pos()
                x_mouse_pos = pos[0]
                y_mouse_pos = pos[1]
                mouse_collision = pygame.Rect(x_mouse_pos, y_mouse_pos, 1, 1)
                print(pos)
                #print(active_players)
                if mouse_collision.colliderect(skills_menu_collision):
                    skills_menu.toggle_skill_menu()
                for i in range(len(skills_menu.slots_collisions)):
                    if mouse_collision.colliderect(
                            skills_menu.slots_collisions[i]) and skills_menu.display_skills_menu == True:
                        skills_menu.skill_slots[i].skill.attack_collision_maker()

    keys = pygame.key.get_pressed()
    for i in range(len(skills_menu.slots_collisions)):
        if mouse_collision.colliderect(
                skills_menu.slots_collisions[i]) and skills_menu.display_skills_menu == True and keys[pygame.K_1]:
                skill_quick_use.add_skill(skills_menu.skill_slots[i].skill,1)
                skill_first_check = True
        if mouse_collision.colliderect(
                skills_menu.slots_collisions[i]) and skills_menu.display_skills_menu == True and keys[pygame.K_2]:
            skill_quick_use.add_skill(skills_menu.skill_slots[i].skill, 2)
        if mouse_collision.colliderect(
                skills_menu.slots_collisions[i]) and skills_menu.display_skills_menu == True and keys[pygame.K_3]:
                skill_quick_use.add_skill(skills_menu.skill_slots[i].skill,3)
        if mouse_collision.colliderect(
                skills_menu.slots_collisions[i]) and skills_menu.display_skills_menu == True and keys[pygame.K_4]:
            skill_quick_use.add_skill(skills_menu.skill_slots[i].skill, 4)
        if mouse_collision.colliderect(
                skills_menu.slots_collisions[i]) and skills_menu.display_skills_menu == True and keys[pygame.K_5]:
                skill_quick_use.add_skill(skills_menu.skill_slots[i].skill,5)
        if mouse_collision.colliderect(
                skills_menu.slots_collisions[i]) and skills_menu.display_skills_menu == True and keys[pygame.K_6]:
                skill_quick_use.add_skill(skills_menu.skill_slots[i].skill,6)
        if mouse_collision.colliderect(
                skills_menu.slots_collisions[i]) and skills_menu.display_skills_menu == True and keys[pygame.K_7]:
                skill_quick_use.add_skill(skills_menu.skill_slots[i].skill,7)
        if mouse_collision.colliderect(
                skills_menu.slots_collisions[i]) and skills_menu.display_skills_menu == True and keys[pygame.K_8]:
                skill_quick_use.add_skill(skills_menu.skill_slots[i].skill,8)
        if mouse_collision.colliderect(
                skills_menu.slots_collisions[i]) and skills_menu.display_skills_menu == True and keys[pygame.K_9]:
                skill_quick_use.add_skill(skills_menu.skill_slots[i].skill,9)
    # movement right left up down events

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:  # and int(player_class_dictionary_global["x_coordinate"]) -vel > 0:
        # update player position data
        last_used_move_key = "left"
        collision_count = 0
        for key in first_map_colision_dict:
            #if player_collision_rect.colliderect(first_map_colision_dict[key]):
            if player_object_saver['player'].collision_rect.colliderect(first_map_colision_dict[key]):
                collision_count += 1
        if collision_count == 0 and keys[pygame.K_RIGHT] == False:
            previous_x = player_object_saver['player'].x
            player_object_saver['player'].x -= vel
            player_object_saver['player'].last_used_movement_direction = 1
            player_object_saver['player'].update(0.5)
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # and int(player_class_dictionary_global["x_coordinate"]) + vel < 2950:
        # update player position data
        last_used_move_key = "right"
        collision_count = 0
        for key in first_map_colision_dict:
            #if player_collision_rect.colliderect(first_map_colision_dict[key]):
            if player_object_saver["player"].collision_rect.colliderect(first_map_colision_dict[key]):
                collision_count += 1
        if collision_count == 0 and keys[pygame.K_LEFT] == False:
            previous_x = player_object_saver['player'].x
            player_object_saver['player'].x += vel
            player_object_saver['player'].last_used_movement_direction = 2
            player_object_saver['player'].update(0.5)
    if keys[pygame.K_UP] or keys[pygame.K_w]:  # and int(player_class_dictionary_global["y_coordinate"]) - vel > 0:
        # update player position data
        last_used_move_key = "up"
        collision_count = 0
        for key in first_map_colision_dict:
            #if player_collision_rect.colliderect(first_map_colision_dict[key]):
            if player_object_saver["player"].collision_rect.colliderect(first_map_colision_dict[key]):
                collision_count += 1
        if collision_count == 0 and keys[pygame.K_DOWN] == False:
            previous_y = player_object_saver['player'].y
            player_object_saver['player'].y -= vel
            player_object_saver['player'].last_used_movement_direction = 4
            player_object_saver['player'].update(0.2)
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:  # and int(player_class_dictionary_global["y_coordinate"]) + vel < 2935:
        # update player position data
        last_used_move_key = "down"
        collision_count = 0
        for key in first_map_colision_dict:
            #if player_collision_rect.colliderect(first_map_colision_dict[key]):
            if player_object_saver['player'].collision_rect.colliderect(first_map_colision_dict[key]):
                collision_count += 1
        if collision_count == 0 and keys[pygame.K_UP] == False:
            previous_y = player_object_saver['player'].y
            player_object_saver['player'].y += vel
            player_object_saver['player'].last_used_movement_direction = 3
            player_object_saver['player'].update(0.2)

    # portal logic setup
    #if player_collision_rect.colliderect(first_map_colision_dict["portal1"]) or player_collision_rect.colliderect(
            #first_map_colision_dict["portal2"]):
    if player_object_saver['player'].collision_rect.colliderect(first_map_colision_dict['portal1']) or player_object_saver['player'].collision_rect.colliderect(first_map_colision_dict['portal2']):
        player_object_saver['player'].map = 2
        player_object_saver['player'].x = 5
        player_object_saver['player'].y = 5
        bg = pygame.image.load("assets/bg.jpg")

    # collision fixer
    collision_count = 0
    for key in first_map_colision_dict:
        #if player_collision_rect.colliderect(first_map_colision_dict[key]):
        if player_object_saver['player'].collision_rect.colliderect(first_map_colision_dict[key]):
            collision_count += 1
    if last_used_move_key == "up" and collision_count > 0:
        player_object_saver['player'].y = previous_y
    if last_used_move_key == "down" and collision_count > 0:
        player_object_saver['player'].y = previous_y
    if last_used_move_key == "left" and collision_count > 0:
        player_object_saver['player'].x = previous_x
    if last_used_move_key == "right" and collision_count > 0:
        player_object_saver['player'].x = previous_x

    # X and Y checker
    if keys[pygame.K_SPACE]:
        # test of cooldowns
        # if time.time() - attack_cd > 3:  # if its been 1 second
        # attack_now = True
        # attack_cd = time.time()
        #print(player_object_saver['player'].x)
        #print(player_object_saver['player'].y)
        #print(skills_menu.skill_slots[0].skill.img)
        #print(vars(skills_menu.skill_slots[0]))
        print(player_object_saver['player'].skill_used)
    # refreshing the camera view
    slide_to(cameraObject,
             (int(player_object_saver['player'].x), player_object_saver['player'].y),
             1 / (clock.get_fps() + 1e-07), 7, (WIDTH / 2, HEIGHT / 2))

    # camera lock to prevent the camera from going off the map
    cameraObject.x = clamp(cameraObject.x, 0, 1720)
    cameraObject.y = clamp(cameraObject.y, 0, 780)
    # window graphic update
    redraw_game_window()
    if player_object_saver['player'].skill_used != 0:
        player_object_saver['player'].skill_animation_count += 1
        if player_object_saver['player'].skill_animation_count > 9:
            player_object_saver['player'].skill_used = 0
            player_object_saver['player'].skill_animation_count = 0
send(DISCONNECT_MESSAGE)
pygame.quit()