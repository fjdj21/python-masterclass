vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimmy': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

my_car = vehicles['fiesta']  # if doesn't match, produces an error
print(my_car)

commuter = vehicles['virago']
print(commuter)

# get method
learner = vehicles.get('er5')  # case sensitive
print(learner)

learner = vehicles.get('ER5')  # returns None
print(learner)
