from collections import namedtuple

"""Namedtuples example"""
Room = namedtuple('Room', ['room_size', 'price', 'sunlight', 'flat_rooms'])

flat = Room(30, 600, True, 3)

if flat.price <= 620:
    print('take it!')