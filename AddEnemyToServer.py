import pickle
enemies_pickle_open = open("enemies/enemies_pos_upd.pkl", "rb")
enemies_pickle_load = pickle.load(enemies_pickle_open)
enemies_pickle_open.close()
enemies_pickle_load["goblin1"] = {'x': 1435, 'y': 580, 'live': True, 'player_to_follow': '0', 'hp': 1, 'previous_x': 1435, 'previous_y': 580}
print(enemies_pickle_load)
enemy_databse_pickle = open("enemies/enemies_pos_upd.pkl","wb")
pickle.dump(enemies_pickle_load,enemy_databse_pickle)
enemy_databse_pickle.close()