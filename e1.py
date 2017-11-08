import requests
from bs4 import BeautifulSoup


url = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html5lib")
rows = soup.find_all('tr', "election_item")
ids = []
years = []
for row in rows:
    year_td = row.find("td", "year")
    year = year_td.string
    data = row["id"]
    data_lst = data.split("-")
    print("%s %s" % (year, data_lst[-1]))