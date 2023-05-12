from bs4 import BeautifulSoup
import pandas as pd
import requests

years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006,
         2010, 2014, 2018, 2022]

data = []  # List to store the data for all years

for year in years:
    web = f"https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup"
    r = requests.get(web)
    soup = BeautifulSoup(r.text, "html.parser")
    home_elem = [home_team.get_text() for home_team in soup.find_all("th", class_="fhome")]
    score_elem = [score.get_text() for score in soup.find_all("th", class_="fscore")]
    away_elem = [away_team.get_text() for away_team in soup.find_all("th", class_="faway")]
    dict_football = {"home": home_elem, "score": score_elem, "away": away_elem, "year": year}
    data.append(pd.DataFrame(dict_football))  # Append the DataFrame for the current year to the list

df_world_cups = pd.concat(data)  # Concatenate all DataFrames in the list

df_world_cups.to_csv("world_cup.csv", index=False)

