from stopwatch import Stopwatch


class firstn(object):
  def __init__(self, n):
    self.n = n
    self.num = 0 #    self.num, self.nums = 0, []

  def __iter__(self):
    return self

  def next(self):
    if self.num < self.n:
      cur, self.num = self.num, self.num+1
      return cur
    else:
      raise StopIteration()


      
s = Stopwatch()
sum_of_first_n = sum(firstn(10000000))
duration = s.duration()
print "sum:",sum_of_first_n
print "duration:",duration