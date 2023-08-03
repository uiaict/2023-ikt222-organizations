import pytest
from building import Building

def test_add_room():
    building = Building()
    building.add_room('Room1')
    assert 'Room1' in building.rooms

def test_remove_room():
    building = Building()
    building.add_room('Room1')
    building.remove_room('Room1')
    assert 'Room1' not in building.rooms

def test_locate_fire_exits():
    building = Building()
    building.add_fire_exit('Exit1')
    assert 'Exit1' in building.fire_exits

def test_calculate_total_value():
    building = Building()
    building.add_room('Room1')
    building.rooms['Room1'].add_peripheral('Computer', 1000)
    assert building.calculate_total_value() == 1000
