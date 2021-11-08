import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


def sasa(song_dict):
    return song_dict["title"]


for song_dict in filter(sasa, song_list):

    list[len((song_dict["title"].split()))]

    print(list.sort())
