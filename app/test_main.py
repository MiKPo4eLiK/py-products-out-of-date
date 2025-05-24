import datetime
from unittest import mock
from app.main import outdated_products


def test_outdated_products_with_mocks() -> None:
    products = [
        {"name": "salmon", "expiration_date":
            datetime.date(2022, 2, 10),
         "price": 600},
        {"name": "chicken", "expiration_date":
            datetime.date(2022, 2, 5),
         "price": 120},
        {"name": "duck", "expiration_date":
            datetime.date(2022, 2, 1),
         "price": 160}
    ]

    real_date = datetime.date

    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = real_date(2022, 2, 2)
        mock_date.side_effect = lambda *args, **kwargs: real_date(*args, **kwargs)
        result = outdated_products(products)
        assert result == ["duck"]

    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = real_date(2022, 2, 1)
        mock_date.side_effect = lambda *args, **kwargs: real_date(*args, **kwargs)
        result = outdated_products(products)
        assert result == []

    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = real_date(2022, 2, 11)
        mock_date.side_effect = lambda *args, **kwargs: real_date(*args, **kwargs)
        result = outdated_products(products)
        assert sorted(result) == sorted(["salmon", "chicken", "duck"])
