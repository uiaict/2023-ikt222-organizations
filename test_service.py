import pytest
from service import Service

def test_identify_vulnerabilities():
    service = Service('Service1', ['Vulnerability1'])
    assert 'Vulnerability1' in service.identify_vulnerabilities()
