import pytest

from Application.api import bills


@pytest.fixture
def client():
    pass


def test_tva_1():
    assert 0.21 == bills.calculate_vat(1)


def test_tva_2():
    assert 0.42 == bills.calculate_vat(2)


def test_total_1():
    assert 2.42 == bills.total_with_vat(2)


def test_total_2():
    assert 1.21 == bills.total_with_vat(1)
