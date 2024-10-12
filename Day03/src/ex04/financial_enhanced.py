import sys
import time
import http.client
from bs4 import BeautifulSoup
import cProfile
from pstats import Stats



def yahoo_parser(ticker: str, field_to_find: str):
    headers = { 'User-Agent': "browser" }
    conn = http.client.HTTPSConnection("finance.yahoo.com")
    conn.request("GET", f"/quote/{ticker}/financials", headers=headers)
    response = conn.getresponse()
    if response.status != 200:
        raise Exception("URL does not exist")

    soup = BeautifulSoup(response.read(), "html.parser")
    totals = soup.find(title=field_to_find)
    if totals is None:
        raise Exception("Requested field does not exist")

    values = []
    for data in totals.parent.parent:
        if data.find('span') is not None:
            values.append(data.text)
    return tuple(values)


if __name__=='__main__':
    if len(sys.argv) < 3:
        raise Exception("Enter ticker and the field of the table")

    with cProfile.Profile() as profile, open("pstats-cumulative.txt", "w") as file:
        yahoo_parser(sys.argv[1], sys.argv[2])
        result = Stats(profile, stream=file).sort_stats('cumulative')
        result.print_stats(5)


    