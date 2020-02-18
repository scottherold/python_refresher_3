# this will print the numbers 0-16 in binary
for i in range(17):
    # {:08b} tells Python to convert the numbers in binary bytes
    # remember a byte is 8 bits, which explains the formula
    print("{0:>2} in binary is {0:>08b}".format(i))