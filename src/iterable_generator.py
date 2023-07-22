import re
import reprlib


class IterableGenerator:

    def __init__(self, text):
        self.text = text
        self.words = re.compile(r'\w+').findall(self.text)

    def __repr__(self):
        return 'Iterable(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for s in self.words:
            yield s
