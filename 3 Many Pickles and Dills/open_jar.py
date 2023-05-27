
import dill

# the jar is stored in the my_jar.dill file
with open("./my_jar.dill", "rb") as fh:
    jar_dill = fh.read()

jar = dill.loads(jar_dill)

print("jar is a ", type(jar))
keys = [key for key in jar.keys()]
print("its keys are", keys)
print("\nlooping thru the keys of jar\n")

for key in keys:
    print(key, "is a", type(jar[key]))

print('')

for key in jar.keys():
    globals()[key] = jar[key]

print("\ntesting")
print(medical_disclaimer[:35])
print_me("medical_disclaimer[:35]")

