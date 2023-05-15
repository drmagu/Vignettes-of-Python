#! /usr/bin/python3
import pickle

def print_me(expression, namespace=globals()):
    print(expression + ' => ', eval(expression, namespace))

with open("my_func.pkl", "wb") as fh:
    pickle.dump(print_me, fh)

print("'my_func.pkl' is ready to be used")
with open("my_func.pkl", "rb") as fh:
    my_func = pickle.load(fh)
hello = "Hello Pickles"
my_func("hello")
my_func("type(my_func)")

