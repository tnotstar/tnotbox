from sys import argv

# unpack command line arguments
script, filename = argv

# open the input file
txt = open(filename)

# print a title, read whole file and print all of it
print(f"Here's your file {filename}:")
print(txt.read())

# ask for the filename again
print("Type the filename again:")
file_again = input("> ")

# open the input file again
txt_again = open(file_again)

# read and prints whole file
print(txt_again.read())