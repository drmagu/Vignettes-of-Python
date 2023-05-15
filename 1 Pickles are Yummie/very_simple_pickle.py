#! /usr/bin/python3
import pickle

def print_me(expression, namespace=globals()):
    print(expression + ' => ', eval(expression, namespace))

yummies = "Pickles are yummie!"
print_me("yummies, type(yummies)")
print_me('yummies.__sizeof__()')
the_pickle = pickle.dumps(yummies)
print(f"the_pickle =>", the_pickle)
print("as you can see, this is a string of bytes")
print_me("type(the_pickle)")
print_me('the_pickle.__sizeof__()')
print("fresh_string = pickle.loads(the_pickle)")
fresh_string = pickle.loads(the_pickle)
print_me("pickle.loads(the_pickle)")
print("check `yummies == fresh_string`")
print_me("yummies == fresh_string")
