import re
import reprlib


class IterableOne:

    RE_PATTERN = re.compile(r'\w+')

    def __init__(self, text):
        self.text = text
        self.words = self.RE_PATTERN.findall(self.text)

    def __len__(self):
        return len(self.words)

    def __getitem__(self, index):
        return self.words[index]

    def __repr__(self):
        return 'Iterator(%s)' % reprlib.repr(self.text)
