from app import app, read_count

def test_count():
    app.config['TESTING'] = True
    assert read_count() == 1
