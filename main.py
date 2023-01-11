
import random

words = ['apple', 'pie', 'salam']

chosen_word = random.choice(words)
print(f'the chosen word is :{chosen_word}')

answer_list = []

for letter in chosen_word:
    answer_list.append('-')

guess_is_correct = False
live = 5
game_is_over = False
while not game_is_over:
 
    if live < 1:
        print('you lose.')
        game_is_over = True

    elif '-' not in answer_list:
        print('+++++++++++++')
        print('well done you win')
        print(answer_list)
        print('+++++++++++++')
        game_is_over = True
    else:
        print('-----------')
        print(f'you have {live} attempts')
        print(answer_list)
        print('-----------')
        user_input = input("Enter a letter: ")
        for i in range(len(answer_list)):
            if user_input == chosen_word[i]:
                guess_is_correct = True
                del answer_list[i]
                answer_list.insert(i,user_input)
        if guess_is_correct == True:
            guess_is_correct = False
        elif guess_is_correct == False:
            live -=1
    
