# import command line arguments
from sys import argv

# unpack command line arguments
script, input_file = argv

# define a function to print given file contents
def print_all(f):
    print(f.read())

# define a function to return to the begin of given file
def rewind(f):
    f.seek(0)

# define a function to print a line from given file and its line counter
def print_a_line(line_count, f):
    print(line_count, f.readline())

# open a file with given name
current_file = open(input_file)

print("First let's print the whole file:\n")

# print opened file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# rewind to begin of file
rewind(current_file)

print("Let's print three lines:")

# print line 1
current_line = 1
print_a_line(current_line, current_file)

# print line 2
current_line = current_line + 1
print_a_line(current_line, current_file)

# print line 3
current_line = current_line + 1
print_a_line(current_line, current_file)