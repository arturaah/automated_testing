from pytest import approx

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
    
def add(a, b):
    return a + b

def test_add2():
    assert add(0.1, 0.2) == approx(0.3)
    