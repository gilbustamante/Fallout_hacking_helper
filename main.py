"""
Fallout Hacking Helper
----------------------
Easily narrow down "hacking" choices in Bethesda-era Fallout hacking
mini-games.
"""

#words = []
#print('Enter listed words:')
#while True:
#    word = input()
#    if word == '':
#        break
#    words.append(word)
#print(words)

temporary_list = [
    'HOST', 'BORN', 'PICK', 'CORK', 'TARP', 'GOLD', 'BORE', 'PACE', 'DANK',
    'LOOK', 'MASS', 'GOLF'
]

while True:
    entered = input('Entered word: ')
    correct_number = int(input('Enter correct number: '))

    for word in temporary_list:
        # Using Python's implicit int value of True and False:
        match_num = sum(c1 == c2 for c1, c2 in zip(word, entered))
        if match_num != correct_number:
            temporary_list.remove(word)

    print(temporary_list)
