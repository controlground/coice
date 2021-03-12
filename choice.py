import random

true = 0
word = open("word.txt", "r" ,encoding='UTF-8')
data = word.read()
data = data.split("\n")
choice = random.sample(data,3)
letters = list("".join(choice))
random.shuffle(letters)
print(" ".join(letters))
while True:
    answer = input("숨겨진 세 글자 단어들을 찾아보세요.")
    true += 1
    if answer in choice:
        choice.remove(answer)
        print("정답입니다.")
    else:
        print("오답입니다.")
    if not choice:
        break
print("{}번 만에 클리어 하셨습니다.".format(true))
