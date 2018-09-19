from nltk.corpus import wordnet as wn


def synonyms(word, top=10):
    synsets = wn.synsets(word)
    ans = list()
    vi = set()
    vi.add(word)
    for synset in synsets:
        for l in synset.lemmas():
            name = l.name()
            if name not in vi:
                vi.add(name)
                ans.append(name)
            if len(ans) > top:
                return ans
    return ans


if __name__ == '__main__':
    import sys
    for i in sys.exit(synonyms(sys.argv[1])):
        print i
