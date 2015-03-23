import time
from itertools import chain, permutations


WORDLIST = 'dict/en.txt'


def main():
    start_w = time.clock()
    wordlist = set(line.strip() for line in open(WORDLIST))
    board_lines = ['PITBU', 'WZRSV', 'OIRNO', 'BFAEN', 'PLSXA',]
    board_lines = [list(l) for l in board_lines]
    board_letters = list(chain.from_iterable(board_lines))
    end_w = time.clock()
    duration_w = (end_w - start_w) / 1000

    found_words = []
    count = 0
    start_s = time.clock()
    for i in range(0, len(board_letters)+1):
        for subset in permutations(board_letters, i):
            if subset in wordlist:
                found_words.append(subset)
            count += 1

            if count % 1000000 == 0:
                print "{0} combinations tried".format(count)

    end_s = time.clock()
    duration_s = (end_s - start_s) / 1000
    print "{0} words found".format(len(count))
    print "wordlist load took {0}s".format(duration_w)
    print "search took {0}s".format(duration_s)


if __name__ == '__main__':
    main()


# http://stackoverflow.com/questions/746082/how-to-find-list-of-possible-words-from-a-letter-matrix-boggle-solver
