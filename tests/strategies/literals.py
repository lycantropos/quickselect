from __future__ import annotations

from decimal import Decimal
from fractions import Fraction
from functools import partial
from operator import gt, lt
from typing import Any, Callable

from hypothesis import strategies as _st

from quickselect.hints import Domain

element_strategy_factories: dict[
    type[Any], Callable[[], _st.SearchStrategy[Any]]
] = {
    int: _st.integers,
    float: partial(_st.floats, allow_nan=False, allow_infinity=False),
    Fraction: _st.fractions,
    Decimal: partial(_st.decimals, allow_nan=False, allow_infinity=False),
}
MAX_RANGE_ENDPOINT = 1_000


def to_range(start_with_increment: tuple[int, int]) -> range:
    start, increment = start_with_increment
    return range(start, start + increment)


range_strategy = _st.tuples(
    _st.integers(-MAX_RANGE_ENDPOINT, MAX_RANGE_ENDPOINT),
    _st.integers(0, MAX_RANGE_ENDPOINT),
).map(to_range)
element_list_strategy = _st.one_of(
    [
        _st.lists(factory(), min_size=1)
        for factory in element_strategy_factories.values()
    ]
    + [range_strategy.map(list), range_strategy.map(reversed).map(list)]
)


def to_number_list_with_index(
    elements: list[Domain], offset: int
) -> tuple[list[Domain], int]:
    return elements, offset_to_index(offset, elements)


def to_number_list_with_index_triplet(
    elements: list[Domain],
    first_offset: int,
    second_offset: int,
    third_offset: int,
) -> tuple[list[Domain], tuple[int, int, int]]:
    first_index, second_index, third_index = sorted(
        [
            offset_to_index(offset, elements=elements)
            for offset in [first_offset, second_offset, third_offset]
        ]
    )
    return elements, (first_index, second_index, third_index)


def offset_to_index(offset: int, elements: list[Domain]) -> int:
    return offset % len(elements)


offset_strategy = _st.integers(0)
element_list_with_index_strategy = _st.builds(
    to_number_list_with_index, element_list_strategy, offset_strategy
)
element_list_with_index_triplet_strategy = _st.builds(
    to_number_list_with_index_triplet,
    element_list_strategy,
    offset_strategy,
    offset_strategy,
    offset_strategy,
)


def identity(value: Domain) -> Domain:
    return value


comparator_strategy = _st.sampled_from([gt, lt])
key_strategy = _st.sampled_from([identity, abs]) | _st.none()
