import pandas as pd
import numpy as np
path_to_data = 'gapminder.tsv'
path_to_data
data = pd.read_csv(path_to_data, sep = '\t')
data.head()
data.tail()
data.shape

data.info()
data.columns
type(data.columns)
list(data.columns)
data.shape[0]*data.shape[1]
data.describe()

#subsetting our data frame
idx_asia = data['continent']=='Asia'
data_asia = data[idx_asia]

#max year
max_year = data_asia['year'].max()
max_year

idx_year = (data_asia['year'] == max_year)
data_asia = data_asia[idx_year]

data_asia = data[(data['continent'] == 'Asia') & (data['year'] == data['year'].max())]
data_asia

cont = 'Asia'
idxCont = data['continent'] == cont
temp = data[idxCont]

year = temp['year'].max()
idxYear = temp['year'] == year
data_final = temp[idxYear]
def GetRecentDataByContinent(data,continent):
    idxCont = data['continent'] == cont
    temp = data[idxCont]
    year = temp['year'].max()
    idxYear = temp['year'] == year
    return temp[idxYear]

data_asia = GetRecentDataByContinent(data, 'Asia')

data['country'].unique()
data_count = data['year'].value_counts()
data_count
len(data['country'].unique())
print(data.sort_index().to_string())

#LOC and ILOC
data_asia.iloc[0]
data_asia.loc[11]

data_frame = data.reset_index(drop=True)
data_asia

#Exercises

#list of all the years in the data
years = data['year'].unique()
print(years)
print('There are 12 Unique Years and they are', years)

#largest value for population: China in 2007
max_pop = data['pop'].max()
#max_pop
idx_pop = (data['pop'] == max_pop)
data_max = data[idx_pop]
data_max

#Europe
cont = 'Europe'
idxCont = data['continent'] == cont
def GetRecentDataByContinent(data,continent):
    idxCont = data['continent'] == cont
    temp = data[idxCont]
    year = temp['year'].max()
    idxYear = temp['year'] == year
    return temp[idxYear]

Europe_data = GetRecentDataByContinent(data,'Europe')
Europe_data

#Which country had the smallest population in 1952: Iceland
def GetEurope(data):
    data_europe = data[(data['continent'] == 'Europe') & (data['year'] == 1952)]
    min_pop = data_europe.loc[data_europe['pop'] == data_europe['pop'].min()]
    return min_pop
GetEurope(data)

#Iceland population in 2007: 301931
now = data[(data['country'] == 'Iceland') & (data['year'] == 2007)]
now

