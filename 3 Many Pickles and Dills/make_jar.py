#! /usr/bin/python3
import dill
"""
We will make a jar containing two dills.  
The first dill is the print_me(expression) function we used in vignette 2.
The second dill is a disclaimer text.
"""
def print_me(expression, namespace=globals()):
    print(expression + ' => ', eval(expression, namespace))

medical_disclaimer = """
Disclaimer of Medical Liability. 
This website DOES NOT PROVIDE MEDICAL ADVICE. 
The content is for general informational purposes only. 
The content is not intended to be a substitute for professional medical advice, diagnosis, or treatment. 
Reliance on any information provided is solely at your own risk. 
"""

# the jar is a dictionary
jar = {
    'print_me': print_me,
    'medical_disclaimer': medical_disclaimer
}

jar_dill = dill.dumps(jar)
with open("my_jar.dill", "wb") as fh:
    # dill.dumps(jar, fh)
    fh.write(jar_dill)

print_me("jar")

# new_jar = dict()
with open("my_jar.dill", "rb") as fh:
    new_jar_dill = fh.read()
new_jar = dill.loads(new_jar_dill)
print_me("new_jar")
