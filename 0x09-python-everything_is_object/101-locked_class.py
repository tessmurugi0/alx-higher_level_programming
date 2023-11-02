#!/usr/bin/python3
"""Locked Class"""
class LockedClass:
    """
    cannot instantiute unless
    attribute is 'first_name'
    """
    __slots__ = ["first_name"]
