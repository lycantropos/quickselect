from __future__ import annotations

from typing import Any, MutableSequence

from hypothesis import given

from quickselect.floyd_rivest import nth_smallest
from quickselect.hints import Key

from tests.strategies import (
    element_list_strategy,
    element_list_with_index_strategy,
    key_strategy,
)


@given(element_list_with_index_strategy, key_strategy)
def test_properties(
    elements_with_index: tuple[MutableSequence[Any], int], key: Key[Any]
) -> None:
    elements, index = elements_with_index

    result = nth_smallest(elements, index, key=key)

    assert result in elements
    assert sorted(elements, key=key)[index] == result


@given(element_list_strategy, key_strategy)
def test_first(elements: MutableSequence[Any], key: Key[Any] | None) -> None:
    result = nth_smallest(elements, 0, key=key)

    assert result == (min(elements) if key is None else min(elements, key=key))
