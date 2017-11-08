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
    years.append(year)
    data = row["id"]
    data_lst = data.split("-")
    ids.append(data_lst[-1])


for i in range(len(years)):
    fp = open("president_general_%s.csv" % years[i], "w")
    res = requests.get("http://historical.elections.virginia.gov/elections/download/%s/precincts_include:0/" % ids[i])
    fp.write(res.text)
    fp.close()
