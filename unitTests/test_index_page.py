import pytest

def test_index_page():
    # Arrange
    testwert = 5
    soll_ergebnis = 6

    # Act
    ist_ergebnis = func(testwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis