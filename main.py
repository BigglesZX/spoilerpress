import time
from itertools import chain, permutations


WORDLIST = 'dict/en.txt'


def main():
    wordlist = set(line.strip() for line in open(WORDLIST))
    board_lines = ['PITBU', 'WZRSV', 'OIRNO', 'BFAEN', 'PLSXA',]
    board_lines = [list(l) for l in board_lines]
    board_letters = list(chain.from_iterable(board_lines))
    board_letters = list(''.join(board_letters).lower())
    print "Testing letters: {0}".format(''.join(board_letters).upper())

    found_words = []
    for word in wordlist:
        if all([board_letters.count(l) >= word.count(l) for l in list(word)]):
            found_words.append(word)

    found_words.sort(key=len, reverse=True)
    print "{0} words found".format(len(found_words))
    for word in found_words[:10]:
        print word


if __name__ == '__main__':
    main()
