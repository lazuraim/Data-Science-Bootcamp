import timeit

def loop_fun(emails: list):
    gmails = []
    for email in emails:
        if email.split('@')[1] == 'gmail.com':
            gmails.append(email)

def list_comp_fun(emails: list):
    gmails = [email for email in emails if email.split('@')[1] == 'gmail.com']

def map_fun(emails: list):
    gmails = map(lambda email: email if email.split('@')[1] else None, emails)


if __name__=='__main__':
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com'] * 5
        
    loop_time = timeit.timeit(lambda: loop_fun(emails), number=90000000)
    lc_time = timeit.timeit(lambda: list_comp_fun(emails), number=90000000)
    map_time = timeit.timeit(lambda: map_fun(emails), number=90000000)

    times = [loop_time, lc_time, map_time]
    
    if loop_time == min(times):
        print("it is better to use a loop")
    elif lc_time == min(times):
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a map")

    times.sort()
    print(f"{times[0]} vs {times[1]} vs {times[2]}")
