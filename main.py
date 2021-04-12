"""
Fallout Hacking Helper
----------------------
Easily narrow down "hacking" choices in Bethesda-era Fallout hacking
mini-games.
"""

def get_entered_words():
    """Prompt user to enter words from the hacking terminal"""
    words = []
    print('Enter listed words (empty string to finish):')
    while True:
        word = input()
        if word == '':
            break
        words.append(word.upper())
    return words


def main(word_list):
    """Iterate through word_list and narrow down matches"""
    while True:
        if len(word_list) == 1:
            print(f"The answer is {word_list[0]}!")
            break
        used_word = input('Entered word: ').upper()
        correct_number = int(input('Correct characters: '))
        for word in word_list:
            # Using Python's implicit values of True and False:
            match_num = sum(c1 == c2 for c1, c2 in zip(word, used_word))
            if match_num != correct_number:
                word_list.remove(word)
        print(f"Remaining words: {word_list}")

if __name__ == "__main__":
    entered_words = get_entered_words()
    main(entered_words)
