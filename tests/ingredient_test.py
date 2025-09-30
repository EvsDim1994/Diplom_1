class TestIngredient:

    def test_get_type(self, create_ingredient):
        assert create_ingredient.get_type() == "соус"

    def test_get_name(self, create_ingredient):
        assert create_ingredient.get_name() == "1000 островов"

    def test_get_price(self, create_ingredient):
        assert create_ingredient.get_price() == 1.5
