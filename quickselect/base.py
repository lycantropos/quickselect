from operator import (gt,
                      lt)
from typing import (Callable,
                    MutableSequence,
                    Optional)

from .hints import (Domain,
                    Key)


def nth_largest(elements: MutableSequence[Domain],
                n: int,
                *,
                key: Optional[Key] = None) -> Domain:
    return _select(elements, n, 0, len(elements) - 1, key, gt)


def nth_smallest(elements: MutableSequence[Domain],
                 n: int,
                 *,
                 key: Optional[Key] = None) -> Domain:
    return _select(elements, n, 0, len(elements) - 1, key, lt)


def _select(elements: MutableSequence[Domain],
            n: int,
            start: int,
            stop: int,
            key: Optional[Key],
            comparator: Callable[[Domain, Domain], bool]):
    while True:
        pivot_index = _partition(elements, start, stop, key, comparator)
        if pivot_index < n:
            start = pivot_index + 1
        elif pivot_index > n:
            stop = pivot_index - 1
        else:
            return elements[n]


def _partition(elements: MutableSequence[Domain],
               start: int,
               stop: int,
               key: Optional[Key],
               comparator: Callable[[Domain, Domain], bool]) -> int:
    keys = (elements
            if key is None
            else _SequenceKeyView(elements, key))
    pivot = keys[(start + stop) // 2]
    while start <= stop:
        while comparator(keys[start], pivot):
            start += 1
        while comparator(pivot, keys[stop]):
            stop -= 1
        if start >= stop:
            break
        if keys[start] == keys[stop]:
            start += 1
            continue
        elements[start], elements[stop] = elements[stop], elements[start]
    return stop


class _SequenceKeyView:
    def __init__(self, sequence: MutableSequence[Domain], key: Key) -> None:
        self.sequence = sequence
        self.key = key

    def __getitem__(self, index: int) -> Domain:
        return self.key(self.sequence[index])
