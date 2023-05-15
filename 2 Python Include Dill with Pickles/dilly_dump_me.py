#! /usr/bin/python3
import dill

def print_me(expression, namespace=globals()):
    print(expression + ' => ', eval(expression, namespace))

with open("print_me.dill", "wb") as fh:
    dill.dump(print_me, fh)

print("'print_me.dill' is ready to be used")
with open("print_me.dill", "rb") as fh:
    print_me = dill.load(fh)
hello = "Hello Pickles"
print_me("hello")
print_me("type(hello)")

