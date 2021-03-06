import socket
import threading
import pickle
from Player import *
import time
import ast
HEADER = 8192
PORT =5050
SERVER= socket.gethostbyname(socket.gethostname())
ADDR =(SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
#Usernames = name of object class player for account
username_object_for_active_player = {}
# Dictionary of enemies to update - first recived form onle client and next send to other
enemies_dictionary_update = {}
#users = {} #po usuneiciu uzyytkownikow do uzycia normalna praca - zakomentowane
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
# zakomentować przy pierwszym uruchomieniu
users_login_database_pickle = open("users/data.pkl", "rb")
users = pickle.load(users_login_database_pickle)
users_login_database_pickle.close()
enemies_pickle_open = open("enemies/enemies_pos_upd.pkl", "rb")
enemies_pickle_load = pickle.load(enemies_pickle_open)
enemies_pickle_open.close()
for key in enemies_pickle_load:
    enemies_dictionary_update[key] = enemies_pickle_load[key]


def handler_client(conn, addr):
    print(f"[NEW CONNECTIONS] {addr} connected.")
    proper_user_name_dict = {}
    connected = True
    timer = time.time()
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if "username" in msg:
                username_split = msg.split('&')
                proper_username = username_split[0]
                proper_user_name_dict["proper_username"] = proper_username
                password_split = msg.split("`")
                proper_password = password_split[1]
                print(proper_password)
                if proper_username in users:
                    if users[proper_username] == proper_password:
                        print(f'{addr} looged in - {proper_username}')

                        conn.send("you can log in".encode(FORMAT))
                        #characters_database_pickle = open(f"characters/{proper_username}.pkl", "r")
                        #pickle.load(characters_database_pickle)
                        #characters_database_pickle.close()
                    else:
                        print("bad password")
                if proper_username not in users:
                    users[proper_username] = proper_password
                    users_login_database_pickle = open("users/data.pkl", "wb")
                    pickle.dump(users, users_login_database_pickle)
                    users_login_database_pickle.close()
                    proper_user_name_dict["clan"] = Player()
                    proper_user_name_dict["clan"].name = proper_username
                    #print(vars(users[proper_username]))
                    characters_database_pickle = open(f"characters/{proper_user_name_dict['proper_username']}.pkl", "wb")
                    pickle.dump(proper_user_name_dict["clan"], characters_database_pickle)
                    characters_database_pickle.close()
                    #characters_database = {character_name:users[proper_username]}
                    #print(characters_database)
                    conn.send("your account is ready".encode(FORMAT))
                    print(f'{addr} maked an account - {proper_username}')
            if "I can login" in msg:
                characters_database_pickle = open(f"characters/{proper_user_name_dict['proper_username']}.pkl", "rb")
                das = pickle.load(characters_database_pickle)
                characters_database_pickle.close()
                smth_to_send = pickle.dumps(das)
                conn.send(smth_to_send)
                enemies_to_send = pickle.dumps(enemies_dictionary_update)
                conn.send(enemies_to_send)
                #conn.send(f'{das} & {enemies_dictionary_update}'.encode(FORMAT))
            if "first clan" in msg:
                msg_clan_split = msg.split('&')
                proper_clan = msg_clan_split[1]
                proper_user_name_dict["clan"].clan  = proper_clan
                characters_database_pickle = open(f"characters/{proper_user_name_dict['proper_username']}.pkl", "wb")
                pickle.dump(proper_user_name_dict['clan'], characters_database_pickle)
                pickle_to_send = pickle.dumps(proper_user_name_dict['clan'])
                characters_database_pickle.close()
                conn.send(pickle_to_send)


            if "update" in msg:
                # Load for login method
                characters_database_pickle = open(f"characters/{proper_user_name_dict['proper_username']}.pkl", "rb")
                proper_user_name_dict["clan"] = pickle.load(characters_database_pickle)
                characters_database_pickle.close()
                # Update and send to client
                username_object_for_active_player[proper_user_name_dict["proper_username"]] = vars(proper_user_name_dict["clan"])
                msg_update_split = msg.split('&')
                #print(msg_update_split)
                proper_user_name_dict["clan"].x = int(msg_update_split[1])
                proper_user_name_dict["clan"].y = int(msg_update_split[2])
                proper_user_name_dict["clan"].map = int(msg_update_split[3])
                proper_user_name_dict["clan"].walk_count = int(msg_update_split[4])
                proper_user_name_dict["clan"].lvl = int(msg_update_split[6])
                proper_user_name_dict["clan"].xp = int(msg_update_split[7])
                proper_user_name_dict["clan"].next_lvl = int(msg_update_split[8])
                proper_user_name_dict["clan"].last_used_movement_direction =int(msg_update_split[5])
                enemies_respond = ast.literal_eval(msg_update_split[9].strip())
                proper_user_name_dict["clan"].hitbox =  eval(msg_update_split[10])
                for key in enemies_respond:
                    if enemies_respond[key]["respawn"] == 1 and enemies_dictionary_update[key]["hp"] == 0:
                        enemies_dictionary_update[key]["x"] = enemies_respond[key]["x"]
                        enemies_dictionary_update[key]["y"] = enemies_respond[key]["y"]
                        enemies_dictionary_update[key]["hp"] = enemies_respond[key]["max_hp"]
                        enemies_dictionary_update[key]["live"] = True

                    if enemies_dictionary_update[key]["previous_x"] != enemies_respond[key]["x"] and enemies_dictionary_update[key]["previous_y"] != enemies_respond[key]["y"] :
                        if enemies_dictionary_update[key]["x"] - enemies_respond[key]["x"] == 3 or enemies_dictionary_update[key]["x"] - enemies_respond[key]["x"] == -3 or enemies_dictionary_update[key]["x"] - enemies_respond[key]["x"] == 0:
                            if enemies_dictionary_update[key]["y"] - enemies_respond[key]["y"] == 3 or enemies_dictionary_update[key]["y"] - enemies_respond[key]["y"] == -3 or enemies_dictionary_update[key]["y"] - enemies_respond[key]["y"] ==0:
                                enemies_dictionary_update[key]["x"] = enemies_respond[key]["x"]
                                enemies_dictionary_update[key]["y"] = enemies_respond[key]["y"]
                                enemies_dictionary_update[key]["previous_x"] = enemies_respond[key]["previous_x"]
                                enemies_dictionary_update[key]["previous_y"] = enemies_respond[key]["previous_y"]
                    #enemies_dictionary_update[key]["hp"] = enemies_respond[key]['hp']
                    if enemies_dictionary_update[key]["hp"] == 0 and enemies_respond[key]['hp'] != 0:
                        enemies_dictionary_update[key]['hp'] = 0
                    if enemies_dictionary_update[key]['hp'] != 0:
                        enemies_dictionary_update[key]['hp'] = enemies_respond[key]['hp']
                    #if enemies_dictionary_update[key]["hp"] > 0 :
                        #enemies_dictionary_update[key]["player_to_follow"] = enemies_respond[key]["player_to_follow"]
                    if enemies_respond[key]["player_to_follow"] != "0" and enemies_respond[key]["player_to_follow"] != 0 :
                        enemies_dictionary_update[key]["player_to_follow"] = enemies_respond[key]["player_to_follow"]
                    if enemies_dictionary_update[key]["hp"] < 1:
                        enemies_dictionary_update[key]["live"] = False
                        enemies_dictionary_update[key]["player_to_follow"] = "0"
                something = {"smth":"smth"}
                conn.send(f"{username_object_for_active_player} & {something} & {enemies_dictionary_update}".encode(FORMAT))
            if msg == DISCONNECT_MESSAGE:
                connected = False

            if time.time() - timer > 30:
                characters_database_pickle = open(f"characters/{proper_user_name_dict['proper_username']}.pkl", "wb")
                pickle.dump(proper_user_name_dict['clan'], characters_database_pickle)
                characters_database_pickle.close()
                enemy_databse_pickle = open("enemies/enemies_pos_upd.pkl","wb")
                pickle.dump(enemies_dictionary_update,enemy_databse_pickle)
                enemy_databse_pickle.close()
                timer = time.time()


    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is Listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handler_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")



start()
