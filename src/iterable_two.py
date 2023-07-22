import re
import reprlib

from src.iterable_iterator import IterableIterator


class IterableTwo:

    def __init__(self, text):
        self.text = text
        self.words = re.compile(r'\w+').findall(self.text)

    def __repr__(self):
        return 'Iterable(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return IterableIterator(self.words)