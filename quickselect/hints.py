from typing import (Any,
                    Callable,
                    TypeVar)

Domain = TypeVar('Domain')
Key = Callable[[Domain], Any]
Comparator = Callable[[Domain, Domain], bool]
