# this will print the numbers 0-16 in hex
for i in range(17):
    # {:02x} tells Python to convert the numbers in hex nibbles
    print("{0:>2} in hex is {0:>02x}".format(i))

# hex value arithmetic
x = 0x20 # this is 32
y = 0x0a # this is 10

print(x)
print(y)
print(x * y) # this equals 320