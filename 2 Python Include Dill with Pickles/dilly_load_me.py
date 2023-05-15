#! /usr/bin/python3
import dill

with open("print_me.dill", "rb") as fh:
    print_me = dill.load(fh)
hello = "Hello Pickles"
print_me("hello")
print_me("type(hello)")
