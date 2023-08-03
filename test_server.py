import pytest
from server import Server

def test_add_service():
    server = Server()
    server.add_service('Service1')
    assert 'Service1' in server.services

def test_remove_service():
    server = Server()
    server.add_service('Service1')
    server.remove_service('Service1')
    assert 'Service1' not in server.services
