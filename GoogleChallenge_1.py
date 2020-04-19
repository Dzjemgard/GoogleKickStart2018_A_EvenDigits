# Google Kickstart Challenge
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/00000000000510ed

# Vars
myArray = []
position = 0

#N = input("Integer value here: \n")   # User inputed number as string
N = str(1340)
print("Integer Value: " + N)
numOfDigits = len(N)

# Turns the string into an array format
for digit in N:
    myArray.append(int(digit))

# Copies the arrays to make them distinct from the orignal array
upArray = myArray.copy()
downArray = myArray.copy()

# counting down
for n in downArray:
    # Check if Even/Odd
    if n%2 != 0:     
        n -= 1
        downArray[position] = n
    
    # Check the special case when all of the elements to the right of the decreased need to convert to 8
    # 9 in this instance is odd, which is considered unacceptable, so 8 is used in place
    if position > 0 and position < numOfDigits and (downArray[position-1] < myArray[position-1]):
        for x in range(position,numOfDigits):
            downArray[x] = 8

    # Iterate through the position
    position += 1

# counting up
position = 0
for n in upArray:
    # Check if Even
    if n%2 != 0:
        n += 1
        upArray[position] = n
    
    # Check for the special case where all digits to the right need to be zeroed out.
    if position > 0 and position < numOfDigits and (upArray[position-1] > myArray[position-1]):
        for x in range(position,numOfDigits):
            upArray[x] = 0

    # Iterate to the next position
    position += 1

# Turn array elements into strings
U = ''
for item in upArray:
    U += str(item)

O = ''
for item in myArray:
    O += str(item)


L = ''
for item in downArray:
    L += str(item)

# Turn array elements into ints
U = int(U)
O = int(O)
L = int(L)

# print(U,O,L)

# Calculate distances to find the path of least resistance
counterUO = U - O
counterLO = O - L

# print(counterLO,counterUO)

# Determine whether the upper limit/lower limit should be used or if they are equal
if counterUO > counterLO:
    print("Lower value: " + str(L) + " @ " + str(counterLO))
elif counterUO < counterLO:
    print("Upper value: " + str(U) + " @ " + (counterUO))
else:
    print("either value is accepted: " + str(counterUO) + " @ " + str(U))