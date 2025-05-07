import pytest
from datetime import datetime
from meishiki.unsei import (
    convert_year_ratio,
    is_junun_gyakuun,
    find_kanshi_idx,
    is_kansatsu,
    is_tensen_chichu,
    append_daiun,
    append_nenun,
    build_unsei,
    Unsei,
)
from meishiki.errors import UnseiException
from meishiki.consts import kd, Sex
from meishiki.meishiki import build_meishiki


class TestUnseiMethods:
    def test_convert_year_ratio(self):
        assert convert_year_ratio(datetime(1926, 1, 6, 10, 55)) == [-11800, 0]
        assert convert_year_ratio(datetime(1926, 1, 6, 10, 56)) == [0, 10]
        assert convert_year_ratio(datetime(2022, 12, 7, 12, 46)) == [10, 0]
        with pytest.raises(IndexError):
            convert_year_ratio(datetime(2022, 12, 7, 12, 47))

    @pytest.mark.parametrize("sex,y_kan,expected", [
        (Sex.MALE.value, 0, 1),
        (Sex.FEMALE.value, 0, 0),
        (Sex.MALE.value, 1, 0),
        (Sex.FEMALE.value, 1, 1),
    ])
    def test_is_junun_gyakuun(self, sex, y_kan, expected):
        assert is_junun_gyakuun(sex, y_kan) == expected

    def test_find_kanshi_idx_valid_and_invalid(self):
        kan, shi = kd.sixty_kanshi[5]
        assert find_kanshi_idx(kan, shi, 1) == 6
        assert find_kanshi_idx(kan, shi, -1) == 4
        with pytest.raises(UnseiException):
            find_kanshi_idx(-1, -1, 1)

    @pytest.mark.parametrize("d_tsuhen,n_tsuhen,expected", [
        (6, 7, 1),
        (7, 6, 1),
        (0, 0, -1),
    ])
    def test_is_kansatsu(self, d_tsuhen, n_tsuhen, expected):
        assert is_kansatsu(d_tsuhen, n_tsuhen) == expected

    def test_is_tensen_chichu_all(self):
        for nisshi, shi in enumerate(kd.hitsuchu_rev):
            assert is_tensen_chichu(nisshi, 6, shi) == 1
            assert is_tensen_chichu(nisshi, 6, (shi + 1) % len(kd.hitsuchu_rev)) == -1
            assert is_tensen_chichu(nisshi, 5, shi) == -1

    def test_build_unsei_and_append(self):
        birthday = datetime(1926, 1, 6, 10, 55)
        meishiki = build_meishiki(birthday, Sex.MALE)
        unsei = build_unsei(meishiki)
        assert isinstance(unsei, Unsei)
        assert len(unsei.daiun) == 13
        assert all(len(item) == 13 for item in unsei.daiun)
        assert len(unsei.nenun) > 0
