import pickle
enemies_pickle_open = open("enemies/enemies_pos_upd.pkl", "rb")
enemies_pickle_load = pickle.load(enemies_pickle_open)
enemies_pickle_open.close()
print(users)