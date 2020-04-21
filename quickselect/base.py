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

    +------------+-------------+-----------------+------------------+
    | complexity |    best     |     average     |      worst       |
    +------------+-------------+-----------------+------------------+
    |    time    | ``O(size)`` |   ``O(size)``   | ``O(size ** 2)`` |
    +------------+-------------+-----------------+------------------+
    |   memory   |  ``O(1)``   | ``O(log size)`` |   ``O(size)``    |
    +------------+-------------+-----------------+------------------+

    where ``size = len(sequence)``.

    :param sequence: sequence to search in
    :param n:
        index of the element to search for
        in the sequence sorted by key in descending order
        (e.g. ``n = 0`` corresponds to the maximum element)
    :param key:
        single argument ordering function,
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
    return select(sequence, n,
                  key=key,
                  comparator=gt)


def nth_smallest(sequence: MutableSequence[Domain],
                 n: int,
                 *,
                 key: Optional[Key] = None) -> Domain:
    """
    Returns n-th smallest element
    and partially sorts given sequence while searching.

    +------------+-------------+-----------------+------------------+
    | complexity |    best     |     average     |      worst       |
    +------------+-------------+-----------------+------------------+
    |    time    | ``O(size)`` |   ``O(size)``   | ``O(size ** 2)`` |
    +------------+-------------+-----------------+------------------+
    |   memory   |  ``O(1)``   | ``O(log size)`` |   ``O(size)``    |
    +------------+-------------+-----------------+------------------+

    where ``size = len(sequence)``.

    :param sequence: sequence to search in
    :param n:
        index of the element to search for
        in the sequence sorted by key in ascending order
        (e.g. ``n = 0`` corresponds to the minimum element)
    :param key:
        single argument ordering function,
        if none is specified compares elements themselves
    :returns: n-th smallest element of the sequence

    >>> sequence = list(range(-10, 11))
    >>> nth_smallest(sequence, 0)
    -10
    >>> nth_smallest(sequence, 1)
    -9
    >>> nth_smallest(sequence, 19)
    9
    >>> nth_smallest(sequence, 20)
    10
    >>> nth_smallest(sequence, 0, key=abs)
    0
    >>> nth_smallest(sequence, 1, key=abs)
    1
    >>> nth_smallest(sequence, 19, key=abs)
    -10
    >>> nth_smallest(sequence, 20, key=abs)
    10
    """
    return select(sequence, n,
                  key=key,
                  comparator=lt)


def select(sequence: MutableSequence[Domain],
           n: int,
           *,
           start: int = 0,
           stop: Optional[int] = None,
           key: Optional[Key] = None,
           comparator: Callable[[Domain, Domain], bool]) -> Domain:
    if stop is None:
        stop = len(sequence) - 1
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
