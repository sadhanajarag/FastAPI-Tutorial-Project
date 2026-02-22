import pytest
from app.logic import is_eligible_for_load


def test_eligible_user():
    assert is_eligible_for_load(60000,25,"employed") == True


def test_underage_user():
    assert is_eligible_for_load(60000,20,"employed") == False


def test_low_income():
    assert is_eligible_for_load(30000,25,'employed') == False

def test_unemplyed_user():
    assert is_eligible_for_load(60000,25,'unemployed') == False

def test_boundry_case():
    assert is_eligible_for_load(50000,21,'employed') == True