from typing import MutableSequence, Tuple

from hypothesis import given

from quickselect.hints import Domain, KeyFunction
from quickselect.hoare import nth_smallest

from tests import strategies


@given(strategies.elements_lists_with_index, strategies.keys)
def test_properties(
    elements_with_index: Tuple[MutableSequence[Domain], int], key: KeyFunction
) -> None:
    elements, index = elements_with_index

    result = nth_smallest(elements, index, key=key)

    assert result in elements
    assert sorted(elements, key=key)[index] == result


@given(strategies.elements_lists, strategies.keys)
def test_first(elements: MutableSequence[Domain], key: KeyFunction) -> None:
    result = nth_smallest(elements, 0, key=key)

    assert result == (min(elements) if key is None else min(elements, key=key))
