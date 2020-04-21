from decimal import Decimal
from fractions import Fraction
from functools import partial
from numbers import Real
from typing import (List,
                    Tuple)

from hypothesis import strategies

from quickselect.hints import Domain
from tests.utils import Strategy

elements_strategies_factories = {Decimal: partial(strategies.decimals,
                                                  allow_nan=False,
                                                  allow_infinity=False),
                                 float: partial(strategies.floats,
                                                allow_nan=False,
                                                allow_infinity=False),
                                 Fraction: strategies.fractions,
                                 int: strategies.integers}
elements_strategies = strategies.sampled_from(
        [factory()
         for factory in elements_strategies_factories.values()])
elements_lists = elements_strategies.flatmap(partial(strategies.lists,
                                                     min_size=1))


def to_numbers_lists_with_index(elements: List[Domain]
                                ) -> Strategy[Tuple[List[Domain], int]]:
    return strategies.tuples(strategies.just(elements),
                             strategies.integers(0, len(elements) - 1))


elements_lists_with_index = elements_lists.flatmap(to_numbers_lists_with_index)


def identity(value: Domain) -> Domain:
    return value


def square(number: Real) -> Real:
    return number * number


keys = strategies.sampled_from([identity, abs, square]) | strategies.none()
