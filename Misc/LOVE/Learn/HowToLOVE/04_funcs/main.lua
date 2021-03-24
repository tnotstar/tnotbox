a = 1
b = 2
function addition(a, b)
    c = a + b
    print("Inside addition:", a, b, c)
    return c
end

print("Before call:", a, b, c)
result = addition(9, 5)

print("After call:", a, b, c)
print("Result:", result)

function introduction(name, age, country)
    print("Hi, my name is " .. name .. ". I'm " .. age .. " years old, and I live in " .. country .. ".")
end

introduction("Daniel", "21", "the Netherlands")
introduction("Steve", "40", "Germany")
