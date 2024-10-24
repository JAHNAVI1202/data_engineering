def fibonacci_generator(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

gen = fibonacci_generator(10)

for value in gen:
    print(value)