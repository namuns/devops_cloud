from collections import defaultdict, Counter
from pprint import pp, pprint
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 방탄소년단의 좋아요 총합
# List comprehension with if statement
like_sum_for_bts = sum([
    song_dict["like"]
    for song_dict in song_list
    if song_dict["artist"] == "방탄소년단"])
print(like_sum_for_bts)
