import random,hangman_art,hangman_words
words=hangman_words.word_list
chosen=random.choice(words)
blanked=list('_'*len(chosen))

stages = hangman_art.stages
lives=0
print(hangman_art.logo)
while lives!=6:
    for i in blanked:
        print(i,end=' ')
    if '_' not in blanked:
        break
    guess=input("\nGuess a letter: ")
    if guess in chosen:
        print("You guessed right!")
        for j in range(len(chosen)):
            if guess==chosen[j]:
                blanked[j]=guess
    else:
        print("You guessed wrong")
        lives+=1
    print(f"Lives left: {6-lives}")
    print(stages[6-lives])   
if(lives!=6):
    print("\nYou Win!")
else:
    print("\nGame over.")
    print(f"The word was {chosen}")
