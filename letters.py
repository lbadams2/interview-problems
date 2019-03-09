import sys

letter_set = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}

def get_missing_letters(sentence):
    sentence_set = set()
    for c in sentence:
        c = c.lower()
        if c in letter_set:
            sentence_set.add(c)
    missing_letters = letter_set - sentence_set
    result_str = ''.join(sorted(missing_letters))
    print(result_str)

def run():
    sentence = sys.argv[1]
    get_missing_letters(sentence)

run()