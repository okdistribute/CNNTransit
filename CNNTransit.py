"""
CNNTransit.py

Written by Karissa McKelvey 

This traverses the cnn transcripts.

"""

from dateutil.parser import *
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os
import unittest


class CNN(object):
    """
    CNNTransit traverses the cnn transcripts using the following logical order:

    collect
    filter
    finish

    Example: counts the number of transcripts containing Barack Obama and Mitt Romney

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
    """

    def __init__(self, name):
        pass

    def filter(self, text):
        """Given the text of each transcript, do what you will"""
        pass

    def finish(self):
        """What to do after all transcripts have been filtered"""
        pass

    def do_filter(self, p):
        o = open(p)
        bs = BeautifulSoup(o)
        text = bs.get_text()
        self.filter(text)
        o.close()

    def collect(self, path=None, start=None, end=None):
        """Collects the transcripts. Dates are inclusive.
        
        Give this function a path, start, and end date and it will traverse each transcript file.
        """

        start = parse(start)
        end = parse(end)
        offset = timedelta(days=1)
        programs = []

        cur = start
        while cur <= end:
            datestr = "%02d%02d" % (int(str(cur.year)[2:]), cur.month)

            current_path = os.path.join(path, datestr, "%02d" % cur.day)
            htmls = os.listdir(current_path)
            htmls = map(lambda p: os.path.join(current_path, p), htmls)
            programs += htmls

            cur += offset

        map(self.do_filter, programs)
        self.finish()


class TestCNNTransit(unittest.TestCase):

    def setUp(self):
        self.cnn = CNN("transit")

        def filter(text):
            print "i've got a transcript!"
            return True

        def finish():
            print "done"

        self.cnn.filter = filter
        self.cnn.finish = finish

    def test_small(self):
        self.cnn.collect(path="/Users/kmac/data/TRANSCRIPTS", start="2010-02-08", end="2010-02-10")

if __name__ == '__main__':
    unittest.main()

