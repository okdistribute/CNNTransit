CNNTransit
==========

Traverses the CNN transcripts archive which can be found at http://archive.org/details/cnn-transcripts-2000-2012

Prerequisites
=============
Python 2+

You can get these from pip or easy_install:

     BeautifulSoup4
    dateutil
    

Usage
=====
CNNTransit traverses the cnn transcripts using the following logical order:

    collect
    filter
    finish

Example: counts the number of transcripts containing Barack Obama and Mitt Romney

    from collections import defaultdict
    from nltk import bigrams
    
    names = ["Barack Obama", "Mitt Romney"]
    ds = CNNTransit("election2012")
    counts = defaultdict(int)

    def filter(self, text):
        for bigram in bigrams(text):
            if bigram in names:
                counts[bigram] += 1

    def finish(self):
        fp = open("out.csv", "wb")
        for name, count in counts.items():
            fp.write("%s, %s\n" % (name, count))
        fp.close()
    
    ds.filter = filter
    ds.finish = finish
    ds.collect(path="/path/to/cnn/TRANSCRIPTS", 
               start="2012-08-01", 
               end="2012-11-01")