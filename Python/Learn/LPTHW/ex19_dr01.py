# define a function named cheese_and_crackers with parameters cheese_count & boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print some formatted messages
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # print simple text
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
# call cheese_and_crackers with literal values as arguments
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
# declare two variables
amount_of_cheese = 10
amount_of_crackers = 50

# call cheese_and_crackers with variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# call cheese_and_crackers with simple expressions as arguments
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
# call cheese_and_crackers with complex expressions as arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)