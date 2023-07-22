from collections import abc
from unittest import TestCase

from src.iterable_generator import IterableGenerator
from src.iterable_one import IterableOne
from src.iterable_two import IterableTwo


class IterableTest(TestCase):

    def test_iterable_one(self):
        s = IterableOne('The world is beautiful')
        assert len(s) > 0
        assert not isinstance(s, abc.Iterable)

    def test_iterable_two(self):
        s = IterableTwo('The world is peaceful')
        assert list(s) is not None
        assert isinstance(s, abc.Iterable)


    def test_iterable_generator(self):
        s = IterableGenerator('The world is splendid')
        assert list(s) is not None
        assert isinstance(s, abc.Iterable)
