#! /usr/bin/python3
import pickle

def print_me(expression, namespace=globals()):
    print(expression + ' => ', eval(expression, namespace))

pickle_func = pickle.dumps(print_me)
my_func = pickle.loads(pickle_func)
hello = "Hello Pickles"
my_func("hello")
my_func("type(my_func)")
