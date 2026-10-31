# A million numbers: a list vs a generator
import sys

big_list = [n * 2 for n in range(1_000_000)]
big_gen = (n * 2 for n in range(1_000_000))
print(sys.getsizeof(big_list))
print(sys.getsizeof(big_gen))
print(sum(big_gen))
