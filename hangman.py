#random module
import random

#List
word_bank = [
    "azlon",
    "bombazine",
    "brocade",
    "calico",
    "cambric",
    "camel hair",
    "canvas",
    "cashmere",
    "cheviot",
    "chiffon",
    "chintz",
    "corduroy",
    "cotton",
    "crash",
    "crepe",
    "crepe de Chine",
    "cretonne",
    "damask",
    "delaine",
    "denim",
    "dimity",
    "duck",
    "flannel",
    "flax",
    "foulard",
    "fustian",
    "gabardine",
    "gauze",
    "gingham",
    "hemp",
    "holland",
    "horsehair",
    "jamdani",
    "jute",
    "khaki",
    "kimkhwāb",
    "lace",
    "linen",
    "mohair",
    "muslin",
    "nankeen",
    "poplin",
    "rabbit hair",
    "rayon",
    "reticella",
    "satin",
    "serge",
    "silk",
    "taffeta",
    "toile de Jouy",
    "tweed",
    "twill",
    "velvet",
    "velveteen",
    "wool",
    "yarn",
]


word = random.choice(word_bank)

guessedWord = ['_'] * len(word)

attempts = 1

#LOOP:
while attempts > 0:

    print('\nCurrent word: ' + ' '.join(guessedWord))

    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    if '_' not in guessedWord:
        print('\nCongratulations!! You guessed the word: ' + word)
        break
    else:
        print('\nYou\'ve run out of attempts! The word was: ' + word)
