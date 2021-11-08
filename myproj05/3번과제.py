
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

print("방탄 소년단의 좋아요 총 합은?")


def filt(song_dic):
    if song_dic["artist"] == "방탄소년단":
        return song_dic["like"]


for song_dic in filter(filt, song_list):
    a = song_dic["like"]
    int(a)
    print(sum(a))
