import socket
import threading
import pickle
from Player import *
import time
HEADER = 2048
PORT =5050
SERVER= socket.gethostbyname(socket.gethostname())
ADDR =(SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
#Usernames = name of object class player for account
username_object_for_active_player = {}

#users = {} #po usuneiciu uzyytkownikow do uzycia normalna praca - zakomentowane
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
# zakomentować przy pierwszym uruchomieniu
users_login_database_pickle = open("users/data.pkl", "rb")
users = pickle.load(users_login_database_pickle)
users_login_database_pickle.close()
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
                proper_user_name_dict["clan"].x_coordinate = int(msg_update_split[1])
                proper_user_name_dict["clan"].y_coordinate = int(msg_update_split[2])
                proper_user_name_dict["clan"].map = str(msg_update_split[3])
                pickle_to_send = pickle.dumps(username_object_for_active_player)
                conn.send(pickle_to_send)
                # test
                #update_my_own_db=open(f"characters/{proper_user_name_dict['proper_username']}.pkl", "wb")
                #pickle.dump(proper_user_name_dict["clan"], update_my_own_db)
                #update_my_own_db.close()
            #disconnect from server

            if msg == DISCONNECT_MESSAGE:
                connected = False

            if time.time() - timer > 30:
                characters_database_pickle = open(f"characters/{proper_user_name_dict['proper_username']}.pkl", "wb")
                pickle.dump(proper_user_name_dict['clan'], characters_database_pickle)
                characters_database_pickle.close()
                users_login_database_pickle = open(f"characters/{proper_user_name_dict['proper_username']}.pkl", "rb")
                smth = pickle.load(users_login_database_pickle)
                users_login_database_pickle.close()
                #print(vars(smth))
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

# What i wanna do after disconnect
for key in username_object_for_active_player:
    username_object_for_active_player[key]["active"] = "afk"
    print(username_object_for_active_player[key])