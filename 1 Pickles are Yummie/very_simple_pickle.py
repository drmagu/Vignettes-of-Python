#! /usr/bin/python3
"""
This script demonstrates the use of Python's pickle module for object serialization and deserialization.
It serializes a string, then deserializes it back to its original form, and finally compares the original 
string with the deserialized one to check if they are identical.

pickle.dumps() is used to convert a Python object into a byte stream, and pickle.loads() is used to 
convert a byte stream back into a Python object.
"""

import pickle

def print_me(expression, namespace=globals()):
    """
    Evaluates and prints a given expression within a specific namespace.
    
    Args:
        expression: String representing the expression to be evaluated.
        namespace: Dictionary representing the namespace within which to evaluate the expression. 
                   Defaults to the global namespace.
    """
    print(expression + ' => ', eval(expression, namespace))

yummies = "Pickles are yummie!"
print_me("yummies, type(yummies)")
print_me('yummies.__sizeof__()')

# Serialize the string using pickle.dumps()
the_pickle = pickle.dumps(yummies)
print(f"the_pickle =>", the_pickle)
print("as you can see, this is a string of bytes")
print_me("type(the_pickle)")
print_me('the_pickle.__sizeof__()')

# Deserialize the string using pickle.loads()
print("fresh_string = pickle.loads(the_pickle)")
fresh_string = pickle.loads(the_pickle)
print_me("pickle.loads(the_pickle)")  # Display the deserialized string

# Check if the original string is identical to the deserialized string
print("check `yummies == fresh_string`")
print_me("yummies == fresh_string")
