import socket
import threading
import pickle
from Player import *
HEADER = 64
PORT =5050
SERVER= socket.gethostbyname(socket.gethostname())
ADDR =(SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
username_object_for_player = {}
character_name_dictionary = {}
#users = {} #po usuneiciu uzyytkownikow do uzycia normalna praca - zakomentowane
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
# zakomentować przy pierwszym uruchomieniu
users_login_database_pickle = open("users/data.pkl", "rb")
users = pickle.load(users_login_database_pickle)
users_login_database_pickle.close()
def handler_client(conn, addr):
    print(f"[NEW CONNECTIONS] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            proper_username = ""
            users[proper_username] = ""
            if "username" in msg:
                username_split = msg.split('&')
                proper_username = username_split[0]
                password_split = msg.split("`")
                proper_password = password_split[1]
                if proper_username in users:
                    if users[proper_username] == proper_password:
                        print(f'{addr} looged in - {proper_username}')
                        conn.send("you can log in".encode(FORMAT))
                        #characters_database_pickle = open(f"characters/{proper_username}.pkl", "r")
                        #pickle.load(characters_database_pickle)
                        #characters_database_pickle.close()
                    else:
                        print("bad password")
                else:
                    users[proper_username] = proper_password
                    users_login_database_pickle = open("users/data.pkl", "wb")
                    pickle.dump(users, users_login_database_pickle)
                    users_login_database_pickle.close()
                    character_name = users[proper_username]
                    character_name_dictionary[addr] = character_name
                    users[proper_username] = Player()
                    users[proper_username].name = character_name
                    username_object_for_player[addr] = users[proper_username]
                    #print(vars(users[proper_username]))
                    characters_database_pickle = open(f"characters/{character_name}.pkl", "wb")
                    pickle.dump(users[proper_username], characters_database_pickle)
                    characters_database_pickle.close()
                    #characters_database = {character_name:users[proper_username]}
                    #print(characters_database)
                    conn.send("your account is ready".encode(FORMAT))
                    print(f'{addr} maked an account - {proper_username}')
            # nie działa
            if "first clan" in msg:
                character_name = character_name_dictionary[addr]
                msg_clan_split = msg.split('&')
                proper_clan = msg_clan_split[1]
                #print("smth" + proper_clan[0])
               # print(f'{proper_username}')
                #characters_database_pickle = open(f"characters/{proper_username}.pkl", "rb")
                #pickle.load(users[proper_username])
                username_object_for_player[addr].clan  = proper_clan
                characters_database_pickle = open(f"characters/{character_name}.pkl", "wb")
                pickle.dump(username_object_for_player[addr], characters_database_pickle)
                pickle_to_send = pickle.dumps(username_object_for_player[addr])
                characters_database_pickle.close()
                print(vars(username_object_for_player[addr]))
                conn.send(pickle_to_send)
                #characters_database_pickle.close()
            if msg == DISCONNECT_MESSAGE:
                connected = False
            #print(f"[{addr}] {msg}")
            #conn.send("Msg recived".encode(FORMAT))
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