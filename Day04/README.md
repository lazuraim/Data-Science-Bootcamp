# Intro to Python: Efficient code practices

### Exercise 00 : List comprehensions

* write two functions:
  * in the first you need to implement the usual approach with a loop and an
  append
  * in the second you use a list comprehension instead
* use timeit to measure the time required to run those functions 90, 000, 000 times
and compare them
* put this into a script that prints “it is better to use a list comprehension” if the
corresponding time is less or equal than that of the loop, and “it is better to use a
loop” if not,
* also, add the time values at the end, after the print described above. Order them
from shortest to longest.

Please, use the following list of email addresses: 
```
emails = [’john@gmail.com’, ’james@gmail.com’, ’alice@yahoo.com’, 
’anna@live.com’, ’philipp@gmail.com’]
```

Duplicate the values 5 times. As a result, the list will contain 25 elements, but only 5 unique
ones.

An example of the script being launched:

```
$ ./benchmark.py
it is better to use a list comprehension
55.71611063099999 vs 58.849982983
```

### Exercise 01 : Map

* Write a function that does the same thing: creates a list with Gmail addresses
taken from the initial list of emails (25 elements), but using a map. Try map() and
list(map()). Note the difference in speed
* You still need to compare which function is faster, but now you have three options:
loop, list comprehension, and map, and add one more phrase according to this in
your code “it is better to use a map” and at the end, you need to display all three
time values with the same condition: they should be in the ascending order by
length.

The example:
```
$ ./benchmark.py
it is better to use a map
29.32016281 vs 54.620376492999995 vs 55.99120069
```

### Exercise 02 : Filter

* Did you notice that what you did in the previous exercises was filtering? Why
not use the corresponding function filter() instead of those list comprehensions and
maps? It works almost the same as map(). You will love it!
* Add a new function to your benchmark that uses filter(). But this time let us
refactor the code. Let us create a script that takes the name of the function (loop,
list comprehension, map, filter) to your benchmark and the number of calls it should
perform for the benchmark. In return, it should give the time spent to make that
number of calls of the function.

The examples:
```
$ ./benchmark.py loop 10000000
6.230267604
$ ./benchmark.py list_comprehension 10000000
6.214286791
$ ./benchmark.py map 10000000
3.063598874
$ ./benchmark.py
```

### Exercise 03 : Reduce

In your script create two functions:

* in the first – you need to implement the usual approach with a loop and ```sum = sum + i*i```
* in the second – you use a reduce() instead

* Let us create a script that takes as an argument the name of the function (loop or
reduce), the number of calls it should perform for the benchmark, and the number for
the sum of the calculation of squares. In return, it should give the time spent to make
that number of calls of the function.

The example:
```
$ ./benchmark.py loop 10000000 5
6.230267604
$ ./benchmark.py reduce 10000000 5
3.063598874
```

### Exercise 04 : Counter

* generate a list with 1 000 000 random values from 0 to 100 (remember list compre-
hensions?)
* write a function that creates a dict out of the list where the keys are the numbers
from 0 to 100 and the values are their counts
* write a function that returns the top 10 most common numbers where the keys are
the numbers and the values are the counts, the input is the list
* solve 2 and 3 using Counter
* make a comparison: your script should display the time spent for 2 and 3 with
Counter and without it

Example:
```
$ ./benchmark.py
my function: 0.4501532
Counter: 0.0432341
my top: 0.1032348
Counter's top: 0.017573
```

### Exercise 05 : Generator

* Download the [MovieLens dataset](http://files.grouplens.org/datasets/movielens/ml-25m.zip).
* Unzip it. You will need the file ratings.csv (678.3 MB is not that big, right?).
* Create the first script, ordinary.py. It should have only one function: it reads all
the file lines into a list and then returns it. In the main program, write a loop that
iterates through the list and calls pass. You should give the path to the file as an
argument to the script
* Create the second script, generator.py. It does exactly the same thing, but in your
function, you must use a generator. It uses the keyword yield to read one line at a
time and returns it to the caller. In the main program, write a loop that iterates
through the generator and calls pass. You should give the path to the file as an
argument to the script.
* Both scripts should display Peak memory usage in GB and User mode time +
System mode time in seconds. If you have Windows OS, use the corresponding
functions to get the same metrics.

Example:
```
$ ./ordinary.py ratings.csv
Peak Memory Usage = 2.114 GB
User Mode Time + System Mode Time = 5.77s
$ ./generator.py ratings.csv
Peak Memory Usage = 0.005 GB
User Mode Time + System Mode Time = 9.04s
```
