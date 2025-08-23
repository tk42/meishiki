import pytest
from datetime import datetime, timedelta
from meishiki.unsei import (
    build_unsei, convert_year_ratio, is_junun_gyakuun, is_tensen_chichu,
    calculate_monthly_fortune, calculate_daily_fortune, calculate_weekly_fortune,
    find_kanshi_idx, is_kansatsu, append_daiun, append_nenun, Unsei
)
from meishiki.errors import UnseiException
from meishiki.consts import kd, Sex
from meishiki.meishiki import build_meishiki


class TestUnseiMethods:
    # setsuiri が正しく判定されることを確認する
    # setsuiri を更新したら、このテストも更新する
    def test_convert_year_ratio(self):
        assert convert_year_ratio(datetime(1926, 1, 6, 10, 55)) == [-12287, 0]
        assert convert_year_ratio(datetime(1926, 1, 6, 10, 56)) == [0, 10]
        assert convert_year_ratio(datetime(2022, 12, 7, 12, 46)) == [10, 0]
        assert convert_year_ratio(datetime(2026, 12, 7, 11, 53)) == [10, 0]
        with pytest.raises(IndexError):
            # 「現在の節入り日」を過ぎた日時を渡すと、IndexError が発生することを確認する
            convert_year_ratio(datetime(2026, 12, 7, 11, 54))

    @pytest.mark.parametrize("sex,y_kan,expected", [
        (Sex.MALE, 0, 1),
        (Sex.FEMALE, 0, 0),
        (Sex.MALE, 1, 0),
        (Sex.FEMALE, 1, 1),
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

    def test_calculate_monthly_fortune(self):
        birthday = datetime(1978, 9, 26, 13, 51)
        meishiki = build_meishiki(birthday, Sex.MALE)
        
        # 2024年1月の月運を計算
        monthly_fortune = calculate_monthly_fortune(meishiki, 2024, 1)
        
        assert isinstance(monthly_fortune, dict)
        assert monthly_fortune['year'] == 2024
        assert monthly_fortune['month'] == 1
        assert 'kan' in monthly_fortune
        assert 'shi' in monthly_fortune
        assert 'tsuhen' in monthly_fortune
        assert isinstance(monthly_fortune['kan'], int)
        assert isinstance(monthly_fortune['shi'], int)
        assert isinstance(monthly_fortune['tsuhen'], int)

    def test_calculate_daily_fortune(self):
        birthday = datetime(1978, 9, 26, 13, 51)
        meishiki = build_meishiki(birthday, Sex.MALE)
        
        # 2024年1月1日の日運を計算
        target_date = datetime(2024, 1, 1)
        daily_fortune = calculate_daily_fortune(meishiki, target_date)
        
        assert isinstance(daily_fortune, dict)
        assert daily_fortune['date'] == target_date
        assert 'kan' in daily_fortune
        assert 'shi' in daily_fortune
        assert 'tsuhen' in daily_fortune
        assert isinstance(daily_fortune['kan'], int)
        assert isinstance(daily_fortune['shi'], int)
        assert isinstance(daily_fortune['tsuhen'], int)

    def test_calculate_weekly_fortune(self):
        birthday = datetime(1978, 9, 26, 13, 51)
        meishiki = build_meishiki(birthday, Sex.MALE)
        
        # 2024年1月1日から1週間の週運を計算
        week_start = datetime(2024, 1, 1)
        weekly_fortune = calculate_weekly_fortune(meishiki, week_start)
        
        assert isinstance(weekly_fortune, list)
        assert len(weekly_fortune) == 7
        
        # 各日の運勢データを確認
        for i, daily_data in enumerate(weekly_fortune):
            assert isinstance(daily_data, dict)
            expected_date = week_start + timedelta(days=i)
            assert daily_data['date'] == expected_date
            assert 'kan' in daily_data
            assert 'shi' in daily_data
            assert 'tsuhen' in daily_data
