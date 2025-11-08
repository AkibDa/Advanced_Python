def mydecorater(func):
  def wrapper(*args, **kwargs):
    print("Before function call")
    return func(*args, **kwargs)
  return wrapper

@mydecorater
def hello(person):
  return "Hello, {}!".format(person)
  
# mydecorater(hello)()
hello()
# hello("Alice") # This will raise an error because wrapper() does not accept any arguments
print(hello("Alice"))

# Practical example #1 of decorators - logging

def log_decorator(func):
  def wrapper(*args, **kwargs):
    print(f"Calling function {func.__name__} with args: {args} and kwargs: {kwargs}")
    result = func(*args, **kwargs)
    print(f"Function {func.__name__} returned: {result}")
    return result
  return wrapper

@log_decorator
def add(a, b):
  return a + b

@log_decorator
def multiply(a, b):
  return a * b

add(3, 5)
multiply(4, 6)

# Practical example #2 of decorators - timing

import time

def time_decorator(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to execute")
    return result
  return wrapper

@time_decorator
def slow_function(seconds):
  time.sleep(seconds)
  return "Finished"

slow_function(2)
slow_function(1)