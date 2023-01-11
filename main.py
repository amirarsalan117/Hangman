
import random

words = ['apple', 'pie', 'salam']

chosen_word = random.choice(words)
print(f'the chosen word is :{chosen_word}')

answer_list = []

for letter in chosen_word:
    answer_list.append('-')



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
                
