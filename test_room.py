import pytest
from room import Room

def test_add_peripheral():
    room = Room()
    room.add_peripheral('Computer', 1000)
    assert 'Computer' in room.peripherals

def test_remove_peripheral():
    room = Room()
    room.add_peripheral('Computer', 1000)
    room.remove_peripheral('Computer')
    assert 'Computer' not in room.peripherals

def test_calculate_room_size():
    room = Room(10, 10)
    assert room.calculate_room_size() == 100

def test_identify_door_type():
    room = Room()
    room.add_door('Door1', 'Wooden')
    assert room.doors['Door1'] == 'Wooden'
