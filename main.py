def non_complex(string):
    if "'" in string or '"' in string or "-" in string:
        return False
    else:
        return True


def match(input, compare):
    m = True
    if len(input) == len(compare): 
        for n, letter in enumerate(list(input)):
            if not letter == '?':
                if not letter == compare[n]:
                    m = False
    else:
        m = False
    return m


corpus = open('corpus', encoding='utf-8').read().splitlines()
phrase = input('>>  ')
for word in corpus:
        if match(phrase, word) and non_complex(word):
            print(word)
