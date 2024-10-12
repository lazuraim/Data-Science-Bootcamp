import sys
import time
import requests
from bs4 import BeautifulSoup


def yahoo_parser(ticker: str, field_to_find: str):
    url=f'https://finance.yahoo.com/quote/{ticker}/financials'
    headers = { 'User-Agent': "browser" }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception("URL does not exist")

    soup = BeautifulSoup(response.text, "html.parser")
    totals = soup.find(title=field_to_find)
    if totals is None:
        raise Exception("Requested field does not exist")

    values = []
    for data in totals.parent.parent:
        if data.find('span') is not None:
            values.append(data.text)
    time.sleep(5)
    return tuple(values)


if __name__=='__main__':
    if len(sys.argv) != 3:
        raise Exception("Enter ticker and the field of the table")
    
    print(yahoo_parser(sys.argv[1], sys.argv[2]))