
import dill
simp = {'a': 1, 'b': 2}
simp_dill = dill.dumps(simp)
print(simp_dill)
simp_1 = dill.loads(simp_dill)
print("simp == simp_1", (simp == simp_1))

sometext = """This is some text.
Nothing serious!"""
dimp = {'sometext': sometext}
dimp_dill = dill.dumps(dimp)
dimp_1 = dill.loads(dimp_dill)
print(dimp_1['sometext'])

def say_hello(name):
    return f"Well, {name}, hello there!"
print(say_hello("Willy"))
sometext = """This is some new text.
Nothing serious!"""
ddimp = {'sometext': sometext, 'hello': say_hello}
ddimp_dill = dill.dumps(ddimp)
ddimp_1 = dill.loads(ddimp_dill)
print(ddimp_1['sometext'])
print(ddimp_1['hello']('Johnny'))


