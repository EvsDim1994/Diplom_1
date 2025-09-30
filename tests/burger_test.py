from unittest.mock import Mock

import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestBurger:

    def test_set_burger(self, create_bun: Bun, create_burger: Burger):
        create_burger.set_buns(create_bun)
        assert create_burger.bun == create_bun

    def test_add_ingredient(self, create_burger: Burger, create_ingredient: Ingredient):
        create_burger.add_ingredient(create_ingredient)
        assert len(create_burger.ingredients) == 1
        assert create_burger.ingredients[0] == create_ingredient

    def test_move_ingredient(self, create_burger: Burger, create_ingredient: Ingredient):
        create_burger.add_ingredient(create_ingredient)
        another_ingredient = Ingredient("соус", "сырный",  100)
        create_burger.add_ingredient(another_ingredient)
        create_burger.move_ingredient(0, 1)
        assert len(create_burger.ingredients) > 0
        assert create_burger.ingredients[1] == create_ingredient

    def test_remove_ingredient(self, create_burger: Burger, create_ingredient: Ingredient):
        create_burger.add_ingredient(create_ingredient)
        another_ingredient = Ingredient("соус", "сырный",  100)
        create_burger.add_ingredient(another_ingredient)
        create_burger.remove_ingredient(1)
        assert len(create_burger.ingredients) == 1
        assert create_burger.ingredients[0] == create_ingredient

    def test_get_price(self, create_burger: Burger):
        # Создаем моки объектов
        bun_mock = Mock(spec=Bun)
        ingredient1_mock = Mock(spec=Ingredient)
        ingredient2_mock = Mock(spec=Ingredient)
        
        # Настраиваем возвращаемые значения цен
        bun_mock.get_price.return_value = 2.50
        ingredient1_mock.get_price.return_value = 1.00
        ingredient2_mock.get_price.return_value = 0.75
        
        # добавляем ингредиенты
        create_burger.set_buns(bun_mock)
        create_burger.add_ingredient(ingredient1_mock)
        create_burger.add_ingredient(ingredient2_mock)
        
        # Ожидаемая цена: 2 булочки (2.50 * 2) + 2 ингредиента (1.00 + 0.75)
        expected_price = (2.50 * 2) + 1.00 + 0.75
        
        # Проверяем расчет цены
        assert abs(expected_price - create_burger.get_price()) < 0.01


    def test_get_price_with_empty_bun(self, create_burger: Burger):
        with pytest.raises(ValueError, match="Бургер не может быть собран без булки"):
            create_burger.get_price()

    def test_get_receipt(self, create_burger: Burger):
        # Создаем моки объектов
        bun_mock = Mock(spec=Bun)
        ingredient1_mock = Mock(spec=Ingredient)
        ingredient2_mock = Mock(spec=Ingredient)

        # Настраиваем возвращаемые значения для булки
        bun_mock.get_name.return_value = "Булочка"
        bun_mock.get_price.return_value = 2.50

        # Настраиваем возвращаемые значения для первого ингредиента
        ingredient1_mock.get_name.return_value = "Сыр"
        ingredient1_mock.get_type.return_value = INGREDIENT_TYPE_FILLING
        ingredient1_mock.get_price.return_value = 1.00  # предполагаемая цена

        # Настраиваем возвращаемые значения для второго ингредиента
        ingredient2_mock.get_name.return_value = "Соус"
        ingredient2_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingredient2_mock.get_price.return_value = 0.75  # предполагаемая цена

        # добавляем ингредиенты
        create_burger.set_buns(bun_mock)
        create_burger.add_ingredient(ingredient1_mock)
        create_burger.add_ingredient(ingredient2_mock)

        receipt_lines = create_burger.get_receipt().split('\n')
        expected_lines = [
            "(==== Булочка ====)",
            "= filling Сыр =",
            "= sauce Соус =", 
            "(==== Булочка ====)",
            "",
            "Price: 6.75"
        ]
        
        assert receipt_lines == expected_lines

    def test_get_receipt_with_empty_bun(self, create_burger: Burger):
        with pytest.raises(ValueError, match="Бургер не может быть собран без булки"):
            create_burger.get_receipt()
