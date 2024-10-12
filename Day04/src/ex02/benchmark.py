import timeit
import sys


def handle_args(option: str, times: int):
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com'] * 5
        
    loop_time = timeit.timeit(lambda: loop_fun(emails), number=times)
    lc_time = timeit.timeit(lambda: list_comp_fun(emails), number=times)
    map_time = timeit.timeit(lambda: map_fun(emails), number=times)
    filter_time = timeit.timeit(lambda: filter_fun(emails), number=times)

    if option == 'loop':
        print(loop_time)
    elif option == 'list_comprehension':
        print(lc_time)
    elif option == 'map':
        print(map_time)
    elif option == 'filter':
        print(filter_time)

def loop_fun(emails: list):
    gmails = []
    for email in emails:
        if email.split('@')[1] == 'gmail.com':
            gmails.append(email)

def list_comp_fun(emails: list):
    gmails = [email for email in emails if email.split('@')[1] == 'gmail.com']

def map_fun(emails: list):
    gmails = map(lambda email: email if email.split('@')[1] else None, emails)


def filter_fun(emails: list):
    gmails = filter(lambda email: email if email.split('@')[1] else None, emails)

if __name__=='__main__':
    if len(sys.argv) != 3:
        print("Enter name of the option and number of times to execute the script")
        exit(1)
    
    handle_args(sys.argv[1], int(sys.argv[2]))
