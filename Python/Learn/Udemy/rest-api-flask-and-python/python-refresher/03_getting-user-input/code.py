name = input("Enter your name: ")
print(name)

size_input = input("How big is your house (in squre feet): ")
square_feet = int(size_input)
square_metres = square_feet / 10.8
print("{} square feet are {:.2f} square metres.".format(square_feet, square_metres))
print(f"{square_feet} square feet are {square_metres:.2f} square metres.")
