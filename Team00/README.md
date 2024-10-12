# MovieLens Analytics


### Mandatory part

In this rush, you are going to work on your own analytical report. You will
analyze data from the MovieLens database. By the end of the rush, you will
have two files:

```movielens_analysis.py``` and ```movielens_report.ipynb```. In the first file, you will
need to create your own module with classes and methods. In the second file,
you will create the report itself using only your module.

#### Module

Remember that the goal of the rush is to strengthen your skills.

Try to use as much as you can from what you have learned from the previous days.

* Use a smaller version of MovieLens dataset, [download](https://drive.google.com/file/d/1CwC887F6FMneXea2yCpDrlrf47Em664u/view?usp=sharing) it, please
* Read the README.txt very carefully. Focus on the file structures
* In your module, you will need to create 4 classes corresponding to 4 files from the
data and 1 class for testing
* The classes and methods below are obligatory but you can add to them anything
that suits your needs 

*Classes Ratings, Tags, Movies, Links can be found in code-samples.*

Class Tests:

Create tests using PyTest for each and every method of the classes above.

They should check:

* if the methods return the correct data types
* if the lists elements have the correct data types
* if the returned data sorted correctly

Run the tests before going to the next stage of the rush.

#### Report

Using only the classes and methods from movielens_analysis.py,
prepare your report.

You should do it in Jupyter Notebook.

It is a great tool especially if you are a data scientist.

It gives you an opportunity to work with the code interactively
by launching and relaunching different cells with different values.

You do not have to rerun your whole code from the beginning.

Also, you can put in the cells not only code but text too,
which is a great feature for making reports.

Install it to your environment.


In this part of the rush, we will give you more freedom.

We are not going to define the structure of your report.

The goal of the report is to tell us an interesting story
about the MovieLens dataset.

Find the good structure and the right sequence.

The only constraints:

* you must use each and every method from movielens_analysis.py except class Tests
* every cell in your notebook should contain magic command %timeit
* all other imports are prohibited as well as using built-in functions. If you need
them, put them in your module in advance


### Bonus part

* Add to the classes more methods that you may find useful and interesting for your
report. Do not forget to test them too
* Improve the tests. Check the correctness of your calculations as well. Precalculate
manually some results and metrics and check if the methods return the correct
information if you give them the specific input