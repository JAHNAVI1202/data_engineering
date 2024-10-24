#1
import functools

def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Return value: {result}")
        return result
    return wrapper

# Example usage
@log_function_call
def add(a, b):
    return a + b

# Test the decorator
add(3, 4)
#2
class customRange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        current_value = self.current
        self.current += self.step
        return current_value

# Example usage
for i in customRange(0, 10, 2):
    print(i)
#3
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Example usage
prime_gen = prime_generator()
for _ in range(10):
    print(next(prime_gen))
