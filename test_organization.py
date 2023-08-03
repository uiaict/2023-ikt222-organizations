import pytest
from organization import Organization

def test_add_building():
    org = Organization()
    org.add_building('Building1')
    assert 'Building1' in org.buildings

def test_remove_building():
    org = Organization()
    org.add_building('Building1')
    org.remove_building('Building1')
    assert 'Building1' not in org.buildings

def test_generate_report():
    org = Organization()
    org.add_building('Building1')
    report = org.generate_report()
    assert 'Building1' in report

def test_simulate_scenario():
    org = Organization()
    org.add_building('Building1')
    scenario = org.simulate_scenario('Fire')
    assert scenario is not None

def test_suggest_mitigation():
    org = Organization()
    org.add_building('Building1')
    mitigation = org.suggest_mitigation()
    assert mitigation is not None
