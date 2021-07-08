import pickle

users = {}
nadpisz = open("users/data.pkl", "wb")
pickle_dump = pickle.dump(users,nadpisz)
nadpisz.close()
