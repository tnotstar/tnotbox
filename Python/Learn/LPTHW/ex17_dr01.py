from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

buffer = open(from_file).read()

print(f"The input file is {len(buffer)} bytes long")

out_file = open(to_file, "w")
out_file.write(buffer)
out_file.close()

print("Alright, all done.")