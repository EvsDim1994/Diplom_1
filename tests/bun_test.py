class TestBun:

    def test_get_name(self, create_bun):
        assert create_bun.get_name() == "Булка"

    def test_get_price(self, create_bun):
        assert create_bun.get_price() ==  1.5
