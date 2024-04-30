#!/usr/bin/python3

class LockedClass:
    def __setattr__(self,name, value):
        if hasattr(self, name) and name != 'first_name':
            raise AttributeError("Cannot modify existing attributes")
        super().__setattr__(name, value)

