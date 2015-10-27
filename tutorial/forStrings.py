Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> 
>>> 
>>> for i in range(1,10,2):
	print(i)

	
1
3
5
7
9
>>> data = ['zero', 'one', 'two', 'three']
>>> for i in range(len(data)):
	print(i , ' - ', data[i])

	
0  -  zero
1  -  one
2  -  two
3  -  three
>>> 
>>> music = ['Poe', 'Gaudi', 'Freud']
>>> for i in range(len(music)):
	s = 'album {}:  {}'
	print(s.format(i, music[i]))

	
album 0:  Poe
album 1:  Gaudi
album 2:  Freud
>>> 
