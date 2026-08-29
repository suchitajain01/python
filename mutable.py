# Immutable object
x = 10
print("Before:", x, id(x))

x = 20
print("After:", x, id(x))


# Mutable object
numbers = [1, 2, 3]
print("Before:", numbers, id(numbers))

numbers.append(4)
print("After:", numbers, id(numbers))