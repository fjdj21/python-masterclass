vehicles = {
    'dream'     :   'Honda 250T',
    'roadster'  :   'BMW R1100',
    'er5'       :   'Kawasaki ER5',
    'can-am'    :   'Bombardier Can-Am 250',
    'virago'    :   'Yamaha XV250',
    'tenere'    :   'Yamaha XT650',
    'jimmy'     :   'Suzuki Jimny 1.5',
    'fiesta'    :   'Ford Fiesta Ghia 1.4',
    'roadster'  :   'Triumph Street Triple', # duplicate, replaces old value
}

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"

# Upgrade the Virago
vehicles['virago'] = "Yamaha XV535" # replaces the original value

# iterating over key with values using the .items() method
for key, value in vehicles.items():
    print(key, value, sep=" : ")
