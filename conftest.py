import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient


@pytest.fixture(scope='function')
def create_bun():
    return Bun("Булка", 1.5)

@pytest.fixture(scope='function')
def create_ingredient():
    return Ingredient("соус", "1000 островов",  1.5)

@pytest.fixture(scope='function')
def database():
    return Database()

@pytest.fixture(scope='function')
def create_burger():
    return Burger()
