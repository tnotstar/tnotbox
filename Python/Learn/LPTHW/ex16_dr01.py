from sys import argv

# unpack command line arguments
script, filename = argv

# ask user for confirmation or break
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# wait for user input
input("?")

print("Opening the file...")
# open file with given filename
target = open(filename, "w")

print("Truncating the file. Goodbye!")
# truncate (make it zero length) last open file
target.truncate()

print("Now I'm going to ask you for three lines.")

# ask for new file contents
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# write new file contents
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# close the new file
target.close()