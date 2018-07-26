from sys import argv

script, first, second = argv
prompt = "> "

print(f"Hi {first}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {first}?")
likes = input(prompt)

print(f"Where do you live {first}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright {first}, your alias is {second}
and so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")