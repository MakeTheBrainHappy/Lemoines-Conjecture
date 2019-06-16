"""
Description: Lemoine's Conjecture implemented with numpy speedups
"""

import numpy as np
import time
from sympy import prime
from sympy import sieve,primerange 

def primesfrom2to(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

#def lemoinesConjecture(batch):
   # while(len(batch) != 0):
        #print()
        
def main():
    start_time = time.time()
    
    l = primesfrom2to(100000)
    
    nums = range(5,100000,2)
    
    print("--- %s seconds ---" % (time.time() - start_time))
    
    batch_size = 2000
    
    i = 0
    
    while i < len(nums):
        batch = nums[i:i+batch_size]
        #lemoinesConjecture(batch)
        i += batch_size
    
    #l = primerange(1,100000)
    #while (n < 100000):
       #if(n - 2*prime(x) in l):
       #     n = n+2    
       #     x = 1
      #  x = x + 1

    print("--- %s seconds ---" % (time.time() - start_time))
    
    
main()