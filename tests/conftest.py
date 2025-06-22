from datetime import datetime

import pytest

from meishiki.meishiki import build_meishiki
from meishiki.unsei import build_unsei
from meishiki.consts import Sex


@pytest.fixture
def sample():
    """2000-01-01 12:00 男性のサンプル"""
    birthday = datetime(2000, 1, 1, 12, 0)
    meishi = build_meishiki(birthday, sex=Sex.MALE)
    unsei = build_unsei(meishi)
    return meishi, unsei


@pytest.fixture
def sample2():
    """1989-10-28 12:00 男性のサンプル"""
    birthday = datetime(1989, 10, 28, 12, 0)
    meishi = build_meishiki(birthday, sex=Sex.MALE)
    unsei = build_unsei(meishi)
    return meishi, unsei


@pytest.fixture
def sample3():
    """1988-08-09 12:00 男性のサンプル"""
    birthday = datetime(1988, 8, 9, 12, 0)
    meishi = build_meishiki(birthday, sex=Sex.MALE)
    unsei = build_unsei(meishi)
    return meishi, unsei
