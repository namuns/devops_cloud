
import requests
from bs4 import BeautifulSoup


def check_available(received_text: str) -> bool:  # 명시한것.
    return received_text.startswith("네이버 검색:")


def make_response(received_text: str) -> str:
    query = received_text[7:]
    post_list = naver_search(query)

    response_text = "\n".join([
        post["title"]
        for post in post_list])

#2번 같은 것
#response_text = ""
#   for post in post_list
#   response_text += post["title"] + "\n"

#3번 같은 것
#   response_text = "\n".join([
#       post["title"]
#       for post in post_list])
#   return response_text

def naver_search(query):
    naver_search_url = "https://search.naver.com/search.naver"
    params = {
        "where": "view",
        "sm": "tab_jum",
        "query": query,  # 검색어
    }
    res = requests.get(naver_search_url, params=params)
    soup = BeautifulSoup(res.text, "html.parser")
    return [
        {"title": tag.text} #tag.text만 쓸려면 title이 문자열이기 때문에
            for tag in soup.select(".lst_total .total_tit")]

