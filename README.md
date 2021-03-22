# Mibolsillo Challenge

###### For confidential purposes, the direct question link shouldn't be posted


### Concept

The overall concept of this challenge is to find a path, (more like a route) to help people find their way along a local road, given a graph entry(something like a roadmap). For example:

Imagine given a plot of a geographical area as graph entries:
AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7

where A, B, C e.t.c. represent a certain point(let's say a cafe or bus-stop, e.t.c.) and together i.e AB, BC, CD represents paths (i.e from cafe to bus-stop). and the numbers beside the path represent the distance. So all together, we could say:

if A = Mckenzie's cafe, B = Ino's flower shop. Then AB5 tells us: From Mckenzie's cafe to Ino's flower shop (imagine a scale 1 to 100m) is about 500m away and this helps people trying to locate the flower shop from the cafe to know how far they must go.

So far, that is the general concept behind this challenge.


### Deep-Dive

Now let's delve into the project thoroughly:
There were 4 major path finding functions, which are (as used in the code):

findstandardpath(): This function helps to check if certain lists of path are possible, if they are, their total distance is returned, else, "NO SUCH ROUTE" is returned. Two parameters are technically needed for this function to run i.e the paths to be followed and the graph entry.

findtripstoandfroapath(): This function helps to return number of different ways to and fro a given path with either the exact number of times the person would need to make a stop on some place(s) or with the maximum number of stop on some place(s) i.e i.e combination of different paths to take to a certain place given the highest or exact number of possible times one can make a stop. Three parameters, actually 4 are needed: The place to start and the place to end: e.g "A B", graph entries: AB5, BC4..., if a maximum stop is needed then it should be greater than 0 i.e 1,2,3 while the exact number param is set to 0 else the maximum is set as 0 and exact is set greater than 1

findshortestpath(): For a given start and stop point, This function helps to compute the shortest distance attainable from the various paths available: params needed: The start and end point: e.g "A B", graph entries.

finddifferentpaths(): Within a set number of distance, the function computes a number of list of paths that can be followed. params needed: The start and end point: e.g "A B", graph entries: AB5, BC4..., maximum distance attainable by the list of paths


### How to run
```sh

git clone https://github.com/adewolejosh/MiBolsillo-IT-challenge.git/
cd MiBolsillo-IT-challenge/
# this is to run the given parameters in the challenge
python test.py
# for a unit test in python, run
python unit_test.py
```
To test functions, head over to test.py in you favorite code editor, comment out the block of code "My test" or you can simply delete the block and put in a function you'd like to test. Remember to give it its parameters for it to run smoothly


### Author
Joshua Adewole [Github](https://github.com/adewolejosh)

Special Thanks to Julio and the team at MiBolsillo for this challenge!



#### Unofficial and Kind of Unrelated Block: Should/Could be Ignored!!!

After consulting some research, I found out quite a number of folks consider each node(path) in each process and for me, I was like why do you consider a node why not the path way, this kind of added to my thought process when writing each block and I really hope this helps someone out there one day but until(and after) then, Love and Light! :)