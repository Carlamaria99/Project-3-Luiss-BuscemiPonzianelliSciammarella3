import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# perform some cleaning operation on the dataset in order to make it useful for data visualization
movies = pd.read_csv("/Users/Andrea/Desktop/Python and R/Progetto Film/DEF/SCRIPT/DF_1999movies.csv", )

movies["BoxOffice"].replace({",": ""},
                            regex = True,
                            inplace=True)

movies["BoxOffice"].replace({"\$": ""},
                            regex = True,
                            inplace=True)

movies["Runtime"].replace(" min", "",
                          regex = True,
                          inplace=True)
movies.rename(columns={"Runtime": "Runtime (min)"}, inplace=True)
movies["Runtime (min)"] = movies["Runtime (min)"].replace({"1 h 34": "94",
                                                           "1 h 15": "75",
                                                           "1 h 22": "82",
                                                           "1 h 25": "85",
                                                           "1 h 28": "88",
                                                           "2 h 5": "125",
                                                           "1 h 30": "90",
                                                           "1 h 33": "93",
                                                           "1 h 46": "106",
                                                           "1 h 20": "80",
                                                           "1 h 40": "100",
                                                           "1 h 10": "70",
                                                           "1 h 56": "116",
                                                           "1 h 19": "79",
                                                           "1 h": "60",
                                                           "1 h 50": "110",
                                                           "1 h 4": "64",
                                                           "60 22": "82",
                                                           "60 15": "75",
                                                           "60 25": "85",
                                                           "60 28": "88",
                                                           "60 30": "90",
                                                           "60 33": "93",
                                                           "60 46": "106",
                                                           "60 20": "80",
                                                           "60 40": "100",
                                                           "60 10": "70",
                                                           "2 h 13": "133",
                                                           "60 56": "116",
                                                           "60 19": "79",
                                                           "60 50": "110",
                                                           "60 4": "64",
                                                           "2 h 34": "154"})
movies["imdbVotes"].replace({",": ""},
                            regex = True,
                            inplace = True)

#drop useless columns for data visualization
v_useless = ["Unnamed: 0", "Response", "Error","Year", "Rated", "Released", "Plot", "Poster",
             "imdbID", "Type", "DVD", "Website", "Director", "Writer", "Actors",
             "Awards", "Ratings", "Metascore", "Production"]

for v in v_useless:
    movies.drop(columns=[v], inplace=True)

#transform numeric variables
v_numeric = ["Runtime (min)", "imdbRating", "imdbVotes", "BoxOffice"]

for v in v_numeric:
    movies[v] = pd.to_numeric(movies[v])

#remove second language, country and genre in every observation, we keep only first
movies["LanguageNew"] = movies["Language"].str.split(",").str[0]
movies["CountryNew"] = movies["Country"].str.split(",").str[0]
movies["GenreNew"] = movies["Genre"].str.split(",").str[0]

#additional cleaning
movies["CountryNew"].replace({"United States" : "USA",
                              "United Kingdom" : "UK"})

#trnasform categorical variables
v_factors = ["LanguageNew", "CountryNew", "GenreNew"]

for v in v_factors:
    movies[v] = movies[v].astype("category")

#drop now useless variables
movies.drop(columns = ["Language", "Country", "Genre"], inplace = True)


pl_num = ["Runtime (min)", "imdbRating", "imdbVotes", "BoxOffice"]
pl_cat = ["LanguageNew", "CountryNew", "GenreNew"]

#subset only relevant countries and languages (otherwise too many categories)
rel_lang = ["English", "French", "Spanish", "Italian", "German", "Portuguese",
            "Greek", "Russian", "Dutch", "Afrikaans", "Arabic", "Hindi",
            "Chinese", "Korean", "Japanese", "Indian", "Mandarin", "Bengali", "Indonesian"]
rel_countries = ["USA", "UK", "France", "China", "Italy",
                 "Spain", "Portugal", "Greece", "Germany", "Netherlands",
                 "India", "Egypt", "Japan", "Brasil", "Mexico", "Argentina"]

#create bew dfs for simpler use and plotting
lang_df = movies
country_df = movies

#change to str otherwise precious categories are kept
for v in v_factors:
    lang_df[v] = lang_df[v].astype("str")
    country_df[v] = country_df[v].astype("str")

lang_df = lang_df[lang_df.LanguageNew.isin(rel_lang)]
country_df = country_df[country_df.CountryNew.isin(rel_countries)]


#plot every categorical variables count
movies["GenreNew"].value_counts().plot(kind = "bar",
                                       legend = True)
lang_df["LanguageNew"].value_counts().plot(kind="bar",
                                           legend = True)
country_df["CountryNew"].value_counts().plot(kind = "bar",
                                             legend = True)
plt.show()

#plot every numeric variables frequency
for p in pl_num:
    movies[p].plot(kind="hist",
                   legend = True)
    plt.show()

#plot boxlpots of every categorical to numerics
for j in pl_num:
    bxp = sns.boxplot(x=movies["GenreNew"], y=j, data = movies)
    bxp.get_figure().autofmt_xdate()
    plt.show()


for j in pl_num:
    bxp1 = sns.boxplot(x=lang_df["LanguageNew"], y =j, data = lang_df)
    bxp1.get_figure().autofmt_xdate()
    plt.show()

for j in pl_num:
    bxp2 = sns.boxplot(x=country_df["CountryNew"], y =j, data = country_df)
    bxp2.get_figure().autofmt_xdate()
    plt.show()