import pytest
from network import Network

def test_add_server():
    network = Network()
    network.add_server('Server1')
    assert 'Server1' in network.servers

def test_remove_server():
    network = Network()
    network.add_server('Server1')
    network.remove_server('Server1')
    assert 'Server1' not in network.servers

def test_identify_network_type():
    network = Network('Public')
    assert network.identify_network_type() == 'Public'
