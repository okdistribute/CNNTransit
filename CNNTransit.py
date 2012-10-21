"""
CNNTransit.py

Written by Karissa McKelvey 

This traverses the cnn transcripts.

"""

from nltk import bigrams
from bs4 import BeautifulSoup

class CNNTransit(object):
    """
    CNNTransit traverses the cnn transcripts using the following logical order:

    collect
    filter
    write
    finish

    Example: Get transcripts containing Barack Obama and Mitt Romney

    names = [BarackObama, MittRomney]

    ds = CNNTransit("election2012")
    ds.filter = lambda w : w in names
    ds.write = lambda t, w : 
    def finish():
        print "All done after %d" % datetime.now() - start_time
    ds.finish = finish

    ds.collect(path="/path/to/cnn/TRANSCRIPTS", 
               start="2012-08-01", 
               end="2012-11-01")
    """

    def __init__(self, name):
        pass

    def filter(self, transcript):
        """Returns True if the transcript should be included in the dataset."""
        return True

    def write(self, transcript):
        """How the transcript should be written"""
        pass

    def finish(self):
        """What to do when we are finished"""
        pass

    def collect(self, path=None, start=None, end=None):
        """Collects the transcripts"""
        pass

class Transcript(object):
    """
    Defines a transcript object
    """

    def __init__(self, path):
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
