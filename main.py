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
        if all([l in board_letters for l in list(word)]):
            # FIXME: this doesn't take into account multiple uses of same letter
            found_words.append(word)

    found_words.sort(key=len, reverse=True)
    print "{0} words found".format(len(found_words))
    for word in found_words[:10]:
        print word


if __name__ == '__main__':
    main()
