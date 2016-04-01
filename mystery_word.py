import random

def greeting():
    print("Hello! Shall we play a word game?")
    print("I will pick a word and you will try to guess it one letter at a time.")

def get_difficulty():
    while True:
        difficulty = input("How difficult should this game be? Would you like [E]asy, [N]ormal, or [H]ard? ").lower()
        if difficulty == 'e' or difficulty == 'easy':
            return 'EASY'
        elif difficulty == 'n' or difficulty == 'normal':
            return 'NORMAL'
        elif difficulty == 'h' or difficulty == 'hard':
            return 'HARD'
        else:
            print("What was that? I didn't quite understand you. Let's try again.")


#get words file
def get_words(path='/usr/share/dict/words'):
    list_of_words = []
    with open(path, 'r') as words:
        for line in words:
            word = line.strip()
            list_of_words.append(word)
    return list_of_words

#difficulty level: easy (4-6 character words), normal(6-8 character words), hard (8+ character words)
def make_appropriate_difficulty(word_list, difficulty='EASY'):
    dictionary_of_pain = {'EASY': (3,7), 'NORMAL': (5,9), 'HARD': (7,25)}
    appropriate_difficulty = []
    for word in word_list:
            if len(word) > dictionary_of_pain[difficulty][0] and len(word) < dictionary_of_pain[difficulty][1]:
                appropriate_difficulty.append(word)
    return appropriate_difficulty

def show_word(mystery_word, guesses):
    word = []
    for letter in mystery_word:
        if letter in guesses:
            word.append(letter)
        else:
            word.append('_')
    print(' '.join(word))
    return word #for unit testing purposes

def main():
    all_the_words = get_words()
    difficulty = get_difficulty()
    mystery_word = random.choice(make_appropriate_difficulty(all_the_words, difficulty)).lower() #choose random word from list of appropriate_difficulty words. make sure lower case.
    print("Mystery Word: ", mystery_word, ", Difficulty : ", difficulty)

#tell/show user the length of the mystery_word

#user guesses one letter per round. one letter input only, must be a character.

if __name__ == "__main__":
    main()
