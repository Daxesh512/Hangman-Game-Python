import random
import art
import words
chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

print (art.logo)
#Create blanks
display = []
for _ in range(word_length):
    display += "_"
lives = 7
final_display = ''
blank_full = False
print (display)
while not blank_full:
    guess = input("Guess a letter: ").lower()
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
           
    if guess not in chosen_word:
        lives -= 1
        print(art.stages[lives])
        print(f"Your Guess is {guess}, Its Wrong!")
        print(f"You Lost One Life, Lives Remaining:{lives}")
    if lives ==0:
        print("Oops You Lost Sommry :(")
        print(f"The Word Was {chosen_word}")
        break
    elif "_" not in display:
        print("You Win")
        break 

    print(display)


