from __future__ import annotations

from decimal import Decimal
from fractions import Fraction
from functools import partial
from operator import gt, lt
from typing import Any, Callable

from hypothesis import strategies as _st

from quickselect.hints import Domain

elements_strategies_factories: dict[
    type[Any], Callable[[], _st.SearchStrategy[Any]]
] = {
    Decimal: partial(_st.decimals, allow_nan=False, allow_infinity=False),
    float: partial(_st.floats, allow_nan=False, allow_infinity=False),
    Fraction: _st.fractions,
    int: _st.integers,
}
elements_strategies = _st.sampled_from(
    [factory() for factory in elements_strategies_factories.values()]
)
elements_lists = elements_strategies.flatmap(partial(_st.lists, min_size=1))


def to_numbers_lists_with_index(
    elements: list[Domain],
) -> _st.SearchStrategy[tuple[list[Domain], int]]:
    return _st.tuples(_st.just(elements), _st.integers(0, len(elements) - 1))


def to_numbers_lists_with_indices_triplet(
    elements: list[Domain],
) -> _st.SearchStrategy[tuple[list[Domain], tuple[int, int, int]]]:
    return _st.tuples(
        _st.just(elements),
        _st.lists(_st.integers(0, len(elements) - 1), min_size=3, max_size=3)
        .map(sorted)
        .map(tuple),
    )


elements_lists_with_index = elements_lists.flatmap(to_numbers_lists_with_index)
elements_lists_with_indices_triplets = elements_lists.flatmap(
    to_numbers_lists_with_indices_triplet
)


def identity(value: Domain) -> Domain:
    return value


comparators = _st.sampled_from([gt, lt])
keys = _st.sampled_from([identity, abs]) | _st.none()
