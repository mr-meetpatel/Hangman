import random
import hangman_art

word_list=['python','java','android','jquery','php']

chosen_word = random.choice(word_list)

print(hangman_art.logo)

print(f"Chosen Word Is {chosen_word}")

letter = []
# create blanks
for i in chosen_word:
    for j in i:
        letter.append('_')

print(letter)

lives=6
repeated_letter=[]
#fill correct character to correct position

while '_' in letter and not lives == 0:
    guess=input("Guess Any Letter pls : ").lower()
    
    for i in range(0,len(chosen_word)):
        if guess in repeated_letter:
            lives= lives - 1
            print(stages[lives])
            break
        if chosen_word[i] == guess:
            letter[i]=chosen_word[i]

    repeated_letter.append(guess)        
        
    if guess not in chosen_word:
        
        lives= lives - 1
        print(hangman_art.stages[lives])
        
    print(letter)
    

 
if lives > 0:
    print("You Win !!")
else:
    print("You Lost !!")



