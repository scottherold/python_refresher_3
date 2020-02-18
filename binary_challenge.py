# When converting a decimal number to binary, you look for the highest
# power of 2 smaller than the number and put a 1 in that column. You
# then take hte remainder and repeat the process wit hthe next highest 
# power -- putting a 1 if it goes into the remained and a zero 
# otherwise. keep repeating until you have dealt wit all the powers down 
# to 2 ** 0 (i.e., 1)

# Write a program that requests a number from the keyboard, then prints 
# out its binary representation.

# Obviously, you could use a format string, but that is not allowed for 
# this challenge.

# the program should cate for numbers up to 65535; i.e. (2 ** 16) -1

# Hint: you will need integer division (//), and the modulo (%) to get 
# the remainder. You will also need ** to raise one number to the power 
# of another: For example, 2 ** 8 raises 2 to the power of 8.

# As an optional extra, avoid print leading zeros.

# One the working is working, modify it to print Octal rather than 
# binary.

########## SOLUTION ##########

# powers
powers = []
for power in range(15, -1, -1):
    powers.append(2 ** power)
    # powers.append(8 ** power) # octal

print(powers)

# user input
x = int(input("Please enter a number: "))

# sets printing to false
printing = False

# breaks the number down into binary
for power in powers:
    # divides x based on each power 
    bit = x // power

    # check to see if result is a 0
    if bit != 0:
        printing = True

    # print once there is a leading binary operator detected
    if printing:
        # end is what is printed at the end of the line.
        print(bit, end='')
    
    # modulo for remainder
    x %= power