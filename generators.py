def with_index(itr):
    """This is the same as builtin function enumerate. Don't use this except as an exercise.
       I changed the name, because I don't like overriding builtin names.
       
       Produces an iterable which returns pairs (i,x) where x is the value of the original,
       and i is its index in the iteration, starting from 0.
    """
    i=0
    for x in itr:
      yield (i,x)
      i = i+1
    #TODO

      
    
        
def fibonacci():
    """An infinite generator for the fibonacci series, where:
       Fib[0] = 0
       Fib[1] = 1
       Fib[n+2] = Fib[n] + Fib[n+1]
    """
    prev=0
    curr=1
    while True:
      yield prev
      (prev,curr) = (curr,prev+curr)
      
    
def product(*seqs):
    """Same as itertools.product - Don't use this except as an exercise.
       Returns a generator for the cartesian product of all sequences given as input. 
       If called with N sequences, then each returned item is a list of N items - one from each sequence.
       For example, product([1,2,3],'ABC',[True,False]) produces the following items:
           [1,'A',True]
           [1,'A',False]
           [1,'B',True]
           ...  
       
       See my blog for discussion of this implementation: 
       http://www.ronnie-midnight-oil.net/2008/05/ok.html
    """
    #TODO
    if len(seqs)==0:
      yield []
    elif len(seqs)==1:
      for elem in seqs[0]:
        yield [elem]
    else:
        for elem in seqs[0]:
#            print "elem=",elem,"\n"
#            print "calling recurse with:",seqs[1:]
            for prod in product(*seqs[1:]):
#                  print "returned prod=",prod,",concatente with:",elem
                  result = [elem] + prod
#                  print "returning: result=",result
                  yield  result
        


#for (i,t) in with_index(range(2,8)):
#  print "i=",i,"t=",t

#for i in fibonacci():
#  print i
#  if i>400:
#    break


#lst = list(product([1,2,3],'XY'))
lst=list(product([1,2,3],'XY',[True,False],['well','now']))
#lst=list(product())
#print "lst=",lst

#product([1,2,3],'ABC',[True,False])
