
l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf" ,"Anne")
s = {"Bob", "Rolf", "Anne"}

print(l[0], l[2])

try:
    t[1] = "Hello"
except Exception as ex:
    print(f"{ex}: tuples are unmutable!!")

l[1] = "Hello"
l.append("Smith")
print(l)

s.remove("Anne")
s.add("Smith")
s.add("Smith")
print(s)