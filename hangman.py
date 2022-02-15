import requests

class bcolors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    WARNING = '\033[93m'

response = requests.get(f'https://random-word-api.herokuapp.com/word?number=1')

if response.status_code != requests.codes.ok:
    print(f'{bcolors.FAIL}Something went wrong!{bcolors.RESET}')
else:
    word = response.json()[0]
    # print(word) 
    # uncomment the line above to see exposed word
    print("\nThis is the hangman game.\nYou have 7 chances to guess the word.\n")
    question = '_ '*len(word)
    print(f'{bcolors.OK}{question}\n{bcolors.RESET}')
    is_guessed = False
    miss = 0
    alphabet = ['a', 'b', 'c', 'd', 
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z']
    
    while not is_guessed and miss < 7:
        if not '_' in question:
            is_guessed = not is_guessed
            print(f'{bcolors.OK}You have won!\nYou only missed {miss} times!{bcolors.RESET}')
            continue
        guess = input('Guess: ').strip()
        print()
        if len(guess) > 1:
            continue
        else:
            if guess in word and guess in alphabet:
                for i in range(len(word)):
                    if word[i] == guess:
                        e = i+i
                        question = question[:e] + guess + question[e+1:]
                print(f'{bcolors.OK}{question}\n{bcolors.RESET}')
                alphabet.remove(guess)

            elif guess in word and guess not in alphabet:
                print(f'{bcolors.WARNING}You have already used this letter!\n{bcolors.RESET}')
                continue
            else:
                print(f'{bcolors.FAIL}{question}\n')
                miss += 1
                print(f'Miss: {miss}{bcolors.RESET}\n')
                if miss == 7:
                    print(f'{bcolors.FAIL}Correct word: {word}{bcolors.RESET}')
