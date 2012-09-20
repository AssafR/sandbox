# a generator that yields items instead of returning a list
from stopwatch import Stopwatch

def firstn(n):
  num = 0
  while num < n:
    yield num
    num += 1


s = Stopwatch()
sum_of_first_n = sum(firstn(10000000))
duration = s.duration()
print "sum:",sum_of_first_n
print "duration:",duration