name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = 2.54 * height
weight = 180 # lbs
weight_kg = weight / 2.2
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches ({height_cm} centimeters) tail.")
print(f"He's {weight} pounds ({weight_kg} kilograms) heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")