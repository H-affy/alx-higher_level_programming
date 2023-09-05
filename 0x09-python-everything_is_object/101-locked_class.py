#!/usr/bin/python3
"""defines a locked class"""


class LockedClass:
    """It prevent user from instantiating new lockedclass
    attribute for anything but attributes called 'first_name'
    """

    __slots__ = ["first_name"]
