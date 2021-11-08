import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


print("TOP100 곡명 단어수 출력")


def sasa(song_dict):
    return song_dict["title"]


for song_dict in filter(sasa, song_list):
    print(len(song_dict["title"].split()))


##################################


print("곡명 단어수로 TOP10 곡명 출력")


def sasa(song_dict):
    return song_dict["title"]


for song_dict in filter(sasa, song_list):

    len((song_dict["title"].split()))

    print()

# sorted 쓰면 될거같은데 모르겠습니다ㅠㅠ

##################################

print("좋아요 수가 가장 많은 곡은? 적은 곡은?")


def filter_fn3(song_dic):
    return song_dic["like"]


for song_dic in filter(filter_fn3, song_list):
    print()

# int로 좋아요 수를 리스트화 하고,
# max와 min으로 print하면 될 것 같습니다..

##################################


print("곡명 단어 수가 가장 많은 곡은? 작은 곡은?")



def filter_k(song_dict):
    return len(song_dict["title"].split()) in song_dict["title"]


    print()


#title에서 .split으로 단어 수를 세고
#각 타이틀 값을 쭉 나열해서
# max와 min을 이용해서 print하면 될 것 같다.


####################################


print("곡명 글자수가 가장 많은곡은? 작은곡은?")


# 타이틀을 len을 이용해서 글자수를 모두 체크 후 리스트화하고
# max와 min을 이용해서 가장 많은 곡과 작은 곡을 print한다.

######################################


print("리스트에 랭크된 가수는 총 몇 팀인가요?")


#artist를 리스트화 하고 set으로 중복제거 후 
# .split으로 개수를 세서 print하면 될 것 같다.


######################################

print("2곡 이상 랭크된 가수는 몇 팀인가요?")


#모르겠습니다 ㅠㅠ

######################################

print("방탄 소년단의 좋아요 총 합은?")


def filt(song_dic):
    if song_dic["artist"] == "방탄소년단":
        return song_dic["like"]


for song_dic in filter(filt, song_list):
    a = int(song_dic["like"])
    print(sum(a))

# TypeError: 'int' object is not iterable
# 적용이 안되네요..

######################################