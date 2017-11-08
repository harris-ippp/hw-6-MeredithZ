import pandas as pd
import matplotlib.pyplot as plt

def read_data(year):
    header = pd.read_csv("./data/president_general_%s.csv" % year, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv("./data/president_general_%s.csv" % year, index_col = 0,
               thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df["Year"] = year
    return df

dataframes = []
for year in range(1924,2017,4):
    dataframes.append(read_data(year))

df = pd.concat(dataframes, join="inner")
df["Republican Share"] = df["Republican"]/df["Total Votes Cast"]


data = df.loc["Accomack County"]
data.set_index(data["Year"], inplace=True)
data["Republican Share"].plot()
plt.ylabel("Republican Share")
plt.savefig('accomack_county.pdf',format='pdf')

data = df.loc["Albemarle County"]
data.set_index(data["Year"], inplace=True)
data["Republican Share"].plot()
plt.ylabel("Republican Share")
plt.savefig('albemarle_county.pdf',format='pdf')

data = df.loc["Alexandria City"]
data.set_index(data["Year"], inplace=True)
data["Republican Share"].plot()
plt.ylabel("Republican Share")
plt.savefig('alexandria_city.pdf',format='pdf')



data = df.loc["Alleghany County"]
data.set_index(data["Year"], inplace=True)
data["Republican Share"].plot()
plt.ylabel("Republican Share")
plt.savefig('alleghany_county.pdf',format='pdf')