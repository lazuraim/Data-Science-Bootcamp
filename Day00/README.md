# UNIX Command Line Tools

Summary: On the first day, we will help you to acquire the skills of using UNIX
command-line tools for basic data science tasks. You will learn how to use curl, sort,
uniq, jq, sed, and cat for data collection and preprocessing.

### Exercise 00 : First shell script


In this exercise, you will need to interact with the HeadHunter API to parse some
information about vacancies. In order to do this, you will need to understand how
both curl and the [HeadHunter API work](https://dev.hh.ru/).

Write a shell script that:

* gets the name of a vacancy - ‘data scientist’ as an argument (some later exercises
will be based on this),
* downloads information about the first 20 vacancies corresponding to the search
parameters,
* stores it in a file with the name hh.json.

The result in the file must be formatted in such a way that each field is placed on a
different line. See the example below:


Your script must be executable. The interpreter to use is /bin/sh.

Put your script as well as your result of parsing in the folder ex00 in the root directory
of your repository.


### Exercise 01 : Transforming JSON to CSV

Write a shell script called json_to_csv.sh that:
* executes jq with a filter written in a separate file filter.jq
* filters the following 5 columns corresponding to the vacancies: “id”, “created_at”,
“name”, “has_test”, and “alternate_url”
* saves the result to the CSV file hh.csv


The CSV file must have headers in the first row.

Your script must be executable. The interpreter to use is /bin/sh.

Put your filter file - the file that converts JSON to CSV, as well as the result of your
conversion in the ex01 folder in the root directory of your repository.


### Exercise 02 : Sorting a file

Write a shell script called sorter.sh that:
* sorts the hh.csv file from the previous exercise according to the column
“created_at” and then by the “id” in ascending order
* saves the result in the CSV file hh_sorted.csv

The CSV file must still have headers in its first row.

Your script must be executable. The interpreter to use is /bin/sh.

Put your shell script as well as your result of the sorting in the folder ex02 in the root
directory of your repository.


### Exercise 03 : Replacing strings in a file


Write a shell called script cleaner.sh that:
* takes “Junior”, “Middle”, “Senior” from the names of position, if the name does not
contain any of these words use “-” (e.g. “Senior Data Scientist” -> “Senior”, “analyst
/(data scientist)” -> “-”, “Специалист / data scientist (big data, прогностическая
аналитика, data mining)” -> “-” ), if there are several of them, keep them all(e.g.
“Middle/Senior Data Scientist” -> “Middle/Senior”)
* saves the result in the CSV file hh_positions.csv.

You can see the example below:

    "id","created_at","name","has_test","alternate_url"
    "35218725","2020-04-11T18:03:53+0300","Junior",false,"https://hh.ru/vacancy/35218725"
    "36359628","2020-04-11T19:25:48+0300","Senior",false,"https://hh.ru/vacancy/36359628"
    "35895583","2020-04-12T12:06:33+0300","-",false,"https://hh.ru/vacancy/35895583"

The CSV file must still have headers in its first row and be sorted as per the previous
exercise.

Your script must be executable. The interpreter to use is /bin/sh.

Put your shell script as well as your result from cleaning in the ex03 folder in the root
directory of your repository.


### Exercise 04 : Descriptive statistics

Write a shell script called counter.sh that:
* counts unique values of the name column in the file you prepared in the
* previous exercise,
* sorts the table by that count in descending order
* stores the result in the CSV file hh_uniq_positions.csv

See the example below:

    "name","count"
    "Junior",10
    "Middle",5
    "Senior",3

The CSV file must have headers in the first row as in the example.

Your script must be executable. The interpreter to use is /bin/sh.
Put your shell script as well as the result of counting in the ex04 folder in the root
directory of your repository.


### Exercise 05 : Partitioning and concatenation


Write one shell script called partitioner.sh that:
* takes as input the result of Exercise 03
* stores slices of data with different "created_at" dates in separate CSV files named
for that date

See the example of such a file below:

    "id","created_at","name","has_test","alternate_url"
    "35218725","2020-04-11T18:03:53+0300","Junior",false,"https://hh.ru/vacancy/35218725"
    "36359628","2020-04-11T19:25:48+0300","Senior",false,"https://hh.ru/vacancy/36359628"

Write another shell script called concatenator.sh that:
* takes as input the separate files from the result of partitioner.sh
* concatenates all separate files into one CSV file

The CSV files must have headers in the first row, as in the example. The CSV from
the result of concatenator.sh must be equal to the result of Exercise 3

Your scripts must be executable. The interpreter to use is /bin/sh.

Put your shell scripts in the ex05 folder in the root directory of your repository.
