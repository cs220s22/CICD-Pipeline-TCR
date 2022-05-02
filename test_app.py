from app import app

def test_count():
    count = read_count()
    assert count == 1
