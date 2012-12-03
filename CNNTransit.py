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
from forkmap import *
from multiprocessing import Pool


class CNN(object):
    """
    CNNTransit traverses the cnn transcripts using the following logical order:

    collect
    filter
    write
    finish

    Example: Get transcripts containing Barack Obama and Mitt Romney

    names = ["Barack Obama", "Mitt Romney"]
    ds = CNNTransit("election2012")
    counts = {}

    def filter(self, text):
        for bigram in bigrams(text):
            if bigram in names:
                counts[bigram] += 1

    def finish(self):
        print counts

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
        """what to do at the end"""
        pass

    @parallelizable(15,perproc=4)
    def do_filter(self, p):
        o = open(p)
        bs = BeautifulSoup(o)
        text = bs.get_text()
        self.filter(text)
        o.close()

    def collect(self, path=None, start=None, end=None):
        """Collects the transcripts. Dates are inclusive
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
        self.cnn = CNNTransit("transit")

        def filter(text):
            print "filtering"
            return True

        def finish():
            print "done"

        self.cnn.filter = filter
        self.cnn.finish = finish

    def test_small(self):
        self.cnn.collect(path="/Users/kmac/data/TRANSCRIPTS", start="2010-02-08", end="2010-02-10")

if __name__ == '__main__':
    unittest.main()

