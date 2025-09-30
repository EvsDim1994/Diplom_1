import pytest
from praktikum.database import Database


class TestDataBase:

    @pytest.mark.parametrize('index, name, price', 
        [
            [0, "black bun", 100],
            [1, "white bun", 200],
            [2, "red bun", 300]
    
        ])    
    def test_available_buns(self, database: Database, index, name, price):
        assert database.available_buns()[index].get_name() == name
        assert database.available_buns()[index].get_price() == price


    @pytest.mark.parametrize('index, name, price, type', 
        [
            [0, "hot sauce", 100, "SAUCE"],
            [1, "sour cream", 200, "SAUCE"],
            [2, "chili sauce", 300, "SAUCE"],
            [3, "cutlet", 100, "FILLING"],
            [4, "dinosaur", 200, "FILLING"],
            [5, "sausage", 300, "FILLING"]
    
        ])    
    def test_available_ingredients(self, database: Database, index, name, price, type):
        assert database.available_ingredients()[index].get_name() == name
        assert database.available_ingredients()[index].get_price() == price
        assert database.available_ingredients()[index].get_type() == type
