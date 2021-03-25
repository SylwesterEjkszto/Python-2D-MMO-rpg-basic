import pickle

users = {}
nadpisz = open("users/data.pkl", "wb")
chuj = pickle.dump(users,nadpisz)
nadpisz.close()