from __future__ import annotations

import typing as _t

import typing_extensions as _te

from quickselect.hints import Domain, Key


class SequenceKeyView(_t.Sequence[Domain]):
    __slots__ = '_sequence', '_key'

    def __init__(
        self, _sequence: _t.MutableSequence[Domain], _key: Key[Domain], /
    ) -> None:
        self._key, self._sequence = _key, _sequence

    @_t.overload
    def __getitem__(self, index: int, /) -> Domain: ...

    @_t.overload
    def __getitem__(self, item: slice, /) -> _te.Self: ...

    def __getitem__(self, item: int | slice, /) -> _t.Any | _te.Self:
        return (
            SequenceKeyView(self._sequence[item], self._key)
            if isinstance(item, slice)
            else self._key(self._sequence[item])
        )

    def __len__(self, /) -> int:
        return len(self._sequence)
