import random
words = ['Strawberries','Nectarines','Apples','Grapes','Peaches','Cherries','Pears',
          'Spinach','Kale','Tomatoes','Celery','Potatoes']

#Random word
random_word = list(random.choice(words))# Generating random word
#print(random_word) print to check
word_length = len(random_word)# length of random word

#Guess space
space = '_'* word_length# Number of letters to guess
print(space)
space = list(space)

#Hang man
hang_man = list('HANG MAN')#Converting to list for ease of manipulation
attempts = len(hang_man)#Length of list

#While the number of attempts is not zero
#and there is a blank space available the game continues
while (attempts > 0) and ('_'in space) :
    guess = input('Please guess a letter in the word: ')#Player input

    #if choice is correct find the index and replace blank space with guessed letter
    # Also replace the guessed letter in the random word with a blank space this way
    # repeating letters can be handled
    if guess in random_word:
        word_index = random_word.index(guess)
        random_word[word_index] = '_'
        space[word_index] = guess
        print(''.join(space))
    #Counting down the number of attempts and using the
    #negative number of attempts to display 'HANG MAN'
    else:
        attempts-=1
        print(attempts)
        print(''.join(hang_man[0:-attempts]))

if not ('_'in space):
    print('Congratulations you won')
elif attempts == 0:
    print('Sorry you loose')

