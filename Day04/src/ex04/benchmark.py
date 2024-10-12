import timeit
import random
from collections import Counter


def my_dict(values: list):
    new_dict = {}
    for elem in values:
        if elem in new_dict:
            new_dict[elem] += 1
        else:
            new_dict[elem] = 1
    return new_dict

def my_top(values: list):
    all_values = my_dict(values)
    all_values = dict(sorted(all_values.items(), key=lambda item: item[1], reverse=True))
    top_list = list(all_values.values())[:10]
    new_dict = {}
    for key, value in all_values.items():
        if value in top_list:
            new_dict[key] = value
    return new_dict

def Counter_dict(values: list):
    cnt = Counter(values)
    return dict(cnt)

def Counter_top(values: list):
    new_dict = Counter_dict(values)
    return dict(Counter(new_dict).most_common(10))
    

if __name__=='__main__':
    values = [random.randint(0, 100) for i in range(1000000)]
    print(f"my function: {timeit.timeit(lambda: my_dict(values), number=100)}")
    print(f"Counter: {timeit.timeit(lambda: Counter_dict(values), number=100)}")
    print(f"my top: {timeit.timeit(lambda: my_top(values), number=100)}")
    print(f"Counter's top: {timeit.timeit(lambda: Counter_top(values), number=100)}")