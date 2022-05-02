import pytest
from app import app

def test_count():
    app.config['TESTING'] = True
    count = app.read_count()
    assert count == 1
