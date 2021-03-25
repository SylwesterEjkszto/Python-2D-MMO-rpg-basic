import time
import pickle

timer = time.time()

while True:
    if time.time() - timer > 2:
        #characters_database_pickle = open(f"characters/smurak.pkl", "wb")
        #pickle.dump(proper_user_name_dict['clan'], characters_database_pickle)
        #characters_database_pickle.close()
        users_login_database_pickle = open(f"characters/smurak.pkl", "rb")
        smth = pickle.load(users_login_database_pickle)
        users_login_database_pickle.close()
        print(smth)
        timer = time.time()