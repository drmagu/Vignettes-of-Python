#! /usr/bin/python3
import pickle

with open("my_func.pkl", "rb") as fh:
    my_func = pickle.load(fh)
hello = "Hello Pickles"
my_func("hello")
my_func("type(my_func)")
