#!/usr/bin/python3

class LockedClass:
    __slots__ = ('first_name',)

    def __getattr__(self, name, value):
        if not hasattr(self, 'first_name') and name != 'first_name':
            raise AttributeError(f"Cannot create new instance attribute '{name}'")
        super().__getattr__(name, value)
