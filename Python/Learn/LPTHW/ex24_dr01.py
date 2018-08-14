# print some text with a single quote
print("Let's practice everything.")
# print some text with escaped sigle quote and \
print('You\'d need to know \'bout escapes with \\ that do:')
# print some text with a newlines and a tab
print('\n newlines and \t tabs.')

# assign multiline text to a variable, with tabs and newlines
poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# print a separator line
print("--------------")
# print last assigned variable
print(poem)
# print a separator line
print("--------------")


# assign a 5 calculated from a simple expression to a variable
five = 10 - 2 + 3 - 6
# print some text with a variable substituted
print(f"This should be five: {five}")

# define a function with one parameter
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


# initialize a variable
start_point = 10000
# call last function and multi-assign its results
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
# print some formatted text
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
# print some formatted text with f""
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# update a variable content
start_point = start_point / 10

# print some text
print("We can also do that this way:")
# call last function and assign its results to a vector
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
# print the resulted vector content
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))