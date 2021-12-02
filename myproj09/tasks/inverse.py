def input(update, context):
    word = input("단어를 입력하세요: ")

    word = word.lower()  # word 를 소문자로 바꿔줌
    word = word.replace(" ", "")  # word띄어쓰기를 제거
    palindrome = True
    for i in range(len(word)):
        if word[i] != word[-1 - i]:
            palindrome = False
            break
        else:
            response_text = palindrome
