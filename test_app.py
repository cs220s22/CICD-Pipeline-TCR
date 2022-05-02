from app import app

def test_count():
    count = app.read_count()
    assert count == 1
