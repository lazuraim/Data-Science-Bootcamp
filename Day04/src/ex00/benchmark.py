import timeit

def loop_fun(emails: list):
    gmails = []
    for email in emails:
        if email.split('@')[1] == 'gmail.com':
            gmails.append(email)

def list_comp_fun(emails: list):
    gmails = [email for email in emails if email.split('@')[1] == 'gmail.com']


if __name__=='__main__':
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com'] * 5
        
    loop_time = timeit.timeit(lambda: loop_fun(emails), number=90000000)
    lc_time = timeit.timeit(lambda: list_comp_fun(emails), number=90000000)

    if loop_time >= lc_time:
        print("it is better to use a list comprehension")
        print(f"{lc_time} vs {loop_time}")
    else:
        print("it is better to use a loop")
        print(f"{loop_time} vs {lc_time}")



