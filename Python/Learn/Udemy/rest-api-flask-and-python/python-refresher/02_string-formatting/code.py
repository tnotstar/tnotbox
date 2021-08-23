# f-string templates

name = "Bob"
greeting = f"Hello, {name}"
print(greeting)
print(f"Hello, {name}")

name = "Rolf"
print(greeting)
print(f"Hello, {name}")

# Template strings with .format(...)

name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)
with_name_two = greeting.format("Rolf")
print(with_name)
print(with_name_two)

longer_phrase = "Hello, {}. Today is {}"
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)
