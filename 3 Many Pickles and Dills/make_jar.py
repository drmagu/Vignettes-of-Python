
import dill
"""
We will make a jar containing two dills.  
The first dill is the print_me(expression) function we used in vignette 2.
The second dill is a disclaimer text.
"""
def print_me(expression, namespace=globals()):
    """
    Function that evaluates and prints the result of an expression.
    """
    namespace = globals()
    print(expression + ' => ', eval(expression, namespace))

medical_disclaimer = """
Disclaimer of Medical Liability. 
This website DOES NOT PROVIDE MEDICAL ADVICE. 
The content is for general informational purposes only. 
The content is not intended to be a substitute for professional medical advice, diagnosis, or treatment. 
Reliance on any information provided is solely at your own risk. 
"""

def create_jar():
    """
    Function that pickles two items: the print_me function and a disclaimer text.
    """
    # the jar is a dictionary
    jar = {
        'print_me': print_me,
        'medical_disclaimer': medical_disclaimer
    }

    jar_dill = dill.dumps(jar)

    # Write the serialized jar into a file
    with open("./my_jar.dill", "wb") as fh:
        # dill.dumps(jar, fh)
        fh.write(jar_dill)

    print(f"jar: {jar}")

    # Load the jar back from the file to verify
    new_jar_dill = None
    with open("./my_jar.dill", "rb") as fh:
        new_jar_dill = fh.read()
    new_jar = dill.loads(new_jar_dill)
    print(f"new_jar: {new_jar}")

if __name__ == "__main__":
    create_jar()
