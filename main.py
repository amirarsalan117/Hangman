#Step1: import random for chose random word from words list
import random

words = ['apple', 'pie', 'salam']

chosen_word = random.choice(words)

#Step2: declare a list that contain - for every letter in chosen word
answer_list = []

for letter in chosen_word:
    answer_list.append('-')
    

