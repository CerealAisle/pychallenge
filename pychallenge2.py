# test
from pprint import pprint

file = open('C:\\Users\\hollmje\\Desktop\\characters.txt')

def count_characters(file):

    line = file.readline()
    count = 0
    characters = {}
    
    while line != "":

        for letter in line:

            if letter in characters:
                characters[letter] += 1
            else:
                characters[letter] = 1

        count += 1
        line = file.readline()

    print(count)

    return characters

pprint(count_characters(file))
file.close()

