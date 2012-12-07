CNNTransit
==========

Traverses the CNN transcripts archive which can be found at http://archive.org/details/cnn-transcripts-2000-2012

Prerequisites
=============
Python 2+ and BeautifulSoup4

Usage
=====
Example: counts the number of transcripts containing Barack Obama and Mitt Romney

    from collections import defaultdict
    from nltk import bigrams
    from CNNTransit import CNN
    
    names = ["Barack Obama", "Mitt Romney"]
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
        
        
    cnn = CNN("election2012")
    cnn.filter = filter
    cnn.finish = finish
    cnn.collect(path="/path/to/cnn/TRANSCRIPTS", 
               start="2000-08-01", 
               end="2012-3-01")