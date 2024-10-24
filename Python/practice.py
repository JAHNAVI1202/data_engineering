#1
def infinite_evens():
    num = 0
    while True:
        yield num
        num += 2

# Using the generator
even_gen = infinite_evens()
for _ in range(10):
    print(next(even_gen))
    #2 geenrator expression
squares_gen = (x**2 for x in range(10))

# Using the generator
for square in squares_gen:
    print(square)
#3
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

file_gen = read_large_file('Python/Exam.txt')

for line in file_gen:
    print(line.strip())
#4
def generate_numbers(n):
    for i in range(n):
        yield i

def filter_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

def square(numbers):
    for num in numbers:
        yield num ** 2

# Creating the generator pipeline
numbers = generate_numbers(10)
even_numbers = filter_even(numbers)
squared_evens = square(even_numbers)

# Using the generator
for num in squared_evens:
    print(num)