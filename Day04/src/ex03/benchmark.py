import timeit
import sys
from functools import reduce


def loop_sum(num_for_sum: int):
    sum = 0
    for i in range(num_for_sum):
        sum = sum + i*i
    return sum

def reduce_sum(num_for_sum):
    return reduce(lambda x, y: x+y*y, range(num_for_sum), 0)


if __name__=='__main__':
    if len(sys.argv) != 4:
        print("Enter: loop / reduce, number of times to execute the script, the number for the sum")
        exit(1)

    times = int(sys.argv[2])
    num_for_sum = int(sys.argv[3]) + 1

    if sys.argv[1] == 'loop':
        print(timeit.timeit(lambda: loop_sum(num_for_sum), number=times))
    elif sys.argv[1] == 'reduce':
        print(timeit.timeit(lambda: reduce_sum(num_for_sum), number=times))