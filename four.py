def myfunction(*args, **kwargs):
  print("Arguments:", args)
  print("Keyword Arguments:", kwargs['key'])
  
myfunction(1, 2, 3, key='value')

import sys
import getopt

print(sys.argv[0]) # will print the name of the script

# Usage : python four.py filename.txt "This is a message"

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ["file=", "message="])
print("Options:", opts)
print("Arguments:", args)

filename = sys.argv[1] if len(sys.argv) > 1 else "default.txt"
message = sys.argv[2] if len(sys.argv) > 2 else "No message provided"
with open(filename, 'w+') as file:
  file.write(message)
  