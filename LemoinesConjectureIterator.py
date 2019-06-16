"""
Description: Lemoine's Conjecture Implemented with Python Iterators 
"""

import time
import numpy as np
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

def main():
    start_time = time.time()
    k = primesfrom2to(10000000)
    p = set(k)
    l = np.nditer(k)
    print("--- %s seconds ---" % (time.time() - start_time))            

    n = 7
    while (n < 10000000):
       if(n - 2*l.next() in p):
           n = n+2  
           l.reset()
    print("--- %s seconds ---" % (time.time() - start_time))            

    
main()
