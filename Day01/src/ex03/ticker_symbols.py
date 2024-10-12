import sys

def display_company_price(ticker: str):
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

    company = ""
    for key in COMPANIES:
        if COMPANIES[key] == ticker:
            company = key

    if ticker in STOCKS:
        print(company + ' ' + str(STOCKS[ticker]))
    else:
        print("Unknown ticker")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        display_company_price(sys.argv[1].upper())