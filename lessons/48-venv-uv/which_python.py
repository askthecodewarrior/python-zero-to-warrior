# Which Python is running this file?
import sys

print(sys.prefix)
print("In a venv:", sys.prefix != sys.base_prefix)
