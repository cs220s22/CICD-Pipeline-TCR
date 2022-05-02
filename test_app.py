from app import app

def test_count():
    app.config['TESTING'] = True
    assert read_count() == 1
