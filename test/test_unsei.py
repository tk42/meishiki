import pytest
from datetime import datetime

from meishiki.unsei import convert_year_ratio


class TestUnseiMethods:
    def test_convert_year_ratio(self):
        assert convert_year_ratio(datetime(1926, 1, 6, 10, 55)) == [-11800, 0]
        assert convert_year_ratio(datetime(1926, 1, 6, 10, 56)) == [0, 10]
        assert convert_year_ratio(datetime(2022, 12, 7, 12, 46)) == [10, 0]
        with pytest.raises(IndexError):
            assert convert_year_ratio(datetime(2022, 12, 7, 12, 47)) == []
