
def create_dict():
    list_of_tuples = [
    ('Russia', '25'),
    ('France', '132'),
    ('Germany', '132'),
    ('Spain', '178'),
    ('Italy', '162'),
    ('Portugal', '17'),
    ('Finland', '3'),
    ('Hungary', '2'),
    ('The Netherlands', '28'),
    ('The USA', '610'),
    ('The United Kingdom', '95'),
    ('China', '83'),
    ('Iran', '76'),
    ('Turkey', '65'),
    ('Belgium', '34'),
    ('Canada', '28'),
    ('Switzerland', '26'),
    ('Brazil', '25'),
    ('Austria', '14'),
    ('Israel', '12')
    ]
    
    my_dict = {}
    for pair in list_of_tuples:
        my_dict[pair[0]] = int(pair[1])

    res_dict = {}
    for pair in list_of_tuples:
        if pair[1] in res_dict:
            res_dict[pair[1]].append(pair[0])
        else:
            res_dict[pair[1]] = [pair[0]]

    sort_dict(res_dict)

                
def sort_dict(res_dict: dict):
    sorted_keys = reversed(sorted(res_dict.keys(), key=int))
    for key in sorted_keys:
        countries = sorted(res_dict[key])
        for country in countries:
            print(country)

if __name__ == "__main__":
    create_dict()
