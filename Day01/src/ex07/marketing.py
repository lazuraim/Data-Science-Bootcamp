import sys

def fun(request):
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
    'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
    'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    if request == 'call_center':
        print(call_center(clients, participants, recipients))
    elif request == 'potential_clients':
        print(potential_clients(clients, participants, recipients))
    elif request == 'loyalty_program':
        print(loyalty_program(clients, participants, recipients))
    else:
        raise Exception("Please, enter one of the following requests: call_center / potential_clients / loyalty_program")

def call_center(clients, participants, recipients) -> list:
    all_people = set(clients + participants)
    to_call = all_people.difference(recipients)
    return list(to_call)

def potential_clients(clients, participants, recipients) -> list:
    all_people = set(participants + recipients)
    potential = all_people.difference(clients)
    return list(potential)

def loyalty_program(clients, participants, recipients) -> list:
    potential = set(clients).difference(set(participants))
    return list(potential)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        fun(sys.argv[1])
    else:
        print("Wrong number of arguments")