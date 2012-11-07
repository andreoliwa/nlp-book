#!/usr/bin/python
"""Examples from the NLTK book."""


def page57():
    """Statistics from the Gutenberg corpora"""
    from nltk.corpus import gutenberg
    for fileid in gutenberg.fileids():
        num_chars = len(gutenberg.raw(fileid))
        num_words = len(gutenberg.words(fileid))
        num_sents = len(gutenberg.sents(fileid))
        num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
        print int(num_chars / num_words), int(num_words / num_sents),
        print int(num_words / num_vocab), fileid


def page59():
    """Prints the longest sentence from Macbeth"""
    from nltk.corpus import gutenberg
    macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
    print 'macbeth_sentences=', macbeth_sentences
    print 'macbeth_sentences[1037]=', macbeth_sentences[1037]
    longest_len = max([len(s) for s in macbeth_sentences])
    print 'longest sentence=',
    print [s for s in macbeth_sentences if len(s) == longest_len]


def page60():
    """Prints the frequency distribution of some modal verbs
    in the Brows Corpus"""
    import nltk
    from nltk.corpus import brown
    news_text = brown.words(categories='news')
    fdist = nltk.FreqDist([w.lower() for w in news_text])
    modals = ['can', 'could', 'may', 'might', 'must', 'will']
    for modal in modals:
        print modal + ':', fdist[modal],


def page61_your_turn():
    """Find question words (starting with wh-) in the Brown corpus,
    and show their frequency distribution"""
    import nltk
    from nltk.corpus import brown
    news_text = brown.words(categories='romance')
    wh_words = sorted(set([wh for wh in news_text if wh.startswith('wh')]))
    tagged_wh_words = nltk.pos_tag(wh_words)
    modals = sorted(set(
        modal for (modal, tag) in tagged_wh_words if tag.startswith('W')))
    fdist = nltk.FreqDist([w.lower() for w in news_text])
    for modal in modals:
        print modal + ':', fdist[modal],

if __name__ == "__main__":
    print __doc__
    print dir()
    #page57()
    #page59()
    page60()
    #page61_your_turn()
