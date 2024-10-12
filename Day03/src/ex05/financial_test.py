import sys
import time
import requests
from bs4 import BeautifulSoup
import pytest


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
    return tuple(values)

def test1():
    result = yahoo_parser('MSFT', 'Total Revenue')
    assert 'Total Revenue' in result

def test2():
    result = yahoo_parser('MSFT', 'Total Revenue')
    assert isinstance(result, tuple)

def test3():
    with pytest.raises(Exception, match="URL does not exist"):
        yahoo_parser('Ticker', 'Total Revenue')

def test4():
    with pytest.raises(Exception, match="Requested field does not exist"):
        yahoo_parser('MSFT', 'Field')


if __name__=='__main__':
    if len(sys.argv) != 3:
        raise Exception("Enter ticker and the field of the table")
    
    print(yahoo_parser(sys.argv[1], sys.argv[2]))