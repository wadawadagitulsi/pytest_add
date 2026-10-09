from add import additions

def test_calculate_positive():
    assert additions(10,20) == 30

def test_calculate_zero():
        assert additions(0,15) == 15

def test_calculate_negative():
            assert additions(-10, 20) == 10   