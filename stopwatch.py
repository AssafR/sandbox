"""\
Stopwatch - a convenience class for timing things.

>> s = Stopwatch()
>> ... # do something you want timed
>> duration = s.duration()
"""

from datetime import datetime

class Stopwatch(object):
    def __init__(self):
        self.time = datetime.now()
     
    def duration(self):
        timediff = datetime.now() - self.time
        micro = timediff.microseconds / 1000000.0
        #print "Diff is:",str(timediff)," microseconds=",micro
        return micro
