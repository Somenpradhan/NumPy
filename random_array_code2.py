# Ask the use to enter a digit. Choose a Position (0-9) in an array if size 10. Create a random array (0-9) of size 10. If the digit it at the position of your choice
import numpy as np
array = np.random.choice(10, 10)
np.random.randint(0, 10, 10)
print("Random Array:", array)
position = int(input("Enter a position (0-9): "))

if position < 0 or position > 9:
    print("Invalid position")
else:
    digit = int(input("Enter a digit (0-9): "))
    if digit == array[position]:
        print("You guessed it right")
    else:
        print("You guessed it wrong")
        print("The digit at position", position, "is:", array[position]) 
