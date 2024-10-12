import sys

def define_entity(entity, entity_uppered: str):
    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }

    STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
    }

    REVERSED_COMPANIES = {value: key for key, value in COMPANIES.items()}
    UPPER_COMPANIES = {key.upper(): value for key, value in COMPANIES.items()}

    if entity_uppered in UPPER_COMPANIES:
        print(f'{REVERSED_COMPANIES[UPPER_COMPANIES[entity_uppered]]} stock price is {STOCKS[UPPER_COMPANIES[entity_uppered]]}')
    elif entity in STOCKS:
        print(f'{entity} is a ticker symbol for {REVERSED_COMPANIES[entity]}')
    else:    
        print(f'{entity} is unknown company or an unknown ticker symbol')


def parse_str(expressions: str):
    new_expressions = [elem.strip() for elem in expressions.split(",")]
    if '' not in new_expressions:
        return
    for elem in new_expressions:
        define_entity(elem, elem.upper())

if __name__ == "__main__":
    if len(sys.argv) == 2:
        parse_str(sys.argv[1])