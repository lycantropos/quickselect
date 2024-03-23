from typing import Any, Callable, TypeVar

Domain = TypeVar('Domain')
Key = Callable[[Domain], Any]
Comparator = Callable[[Any, Any], bool]
