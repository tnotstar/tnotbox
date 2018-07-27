from sys import argv

script, filename = argv

stream = open(filename)
print(stream.read())
stream.close()