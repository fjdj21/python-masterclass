vehicles = {
    'dream'     :   'Honda 250T',
    'roadster'  :   'BMW R1100',
    'er5'       :   'Kawasaki ER5',
    'can-am'    :   'Bombardier Can-Am 250',
    'virago'    :   'Yamaha XV250',
    'tenere'    :   'Yamaha XT650',
    'jimmy'     :   'Suzuki Jimny 1.5',
    'fiesta'    :   'Ford Fiesta Ghia 1.4',
}


# # iterating over key
# for key in vehicles:
#     print(key)

# # iterating over key with its values
# for key in vehicles:
#     print(key, vehicles[key], sep=' : ')

# iterating over key with values using the .items() method
for key, value in vehicles.items():
    print(key, value, sep=" : ")
