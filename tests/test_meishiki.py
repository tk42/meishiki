from datetime import datetime
from meishiki.meishiki import find_zokan, build_meishiki
from meishiki.consts import kd, Sex


class TestMeishikiMethods:
    def test_find_zokan(self):
        assert find_zokan(datetime(1926, 1, 6, 10, 55), 0) == 9
        assert find_zokan(datetime(1926, 1, 6, 10, 56), 0) == 8
        assert find_zokan(datetime(1926, 1, 6, 10, 55), 6) == 3
        assert find_zokan(datetime(1926, 1, 6, 10, 56), 6) == 2
        assert find_zokan(datetime(2022, 12, 7, 12, 46), 0) == 9
        assert find_zokan(datetime(2022, 12, 7, 12, 47), 0) == 8
        assert find_zokan(datetime(2022, 12, 7, 12, 46), 6) == 3
        assert find_zokan(datetime(2022, 12, 7, 12, 47), 6) == 2

    def test_twelve_fortune_contains_teio(self):
        meishiki = build_meishiki(datetime(1995, 11, 28, 12, 0), Sex.FEMALE)
        fortune_names = [kd.twelve_fortune[i] for i in meishiki.twelve_fortune]
        assert ["帝", "帝", "帝", "絶"] == fortune_names
