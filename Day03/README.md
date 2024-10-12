# Intro to Python: Package management and virtual environment


### Exercise 00 : Virtual Environment

* create a virtual environment with your nickname as its name using Python 3 (you
will work with this env here and further on),
* activate it,
* run Python 3 from the terminal,
* print the virtual env name using os library,
* write a small python script that does that thing by calling it in command-line:
    ```
    $ ./venv.py
    Your current virtual env is /Users/McShtuder/shtuder
    ```
* deactivate the environment,
* run the script again ...

If you got a KeyError or an exception when deactivated the env, consider why it happened.
You do not have to fix it in this exercise, but be ready to explain why it happened.

### Exercise 01 : Installing a package

* Let us install the first package in your virtual environment!
* We will work with the library termgraph a bit. It gives you the power to draw
graphs and diagrams right in your terminal. What could be cooler?
* Install the library in the virtual environment created in the previous exercise.
* Make the visualization 
(create a file for the visualization by yourself):
* Make a shell script file for this purpose with the name pies_bars.sh. It contains
only the part for making the graph without activation and deactivation of the env.

### Exercise 02 : Installing many libraries

Write a python script called librarian.py that:

* checks that it runs inside the correct env
* installs the libraries
* displays all the installed libraries at the end like this (doesn’t have to be exactly the same
list):

    ```
    six==1.14.0
    soupsieve==2.0
    termgraph==0.2.0
    wcwidth==0.1.9
    zipp==3.1.0
    ```
* saves it to requirements.txt

Put an archive of your env in the folder. You can put archivation in your code or you
can do it from the command line. The archive may be compressed if you think that would
be useful. If the script was called from the wrong env, there should be an exception.

### Exercise 03 : Very beautiful soup

In this exercise, you will parse Yahoo Finance (yeah, it has an API, but for learning
purposes let us forget about that). You will need to visit a [page like this](https://finance.yahoo.com/quote/msft/financials?p=msft) and get some
data for a specific field of a specific company.

Write a Python script that:

* gets: as the arguments the ticker symbol and the field of the table (for example,
MSFT, Total Revenue)
* returns: the tuple that contains the requested information
* special conditions: add a ’sleep for 5 seconds’ inside your script (we will need it
later)

The example:
```
$ ./financial.py 'MSFT' 'Total Revenue'
('Total Revenue', '134,249,000', '125,843,000', '110,360,000',
'89,950,000', '85,320,000')
```

If the URL does not exist, raise an exception. If the requested field does not exist,
raise an exception.

### Exercise 04 : Profiling

* Applying cProfile to your script financial.py, get a table of the functions used sorted
in descending order by total time spent on their execution. Save it to the file profiling-
sleep.txt.
* Delete the line with time.sleep(5) from your script and run the profiling again.
You should get a new table without built-in method time.sleep. Save it to the file
profiling-tottime.txt
* Try using another HTTP-client library to see if your script got any faster. Save the new
script to financial_enhanced.py. Save the result of the profiling to the file profiling-http.txt
* Get the same table but sorted in descendingly order by number of calls. Sometimes it is
useful to know: that you can choose to optimize those functions to make them call fewer
times. Save the table to the file profiling-ncalls.txt
* This time use the library pstats. Sort by cumulative time and get the top 5 Save it to the file
pstats-cumulative.txt


### Exercise 05 : PyTest

For each of the functions,
you need to create at least 3 tests using the library PyTest. Check if your script gives
the correct information for the request:

* If I ask for Total Revenue, do I get the total revenue for the given ticker?
* Is the type of the return a tuple?
* If I give an invalid ticker name, do I get an exception?

Modify your script financial.py by adding the tests into the code. Put the file in your
directory with the name financial_test.py. Run PyTest. Your tests should have passed.
If not, work on your script to make it ready.
