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


def main():
    all_the_words = get_words()
    #get difficulty from user
    #choose random word from list of appropriate_difficulty words
    mystery_word = random.choice(make_appropriate_difficulty(all_the_words, difficulty))


#tell/show user the length of the mystery_word

#user guesses one letter per round. one letter input only, must be a character.
