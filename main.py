#Step1: import random for chose random word from words list
import random

words = ['apple', 'pie', 'salam']

chosen_word = random.choice(words)
print(f'the chosen word is :{chosen_word}')
#Step2: declare a list that contain - for every letter in chosen word
answer_list = []

for letter in chosen_word:
    answer_list.append('-')


#Step3: Get User input and if the guess is true replace it with the answar list  selected position
game_is_over = False
while not game_is_over:
    print('-----------')
    print(answer_list)
    print('-----------')
    if '-' not in answer_list:
        game_is_over = True
    else:
        user_input = input("Enter a letter: ")
        for i in range(len(answer_list)):
            if user_input == chosen_word[i]:
                del answer_list[i]
                answer_list.insert(i,user_input)
                
