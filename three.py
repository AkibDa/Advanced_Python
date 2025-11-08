# No wastage of memory 

# Seq 1 to 90

import sys

def mygenerator(x):
  for i in range(x):
    yield i ** 3
    
values = mygenerator(90)

# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))

for _ in values:
  print(_, end=' ')
  
print(sys.getsizeof(values))

def infinite_generator():
  num = 1
  while True:
    yield num
    num *= 10
    
inf_gen = infinite_generator()

# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))

for _ in range(10):
  print(next(inf_gen), end=' ')