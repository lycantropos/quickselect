"""
Based on quickselect algorithm by Tony Hoare.

Reference:
    https://en.wikipedia.org/wiki/Quickselect
"""
from operator import (gt,
                      lt)
from typing import (Callable,
                    MutableSequence,
                    Optional)

from .hints import (Domain,
                    Key)


def nth_largest(sequence: MutableSequence[Domain],
                n: int,
                *,
                key: Optional[Key] = None) -> Domain:
    """
    Returns n-th largest element
    and partially sorts given sequence while searching.

    Time complexity:
        best: ``O(size)``
        average: ``O(size)``
        worst: ``O(size ** 2)``
    Memory complexity:
        best: ``O(1)``
        average: ``O(log size)``
        worst: ``O(size)``

    where ``size = len(sequence)``.

    :param sequence: sequence to search in
    :param n:
        index of the element to search for
        in the sequence sorted by key in descending order
        (e.g. ``n = 0`` corresponds to the maximum element)
    :param key:
        a single argument ordering function,
        if none is specified compares elements themselves
    :returns: n-th largest element of the sequence

    >>> sequence = list(range(-10, 11))
    >>> nth_largest(sequence, 0)
    10
    >>> nth_largest(sequence, 1)
    9
    >>> nth_largest(sequence, 19)
    -9
    >>> nth_largest(sequence, 20)
    -10
    >>> nth_largest(sequence, 0, key=abs)
    10
    >>> nth_largest(sequence, 1, key=abs)
    -10
    >>> nth_largest(sequence, 19, key=abs)
    1
    >>> nth_largest(sequence, 20, key=abs)
    0
    """
    return _select(sequence, n, 0, len(sequence) - 1, key, gt)


def nth_smallest(sequence: MutableSequence[Domain],
                 n: int,
                 *,
                 key: Optional[Key] = None) -> Domain:
    return _select(sequence, n, 0, len(sequence) - 1, key, lt)


def _select(sequence: MutableSequence[Domain],
            n: int,
            start: int,
            stop: int,
            key: Optional[Key],
            comparator: Callable[[Domain, Domain], bool]):
    while True:
        pivot_index = _partition(sequence, start, stop, key, comparator)
        if pivot_index < n:
            start = pivot_index + 1
        elif pivot_index > n:
            stop = pivot_index - 1
        else:
            return sequence[n]


def _partition(sequence: MutableSequence[Domain],
               start: int,
               stop: int,
               key: Optional[Key],
               comparator: Callable[[Domain, Domain], bool]) -> int:
    keys = (sequence
            if key is None
            else _SequenceKeyView(sequence, key))
    pivot = keys[(start + stop) // 2]
    while start <= stop:
        while comparator(keys[start], pivot):
            start += 1
        while comparator(pivot, keys[stop]):
            stop -= 1
        if keys[start] == keys[stop]:
            start += 1
        if start >= stop:
            break
        sequence[start], sequence[stop] = sequence[stop], sequence[start]
    return stop


class _SequenceKeyView:
    def __init__(self, sequence: MutableSequence[Domain], key: Key) -> None:
        self.sequence = sequence
        self.key = key

    def __getitem__(self, index: int) -> Domain:
        return self.key(self.sequence[index])
