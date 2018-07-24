# assign 10 to types_of_people
types_of_people = 10
# make a string substituting the value of types_of_people
x = f"There are {types_of_people} types of people."

# assign some text to some variables
binary = "binary"
do_not = "don't"
# make a string substituting last variable's values
y = f"Those who know {binary} and those who {do_not}."

# printing string variables
print(x)
print(y)

# printing formatting string values
print(f"I said: {x}")
print(f"I also said: '{y}'")

# assigning some values to some variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# printing a formatted string
print(joke_evaluation.format(hilarious))

# again, assigning some text to some vars
w = "This is the left side of..."
e = "a string with a right side."

# printing a concatenation expression
print(w + e)