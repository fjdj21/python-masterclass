age = 24
print("My age is " + str(age) + " years") #we cast(coerce) the age as a string
## an alternative is we can coerce it using the .format() method
print("My age is {0} years".format(age)) #this means that we put the age argument, and it's the first sequence which is 0
### this is also called replacement fields
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
    .format(31, "Jan", "Mar", "May", "July", "Aug", "Oct", "Dec"))
print("There are {0} days in Jan, Mar, May, July, Aug, Oct and Dec"
      .format(31))
print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))
print()
print("""Jan: {2}
Feb: {0} 
Mar: {2}
Apr: {1} 
May: {2} 
Jun: {1} 
Jul: {2} 
Sep: {1} 
Oct: {2} 
Nov: {1} 
Dec: {2}
""".format(28, 30, 31))
