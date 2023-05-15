#! /usr/bin/python3
import pickle

with open("my_hello.pkl", "rb") as fh:
    my_func = pickle.load(fh)

my_func("Peter")

