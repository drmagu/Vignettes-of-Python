#! /usr/bin/python3
import pickle

def hello(name):
    return f"Hi there {name}, good to see ya!"

with open("my_hello.pkl", "wb") as fh:
    pickle.dump(hello, fh)

print("'my_hello.pkl' is ready to be used")
with open("my_hello.pkl", "rb") as fh:
    my_func = pickle.load(fh)
print(my_func("Bob"))
