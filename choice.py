import random

word = open("word.txt", "r" ,encoding='UTF-8')
data = word.read()
data = data.split("\n")
choice = random.sample(data,3)
print("".join(choice))