import pandas as pd
import requests
from requests.models import Response
# Part 1: extracting IMDB ids
# load the complete file from imdb data sets (over 8 million items) as df (from https://datasets.imdbws.com)
df = pd.read_csv('/Users/Andrea/Desktop/Python and R/Progetto Film/DEF/data.tsv',
                 #sep='\t',
                 #low_memory=False)

                 # keep in df only "movie" items
                 df = df.loc[df['titleType'] == "movie"]

# NaNs were displayed as "\\N", replace with "NaN"
df.replace(to_replace=r"\N", value="NaN", inplace=True)

# eliminate column endYear (all NaNs, valid only for TVseries)
df = df.drop('endYear', 1)

# subsetting into only 1999-produced movies
df = df.loc[df['startYear'] == '1999']

# eliminate useless columns
df = df.drop('titleType', 1)
df = df.drop('isAdult', 1)
df = df.drop('runtimeMinutes', 1)
df = df.drop('genres', 1)

# create new clean file to extract only 1999 movies with each IMDB id
df.to_csv("1999movies.csv")
# load new file
movies = pd.read_csv('1999movies.csv', nrows = 1000)
# drop previous enumeration
movies = movies.drop('Unnamed: 0', 1)
# now we have a clean df from which we are gonna take every IMDBid needed to perform the OMDB query via-API

# Part 2: API Calls

movies = pd.read_csv('1999movies.csv')
movies = movies.drop('Unnamed: 0', 1)
apiKeys = ["192ed21c",
           "99c43239",
           "bbfdd253",
           "58ed501",
           "1ad6a28c",
           "fc28d556",
           "1ee73f0c",
           "f3ff508",
           "333203af",
           "18bed636",
           "912de1b4",
           "f60c291e",
           "ace194ba",
           "bb624955",
           "7d63d23a",
           "32b32300"]
keysIndex = 0
all_data = []


for i in range(len(movies[movies.columns[0]])):
    url = "http://www.omdbapi.com/"
    params = {"i" : movies[movies.columns[0]][i],
              "apikey" : apiKeys[keysIndex]
              }
    response = requests.get(url, params=params)
    print(str(i+1)+": "+apiKeys[keysIndex]+": " + str(response.status_code))

    if str(response.status_code) != "200":
        keysIndex += 1
        response = requests.get(url, params=params)
        print(str(i+1)+": "+apiKeys[keysIndex]+": " + str(response.status_code))

    all_data.append(response.json())


df = pd.DataFrame(all_data)
df.replace(to_replace="N/A", value="NaN", inplace=True)
print(df)

# keep only rows where API call was succesful
df = df.loc[df['Response'] == "True"]

df.to_csv("DF_1999movies.csv")









