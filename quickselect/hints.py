import typing as _t

Domain = _t.TypeVar('Domain')
Key = _t.Callable[[Domain], _t.Any]
Comparator = _t.Callable[[_t.Any, _t.Any], bool]
