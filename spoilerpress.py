import argparse


''' Location of the Letterpress dictionary file to use '''
WORDLIST = 'Words/Words/en.txt'


def main():
    ''' Iterate the dictionary and test each word to see if it can be built
        from the supplied letters on the board.
    '''
    parser = argparse.ArgumentParser(description='Search a Letterpress game '
                                                 'board for valid dictionary '
                                                 'words.')
    parser.add_argument('letters', metavar='LETTERS', type=str,
                        help='letters on the board')
    parser.add_argument('-n', metavar='N', type=int, dest='limit', default=10,
                        help='limit word output to N items')
    args = parser.parse_args()
    board_letters = args.letters.upper()

    ''' Read in wordlist '''
    wordlist = set(line.strip() for line in open(WORDLIST))
    print "Testing letters: {0}".format(board_letters)
    print "{0} words in dictionary file".format(len(wordlist))
    board_letters = list(board_letters.lower())

    found_words = []
    for word in wordlist:
        ''' If all letters in the word appear the same number of times 
            or greater on the board...
        '''
        if all([board_letters.count(l) >= word.count(l) for l in list(word)]):
            found_words.append(word)

    ''' Sort found words by length '''
    found_words.sort(key=len, reverse=True)
    print "{0} words found on board:".format(len(found_words))
    for word in found_words[:args.limit]:
        print '- {0}'.format(word)


if __name__ == '__main__':
    main()
