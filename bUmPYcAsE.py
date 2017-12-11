import random

inputString = raw_input("Make this string bumpy: ")
input = [x for x in inputString]
x = [each for each in range(len(input))]

for each in range(int(len(input)*0.85)):
    index = random.choice(x)
    input[index] = input[index].upper()
    
print "".join(input)

##