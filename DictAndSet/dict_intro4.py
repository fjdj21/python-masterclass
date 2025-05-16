from z_debuggers import banner, ruler

vehicles = {
    'dream': 'Honda 250T',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimmy': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple',
}

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"

# Upgrade the Virago
vehicles['virago'] = "Yamaha XV535"  # replaces the original value

del vehicles['starfighter']  # removing an item from a dictionary
# del vehicles['f1'] # not existing key from values dict | produces an error

# Pop method
#   - removes an item from the dictionary and returns the value
#   - if `key` doesn't exist, it returns whatever you pass for default
#       instead.
vehicles.pop('f1', None)
result = vehicles.pop('f1', "You wish! Sell the Learjet and you might afford a racing car.")
print(result)
plane = vehicles.pop('learjet')
print(plane)
bike = vehicles.pop('tenere', 'not present')
print(bike)
ruler()

# iterating over key with values using the .items() method
for key, value in vehicles.items():
    print(key, value, sep=" : ")
