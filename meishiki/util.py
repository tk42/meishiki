from datetime import datetime as dt

from meishiki.errors import ConvertWarekiException

WAREKI_START = {"令和": dt(2019, 5, 1), "平成": dt(1989, 1, 8), "昭和": dt(1926, 12, 25)}


def convert_to_wareki(y_m_d):
    """西暦の年月日を和暦の年に変換する."""
    try:
        if WAREKI_START["令和"] <= y_m_d:
            reiwa_year = WAREKI_START["令和"].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = "令和"
        elif WAREKI_START["平成"] <= y_m_d:
            reiwa_year = WAREKI_START["平成"].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = "平成"
        elif WAREKI_START["昭和"] <= y_m_d:
            reiwa_year = WAREKI_START["昭和"].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = "昭和"
        else:
            return "昭和以前"

        if len(str(year)) == 1:
            year = " " + str(year)
        else:
            year = str(year)

        if year == " 1":
            year = "元"

        return era_str + year + "年"
    except ValueError as e:
        raise ConvertWarekiException(e)
