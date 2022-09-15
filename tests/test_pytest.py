import pytest
from main import yandex_disc_request, get_request

fixture = [
    ('test_cat', 201),
    ('test_dir', 201),
    ('test_dir', 409)
]

fixture_get = [
    ('test_cat', 200),
    ('test_dir', 200),
    ('test_cataloge', 404)
]

class TestFunction:
    @pytest.mark.parametrize('path, res_request', fixture)
    def test_yandex_disc_request(self, path, res_request):
        result = yandex_disc_request(path)
        assert res_request == result

    @pytest.mark.parametrize('path, res_request', fixture_get)
    def test_get_request(self, path, res_request):
        result = get_request(path)
        assert res_request == result
