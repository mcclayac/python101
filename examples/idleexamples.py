Python 2.7.6 (default, Sep  9 2014, 15:04:36) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> random.randint(0, 5)
1
>>> random.choice9[1,3,5,7,9])
SyntaxError: invalid syntax
>>> random.choice([1.3.5.7.9])
SyntaxError: invalid syntax
>>> random.choice([1, 3, 5, 7, 9])
1
>>> random.choice([1, 3, 5, 7, 9])
9
>>> random,random()

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    random,random()
TypeError: 'module' object is not callable
>>> random.random()
0.5290582054438404
>>> hel(random)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    hel(random)
NameError: name 'hel' is not defined
>>> help(random)
Help on module random:

NAME
    random - Random variable generators.

FILE
    /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.py

MODULE DOCS
    http://docs.python.org/library/random

DESCRIPTION
        integers
        --------
               uniform within range
    
        sequences
        ---------
               pick random element
               pick random sample
               generate random permutation
    
        distributions on the real line:
        ------------------------------
               uniform
               triangular
               normal (Gaussian)
               lognormal
               negative exponential
               gamma
               beta
               pareto
               Weibull
    
        distributions on the circle (angles 0 to 2pi)
        ---------------------------------------------
               circular uniform
               von Mises
    
    General notes on the underlying Mersenne Twister core generator:
    
    * The period is 2**19937-1.
    * It is one of the most extensively tested generators in existence.
    * Without a direct way to compute N steps forward, the semantics of
      jumpahead(n) are weakened to simply jump to another distant state and rely
      on the large period to avoid overlapping sequences.
    * The random() method is implemented in C, executes in a single Python step,
      and is, therefore, threadsafe.

CLASSES
    _random.Random(__builtin__.object)
        Random
            SystemRandom
            WichmannHill
    
    class Random(_random.Random)
     |  Random number generator base class used by bound module functions.
     |  
     |  Used to instantiate instances of Random to get generators that don't
     |  share state.  Especially useful for multi-threaded programs, creating
     |  a different instance of Random for each thread, and using the jumpahead()
     |  method to ensure that the generated sequences seen by each thread don't
     |  overlap.
     |  
     |  Class Random can also be subclassed if you want to use a different basic
     |  generator of your own devising: in that case, override the following
     |  methods: random(), seed(), getstate(), setstate() and jumpahead().
     |  Optionally, implement a getrandbits() method so that randrange() can cover
     |  arbitrarily large ranges.
     |  
     |  Method resolution order:
     |      Random
     |      _random.Random
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __getstate__(self)
     |  
     |  __init__(self, x=None)
     |      Initialize an instance.
     |      
     |      Optional argument x controls seeding, as for Random.seed().
     |  
     |  __reduce__(self)
     |  
     |  __setstate__(self, state)
     |  
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |  
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |  
     |  expovariate(self, lambd)
     |      Exponential distribution.
     |      
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |  
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      
     |      The probability distribution function is:
     |      
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |  
     |  gauss(self, mu, sigma)
     |      Gaussian distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |      
     |      Not thread-safe without a lock around calls.
     |  
     |  getstate(self)
     |      Return internal state; can be passed to setstate() later.
     |  
     |  jumpahead(self, n)
     |      Change the internal state to one that is likely far away
     |      from the current state.  This method will not be in Py3.x,
     |      so it is better to simply reseed.
     |  
     |  lognormvariate(self, mu, sigma)
     |      Log normal distribution.
     |      
     |      If you take the natural logarithm of this distribution, you'll get a
     |      normal distribution with mean mu and standard deviation sigma.
     |      mu can have any value, and sigma must be greater than zero.
     |  
     |  normalvariate(self, mu, sigma)
     |      Normal distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.
     |  
     |  paretovariate(self, alpha)
     |      Pareto distribution.  alpha is the shape parameter.
     |  
     |  randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
     |  
     |  randrange(self, start, stop=None, step=1, _int=<type 'int'>, _maxwidth=9007199254740992L)
     |      Choose a random item from range(start, stop[, step]).
     |      
     |      This fixes the problem with randint() which includes the
     |      endpoint; in Python this is usually not what you want.
     |  
     |  sample(self, population, k)
     |      Chooses k unique random elements from a population sequence.
     |      
     |      Returns a new list containing elements from the population while
     |      leaving the original population unchanged.  The resulting list is
     |      in selection order so that all sub-slices will also be valid random
     |      samples.  This allows raffle winners (the sample) to be partitioned
     |      into grand prize and second place winners (the subslices).
     |      
     |      Members of the population need not be hashable or unique.  If the
     |      population contains repeats, then each occurrence is a possible
     |      selection in the sample.
     |      
     |      To choose a sample in a range of integers, use xrange as an argument.
     |      This is especially fast and space efficient for sampling from a
     |      large population:   sample(xrange(10000000), 60)
     |  
     |  seed(self, a=None)
     |      Initialize internal state from hashable object.
     |      
     |      None or no argument seeds from current time or from an operating
     |      system specific randomness source if available.
     |      
     |      If a is not None or an int or long, hash(a) is used instead.
     |  
     |  setstate(self, state)
     |      Restore internal state from object returned by getstate().
     |  
     |  shuffle(self, x, random=None)
     |      x, random=random.random -> shuffle list x in place; return None.
     |      
     |      Optional arg random is a 0-argument function returning a random
     |      float in [0.0, 1.0); by default, the standard random.random.
     |  
     |  triangular(self, low=0.0, high=1.0, mode=None)
     |      Triangular distribution.
     |      
     |      Continuous distribution bounded by given lower and upper limits,
     |      and having a given mode value in-between.
     |      
     |      http://en.wikipedia.org/wiki/Triangular_distribution
     |  
     |  uniform(self, a, b)
     |      Get a random number in the range [a, b) or [a, b] depending on rounding.
     |  
     |  vonmisesvariate(self, mu, kappa)
     |      Circular data distribution.
     |      
     |      mu is the mean angle, expressed in radians between 0 and 2*pi, and
     |      kappa is the concentration parameter, which must be greater than or
     |      equal to zero.  If kappa is equal to zero, this distribution reduces
     |      to a uniform random angle over the range 0 to 2*pi.
     |  
     |  weibullvariate(self, alpha, beta)
     |      Weibull distribution.
     |      
     |      alpha is the scale parameter and beta is the shape parameter.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  VERSION = 3
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _random.Random:
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  getrandbits(...)
     |      getrandbits(k) -> x.  Generates a long int with k random bits.
     |  
     |  random(...)
     |      random() -> x in the interval [0, 1).
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from _random.Random:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class SystemRandom(Random)
     |  Alternate random number generator using sources provided
     |  by the operating system (such as /dev/urandom on Unix or
     |  CryptGenRandom on Windows).
     |  
     |   Not available on all systems (see os.urandom() for details).
     |  
     |  Method resolution order:
     |      SystemRandom
     |      Random
     |      _random.Random
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  getrandbits(self, k)
     |      getrandbits(k) -> x.  Generates a long int with k random bits.
     |  
     |  getstate = _notimplemented(self, *args, **kwds)
     |  
     |  jumpahead = _stub(self, *args, **kwds)
     |  
     |  random(self)
     |      Get the next random number in the range [0.0, 1.0).
     |  
     |  seed = _stub(self, *args, **kwds)
     |  
     |  setstate = _notimplemented(self, *args, **kwds)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Random:
     |  
     |  __getstate__(self)
     |  
     |  __init__(self, x=None)
     |      Initialize an instance.
     |      
     |      Optional argument x controls seeding, as for Random.seed().
     |  
     |  __reduce__(self)
     |  
     |  __setstate__(self, state)
     |  
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |  
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |  
     |  expovariate(self, lambd)
     |      Exponential distribution.
     |      
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |  
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      
     |      The probability distribution function is:
     |      
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |  
     |  gauss(self, mu, sigma)
     |      Gaussian distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |      
     |      Not thread-safe without a lock around calls.
     |  
     |  lognormvariate(self, mu, sigma)
     |      Log normal distribution.
     |      
     |      If you take the natural logarithm of this distribution, you'll get a
     |      normal distribution with mean mu and standard deviation sigma.
     |      mu can have any value, and sigma must be greater than zero.
     |  
     |  normalvariate(self, mu, sigma)
     |      Normal distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.
     |  
     |  paretovariate(self, alpha)
     |      Pareto distribution.  alpha is the shape parameter.
     |  
     |  randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
     |  
     |  randrange(self, start, stop=None, step=1, _int=<type 'int'>, _maxwidth=9007199254740992L)
     |      Choose a random item from range(start, stop[, step]).
     |      
     |      This fixes the problem with randint() which includes the
     |      endpoint; in Python this is usually not what you want.
     |  
     |  sample(self, population, k)
     |      Chooses k unique random elements from a population sequence.
     |      
     |      Returns a new list containing elements from the population while
     |      leaving the original population unchanged.  The resulting list is
     |      in selection order so that all sub-slices will also be valid random
     |      samples.  This allows raffle winners (the sample) to be partitioned
     |      into grand prize and second place winners (the subslices).
     |      
     |      Members of the population need not be hashable or unique.  If the
     |      population contains repeats, then each occurrence is a possible
     |      selection in the sample.
     |      
     |      To choose a sample in a range of integers, use xrange as an argument.
     |      This is especially fast and space efficient for sampling from a
     |      large population:   sample(xrange(10000000), 60)
     |  
     |  shuffle(self, x, random=None)
     |      x, random=random.random -> shuffle list x in place; return None.
     |      
     |      Optional arg random is a 0-argument function returning a random
     |      float in [0.0, 1.0); by default, the standard random.random.
     |  
     |  triangular(self, low=0.0, high=1.0, mode=None)
     |      Triangular distribution.
     |      
     |      Continuous distribution bounded by given lower and upper limits,
     |      and having a given mode value in-between.
     |      
     |      http://en.wikipedia.org/wiki/Triangular_distribution
     |  
     |  uniform(self, a, b)
     |      Get a random number in the range [a, b) or [a, b] depending on rounding.
     |  
     |  vonmisesvariate(self, mu, kappa)
     |      Circular data distribution.
     |      
     |      mu is the mean angle, expressed in radians between 0 and 2*pi, and
     |      kappa is the concentration parameter, which must be greater than or
     |      equal to zero.  If kappa is equal to zero, this distribution reduces
     |      to a uniform random angle over the range 0 to 2*pi.
     |  
     |  weibullvariate(self, alpha, beta)
     |      Weibull distribution.
     |      
     |      alpha is the scale parameter and beta is the shape parameter.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Random:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from Random:
     |  
     |  VERSION = 3
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _random.Random:
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from _random.Random:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class WichmannHill(Random)
     |  Method resolution order:
     |      WichmannHill
     |      Random
     |      _random.Random
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  getstate(self)
     |      Return internal state; can be passed to setstate() later.
     |  
     |  jumpahead(self, n)
     |      Act as if n calls to random() were made, but quickly.
     |      
     |      n is an int, greater than or equal to 0.
     |      
     |      Example use:  If you have 2 threads and know that each will
     |      consume no more than a million random numbers, create two Random
     |      objects r1 and r2, then do
     |          r2.setstate(r1.getstate())
     |          r2.jumpahead(1000000)
     |      Then r1 and r2 will use guaranteed-disjoint segments of the full
     |      period.
     |  
     |  random(self)
     |      Get the next random number in the range [0.0, 1.0).
     |  
     |  seed(self, a=None)
     |      Initialize internal state from hashable object.
     |      
     |      None or no argument seeds from current time or from an operating
     |      system specific randomness source if available.
     |      
     |      If a is not None or an int or long, hash(a) is used instead.
     |      
     |      If a is an int or long, a is used directly.  Distinct values between
     |      0 and 27814431486575L inclusive are guaranteed to yield distinct
     |      internal states (this guarantee is specific to the default
     |      Wichmann-Hill generator).
     |  
     |  setstate(self, state)
     |      Restore internal state from object returned by getstate().
     |  
     |  whseed(self, a=None)
     |      Seed from hashable object's hash code.
     |      
     |      None or no argument seeds from current time.  It is not guaranteed
     |      that objects with distinct hash codes lead to distinct internal
     |      states.
     |      
     |      This is obsolete, provided for compatibility with the seed routine
     |      used prior to Python 2.1.  Use the .seed() method instead.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  VERSION = 1
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Random:
     |  
     |  __getstate__(self)
     |  
     |  __init__(self, x=None)
     |      Initialize an instance.
     |      
     |      Optional argument x controls seeding, as for Random.seed().
     |  
     |  __reduce__(self)
     |  
     |  __setstate__(self, state)
     |  
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |  
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |  
     |  expovariate(self, lambd)
     |      Exponential distribution.
     |      
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |  
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      
     |      The probability distribution function is:
     |      
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |  
     |  gauss(self, mu, sigma)
     |      Gaussian distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |      
     |      Not thread-safe without a lock around calls.
     |  
     |  lognormvariate(self, mu, sigma)
     |      Log normal distribution.
     |      
     |      If you take the natural logarithm of this distribution, you'll get a
     |      normal distribution with mean mu and standard deviation sigma.
     |      mu can have any value, and sigma must be greater than zero.
     |  
     |  normalvariate(self, mu, sigma)
     |      Normal distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.
     |  
     |  paretovariate(self, alpha)
     |      Pareto distribution.  alpha is the shape parameter.
     |  
     |  randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
     |  
     |  randrange(self, start, stop=None, step=1, _int=<type 'int'>, _maxwidth=9007199254740992L)
     |      Choose a random item from range(start, stop[, step]).
     |      
     |      This fixes the problem with randint() which includes the
     |      endpoint; in Python this is usually not what you want.
     |  
     |  sample(self, population, k)
     |      Chooses k unique random elements from a population sequence.
     |      
     |      Returns a new list containing elements from the population while
     |      leaving the original population unchanged.  The resulting list is
     |      in selection order so that all sub-slices will also be valid random
     |      samples.  This allows raffle winners (the sample) to be partitioned
     |      into grand prize and second place winners (the subslices).
     |      
     |      Members of the population need not be hashable or unique.  If the
     |      population contains repeats, then each occurrence is a possible
     |      selection in the sample.
     |      
     |      To choose a sample in a range of integers, use xrange as an argument.
     |      This is especially fast and space efficient for sampling from a
     |      large population:   sample(xrange(10000000), 60)
     |  
     |  shuffle(self, x, random=None)
     |      x, random=random.random -> shuffle list x in place; return None.
     |      
     |      Optional arg random is a 0-argument function returning a random
     |      float in [0.0, 1.0); by default, the standard random.random.
     |  
     |  triangular(self, low=0.0, high=1.0, mode=None)
     |      Triangular distribution.
     |      
     |      Continuous distribution bounded by given lower and upper limits,
     |      and having a given mode value in-between.
     |      
     |      http://en.wikipedia.org/wiki/Triangular_distribution
     |  
     |  uniform(self, a, b)
     |      Get a random number in the range [a, b) or [a, b] depending on rounding.
     |  
     |  vonmisesvariate(self, mu, kappa)
     |      Circular data distribution.
     |      
     |      mu is the mean angle, expressed in radians between 0 and 2*pi, and
     |      kappa is the concentration parameter, which must be greater than or
     |      equal to zero.  If kappa is equal to zero, this distribution reduces
     |      to a uniform random angle over the range 0 to 2*pi.
     |  
     |  weibullvariate(self, alpha, beta)
     |      Weibull distribution.
     |      
     |      alpha is the scale parameter and beta is the shape parameter.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Random:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _random.Random:
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  getrandbits(...)
     |      getrandbits(k) -> x.  Generates a long int with k random bits.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from _random.Random:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T

FUNCTIONS
    betavariate(self, alpha, beta) method of Random instance
        Beta distribution.
        
        Conditions on the parameters are alpha > 0 and beta > 0.
        Returned values range between 0 and 1.
    
    choice(self, seq) method of Random instance
        Choose a random element from a non-empty sequence.
    
    expovariate(self, lambd) method of Random instance
        Exponential distribution.
        
        lambd is 1.0 divided by the desired mean.  It should be
        nonzero.  (The parameter would be called "lambda", but that is
        a reserved word in Python.)  Returned values range from 0 to
        positive infinity if lambd is positive, and from negative
        infinity to 0 if lambd is negative.
    
    gammavariate(self, alpha, beta) method of Random instance
        Gamma distribution.  Not the gamma function!
        
        Conditions on the parameters are alpha > 0 and beta > 0.
        
        The probability distribution function is:
        
                    x ** (alpha - 1) * math.exp(-x / beta)
          pdf(x) =  --------------------------------------
                      math.gamma(alpha) * beta ** alpha
    
    gauss(self, mu, sigma) method of Random instance
        Gaussian distribution.
        
        mu is the mean, and sigma is the standard deviation.  This is
        slightly faster than the normalvariate() function.
        
        Not thread-safe without a lock around calls.
    
    getrandbits(...)
        getrandbits(k) -> x.  Generates a long int with k random bits.
    
    getstate(self) method of Random instance
        Return internal state; can be passed to setstate() later.
    
    jumpahead(self, n) method of Random instance
        Change the internal state to one that is likely far away
        from the current state.  This method will not be in Py3.x,
        so it is better to simply reseed.
    
    lognormvariate(self, mu, sigma) method of Random instance
        Log normal distribution.
        
        If you take the natural logarithm of this distribution, you'll get a
        normal distribution with mean mu and standard deviation sigma.
        mu can have any value, and sigma must be greater than zero.
    
    normalvariate(self, mu, sigma) method of Random instance
        Normal distribution.
        
        mu is the mean, and sigma is the standard deviation.
    
    paretovariate(self, alpha) method of Random instance
        Pareto distribution.  alpha is the shape parameter.
    
    randint(self, a, b) method of Random instance
        Return random integer in range [a, b], including both end points.
    
    random(...)
        random() -> x in the interval [0, 1).
    
    randrange(self, start, stop=None, step=1, _int=<type 'int'>, _maxwidth=9007199254740992L) method of Random instance
        Choose a random item from range(start, stop[, step]).
        
        This fixes the problem with randint() which includes the
        endpoint; in Python this is usually not what you want.
    
    sample(self, population, k) method of Random instance
        Chooses k unique random elements from a population sequence.
        
        Returns a new list containing elements from the population while
        leaving the original population unchanged.  The resulting list is
        in selection order so that all sub-slices will also be valid random
        samples.  This allows raffle winners (the sample) to be partitioned
        into grand prize and second place winners (the subslices).
        
        Members of the population need not be hashable or unique.  If the
        population contains repeats, then each occurrence is a possible
        selection in the sample.
        
        To choose a sample in a range of integers, use xrange as an argument.
        This is especially fast and space efficient for sampling from a
        large population:   sample(xrange(10000000), 60)
    
    seed(self, a=None) method of Random instance
        Initialize internal state from hashable object.
        
        None or no argument seeds from current time or from an operating
        system specific randomness source if available.
        
        If a is not None or an int or long, hash(a) is used instead.
    
    setstate(self, state) method of Random instance
        Restore internal state from object returned by getstate().
    
    shuffle(self, x, random=None) method of Random instance
        x, random=random.random -> shuffle list x in place; return None.
        
        Optional arg random is a 0-argument function returning a random
        float in [0.0, 1.0); by default, the standard random.random.
    
    triangular(self, low=0.0, high=1.0, mode=None) method of Random instance
        Triangular distribution.
        
        Continuous distribution bounded by given lower and upper limits,
        and having a given mode value in-between.
        
        http://en.wikipedia.org/wiki/Triangular_distribution
    
    uniform(self, a, b) method of Random instance
        Get a random number in the range [a, b) or [a, b] depending on rounding.
    
    vonmisesvariate(self, mu, kappa) method of Random instance
        Circular data distribution.
        
        mu is the mean angle, expressed in radians between 0 and 2*pi, and
        kappa is the concentration parameter, which must be greater than or
        equal to zero.  If kappa is equal to zero, this distribution reduces
        to a uniform random angle over the range 0 to 2*pi.
    
    weibullvariate(self, alpha, beta) method of Random instance
        Weibull distribution.
        
        alpha is the scale parameter and beta is the shape parameter.

DATA
    __all__ = ['Random', 'seed', 'random', 'uniform', 'randint', 'choice',...


>>> q

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    q
NameError: name 'q' is not defined
>>> 
>>> 
>>> 
>>> 
>>> from datetime import time
>>> lunch - time(hour=11, minute=30)

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    lunch - time(hour=11, minute=30)
NameError: name 'lunch' is not defined
>>> lunch = time(hour=11, minute=30)
>>> lunch.hour
11
>>> snack = time(hour=14)
>>> lunch < snack
True
>>> data = []
>>> if data:
	print('data has elements'
else:
	      
SyntaxError: invalid syntax
>>> if data:
	print('data has elements')
else:
	print('Data is empty')

	
Data is empty
>>> if len(data) > 0:
	print('data has stuff')
else:
	print('data is empty')

	
data is empty
>>> dir(data)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> isinstance(data, list)
True
>>> 
>>> isinstance(data, int)
False
>>> type(data)
<type 'list'>
>>> 1 + 2
3
>>> 5 % 2
1
>>> 2 **3
8
>>> 1 / 2
0
>>> 1 / 2.0
0.5
>>> 1.0//2.0
0.0
>>> 1/2
0
>>> float(1)
1.0
>>> s = 'Python'
>>> s * 2
'PythonPython'
>>> s *= 2
>>> s
'PythonPython'
>>> s[2]
't'
>>> s[1]
'y'
>>> s[-1]
'n'
>>> s[:4]
'Pyth'
>>> s[:6] + 'is cool'
'Pythonis cool'
>>> s[:6] + ' is cool'
'Python is cool'
>>> '-' * 20
'--------------------'
>>> 'ton' in s
False
>>> thon in s

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    thon in s
NameError: name 'thon' is not defined
>>> 'thon' in s
True
>>> hi = '''hi
there!'''
>>> hi
'hi\nthere!'
>>> print hi
hi
there!
>>> "name: %s, age %d" % ('Tony', 45)
'name: Tony, age 45'
>>> strexample = 
"name: %s, age %d" % ('Tony', 45)
SyntaxError: invalid syntax
>>> strexample = "name: %s, age %d" % ('Tony', 45)
>>> strexample
'name: Tony, age 45'
>>> "name: {0}, age: {1}".format('Kevin', 33)
'name: Kevin, age: 33'
>>> strexample2 = "name: {0}, age: {1}".format('Kevin', 33)
>>> print strexample2
name: Kevin, age: 33
>>> d = {'user': 'wes', 'page' : 42 }
>>> 'http://web/%(user)s/%(page)d.html' % d
'http://web/wes/42.html'
>>> 'http://web/%(user)/%(page).html'.format(**d)
'http://web/%(user)/%(page).html'
>>> 
>>> 
>>> s = "Python is cool."
>>> s.find('is not')
-1
>>> s.find('is ')
7
>>> s.rfind('o')
12
>>> s.center(25)
'     Python is cool.     '
>>> s.center(25).strip()
'Python is cool.'
>>> s.split()
['Python', 'is', 'cool.']
>>> '::'.join(s.split())
'Python::is::cool.'
>>> '.'.join(reversed(s.split()))
'cool..is.Python'
>>> 
>>> 
>>> m = ['Code', 'Program', 9, 2006]
>>> m
['Code', 'Program', 9, 2006]
>>> m.append('Prentice Hall')
>>> m
['Code', 'Program', 9, 2006, 'Prentice Hall']
>>> m.insert(1, Python')
	 
SyntaxError: EOL while scanning string literal
>>> m.insert(1, 'Python')
>>> m
['Code', 'Python', 'Program', 9, 2006, 'Prentice Hall']
>>> 2006 in m
True
>>> m.pop(3)
9
>>> m
['Code', 'Python', 'Program', 2006, 'Prentice Hall']
>>> m[2:4] = ['Fundamentals', 2008
	  ]
>>> m
['Code', 'Python', 'Fundamentals', 2008, 'Prentice Hall']
>>> m.remove('Code')
>>> m
['Python', 'Fundamentals', 2008, 'Prentice Hall']
>>> 
