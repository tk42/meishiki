from typing import List
from datetime import datetime
from dataclasses import field, dataclass

from meishiki.consts import kd
from meishiki.errors import UnseiException
from meishiki.meishiki import is_setsuiri, Meishiki


@dataclass
class Unsei:

    daiun: List[int] = field(default_factory=list)
    nenun: List[int] = field(default_factory=list)


def convert_year_ratio(birthday):

    # ＜機能＞
    # 生年月日から前の節入日までの日数と、生年月日から次の節入日までの日数との比を、
    # 10年に占める割合に直す。
    # 例：8日：22日→3年：7年
    # ＜入力＞
    #   - brithday（datetime）：生年月日
    # ＜出力＞
    #   - year_ratio_list（list）：10年に占める割合

    p = is_setsuiri(birthday, birthday.month)
    for i, s in enumerate(kd.setsuiri):
        if (s[0] == birthday.year) and (s[1] == birthday.month):
            if not p:
                k = kd.setsuiri[i + 1]
                previous_setsuiri = datetime(year=s[0], month=s[1], day=s[2], hour=s[3], minute=s[4])
                next_setsuiri = datetime(year=k[0], month=k[1], day=k[2], hour=k[3], minute=k[4])
            else:
                k = kd.setsuiri[i - 1]
                previous_setsuiri = datetime(year=k[0], month=k[1], day=k[2], hour=k[3], minute=k[4])
                next_setsuiri = datetime(year=s[0], month=s[1], day=s[2], hour=s[3], minute=s[4])
            break

    diff_previous = birthday - previous_setsuiri  # 生年月日から前の節入日までの日数
    diff_next = next_setsuiri - birthday  # 生年月日から次の節入日までの日数

    # ３日間を１年に置き換えるので、３除した値を丸める
    p_year = round((diff_previous.days + (diff_previous.seconds / 60 / 60 / 24)) / 3)
    n_year = round((diff_next.days + (diff_next.seconds / 60 / 60 / 24)) / 3)

    year_ratio_list = [p_year, n_year]

    return year_ratio_list


def is_junun_gyakuun(sex, y_kan):

    # ＜機能＞
    # 大運が順運か逆運かを判定する
    # ＜入力＞
    #   - y_kan（int）：年柱天干の番号
    #   - self.sex（int）：性別の番号
    # ＜出力＞
    #   - 順運（1）または逆運（0）の二値
    # ＜異常検出＞
    # 取得できなかった場合はエラーメッセージを出力して強制終了する

    if (((y_kan % 2) == 0) and (sex == 0)) or (((y_kan % 2) == 1) and (sex == 1)):
        return 1  # 年柱天干が陽干の男命 or 年柱天干が陰干の女命は、順運

    elif (((y_kan % 2) == 1) and (sex == 0)) or (((y_kan % 2) == 0) and (sex == 1)):
        return 0  # 年柱天干が陽干の女命 or 年柱天干が陰干の男命は、逆運

    else:
        raise UnseiException("大運の順逆を判定できませんでした。")


def find_kanshi_idx(kan, shi, p):

    # 六十干支表から所定の干支のインデクスを返す

    for idx, sk in enumerate(kd.sixty_kanshi):
        if (sk[0] == kan) and (sk[1] == shi):
            return idx + p

    raise UnseiException("干支が見つかりませんでした。")


def is_kango(tenkan_zokan, kan):

    for i, k in enumerate(tenkan_zokan):
        if k == kd.kango[kan]:
            return i
    return -1


def is_kango_y(tenkan_zokan, d_kan, kan):

    for i, k in enumerate(tenkan_zokan):
        if k == kd.kango[kan]:
            return i
    if d_kan == kd.kango[kan]:
        return len(tenkan_zokan)
    return -1


def is_shigo(chishi, shi):

    for i, s in enumerate(chishi):
        if s == kd.shigo[shi]:
            return i
    return -1


def is_shigo_y(chishi, d_shi, shi):

    for i, s in enumerate(chishi):
        if s == kd.shigo[shi]:
            return i
    if d_shi == kd.shigo[shi]:
        return len(chishi)
    return -1


def is_hogo(chishi, shi):

    # 方合の有無を判定する
    for i, h in enumerate(kd.hogo):
        hg = [j for j in h[0]]
        if shi in hg:
            hg.remove(shi)
            if (hg[0] in chishi) and (hg[1] in chishi):
                return i
    return -1


def is_hogo_y(chishi, d_shi, shi):

    for i, h in enumerate(kd.hogo):
        hg = [j for j in h[0]]
        if shi in hg:
            hg.remove(shi)
            if d_shi in hg:
                hg.remove(d_shi)
                for c in chishi:
                    if c in hg:
                        return i
    return is_hogo(chishi, shi)


def is_sango(chishi, shi):

    # 三合の有無を判定する
    for i, s in enumerate(kd.sango):
        sg = [j for j in s[0]]
        if shi in sg:
            sg.remove(shi)
            if (sg[0] in chishi) and (sg[1] in chishi):
                return i
    return -1


def is_sango_y(chishi, d_shi, shi):

    for i, h in enumerate(kd.sango):
        hg = [j for j in h[0]]
        if shi in hg:
            hg.remove(shi)
            if d_shi in hg:
                hg.remove(d_shi)
                for c in chishi:
                    if c in hg:
                        return i
    return is_sango(chishi, shi)


def is_hankai(chishi, shi):

    # 半会の有無を判定する
    for i, h in enumerate(kd.hankai):
        if ((h[0][0] in chishi) and (h[0][1] in [shi])) or ((h[0][0] in [shi]) and (h[0][1] in chishi)):
            return i
    return -1


def is_hankai_y(chishi, d_shi, shi):

    for i, h in enumerate(kd.hankai):
        if (
            ((h[0][0] in chishi) and (h[0][1] in [shi]))
            or ((h[0][0] in [shi]) and (h[0][1] in chishi))
            or ((h[0][0] in [shi]) and (h[0][1] in [d_shi]))
            or ((h[0][0] in [d_shi]) and (h[0][1] in [shi]))
        ):
            return i
    return -1


def is_tensen_chichu(nisshi, tsuhen, shi):

    if (shi == kd.hitsuchu_rev[nisshi]) and (tsuhen == 6):
        return 1
    return -1


def is_chu(chishi, shi):

    ch = [chishi[0]] + [-1] + [chishi[2]] + [chishi[3]]
    for i, s in enumerate(ch):
        if s == kd.hitsuchu_nodir[shi]:
            return i
    return -1


def is_chu_y(chishi, d_shi, shi):

    ch = chishi + [d_shi]
    for i, s in enumerate(ch):
        if s == kd.hitsuchu_nodir[shi]:
            return i
    return -1


def is_kei(chishi, shi):

    for i, s in enumerate(chishi):
        if s == kd.kei[shi]:
            return i
    return -1


def is_kei_y(chishi, d_shi, shi):

    ch = chishi + [d_shi]
    for i, s in enumerate(ch):
        if s == kd.kei[shi]:
            return i
    return -1


def is_gai_y(chishi, d_shi, shi):

    ch = chishi + [d_shi]
    for i, s in enumerate(ch):
        if s == kd.gai[shi]:
            return i
    return -1


def is_gai(chishi, shi):

    for i, s in enumerate(chishi):
        if s == kd.gai[shi]:
            return i
    return -1


def is_kansatsu(d_tsuhen, n_tsuhen):

    if (d_tsuhen == 6 and n_tsuhen == 7) or (d_tsuhen == 7 and n_tsuhen == 6):
        return 1
    return -1


def append_daiun(meishiki):

    # ＜機能＞
    # 大運を命式に追加する

    daiun = []
    year_ratio_list = convert_year_ratio(meishiki.birthday)

    if is_junun_gyakuun(meishiki.sex, meishiki.nenchu[0]):  # 順運か逆運か？
        ry = year_ratio_list[1]  # 次の節入日が立運の起算日
        p = 1  # 六十干支表を順にたどる
    else:
        ry = year_ratio_list[0]  # 前の節入日が立運の起算日
        p = -1  # 六十干支表を逆にたどる

    idx = find_kanshi_idx(meishiki.getchu[0], meishiki.getchu[1], p)

    for n in list(range(10, 140, 10)):

        if idx >= 60:
            idx = 0
        kan, shi = kd.sixty_kanshi[idx]
        tsuhen = kd.kan_tsuhen[meishiki.nikkan].index(kan)

        kango = is_kango(meishiki.tenkan + meishiki.zokan, kan)  # 干合
        shigo = is_shigo(meishiki.chishi, shi)  # 支合

        hogo = is_hogo(meishiki.chishi, shi)  # 方合
        sango = is_sango(meishiki.chishi, shi)  # 三合
        if sango == -1:
            hankai = is_hankai(meishiki.chishi, shi)  # 半会
        else:
            hankai = -1
        tc = is_tensen_chichu(meishiki.nitchu[1], tsuhen, shi)  # 天戦地冲
        if tc == -1:
            chu = is_chu(meishiki.chishi, shi)  # 冲
        else:
            chu = -1
        kei = is_kei(meishiki.chishi, shi)  # 刑
        gai = is_gai(meishiki.chishi, shi)  # 害

        daiun.append([ry, kan, shi, tsuhen, kango, shigo, hogo, sango, hankai, tc, chu, kei, gai])
        ry += 10
        idx += p

    return daiun


def append_nenun(meishiki, daiun):

    # ＜機能＞
    # 年運を命式に追加する

    nenun = []
    idx = (meishiki.birthday.year - 3) % 60 - 1  # + self.meishiki.is_setsuiri(2)
    ry = daiun[0][0]
    d_idx = 0

    for n in list(range(0, 120)):
        kan, shi = kd.sixty_kanshi[idx]
        tsuhen = kd.kan_tsuhen[meishiki.nikkan].index(kan)

        if (n != ry) and (n % 10 == ry):
            d_idx += 1

        if n >= ry:

            d_kan = daiun[d_idx][1]
            d_shi = daiun[d_idx][2]

            kango = is_kango_y(meishiki.tenkan + meishiki.zokan, d_kan, kan)  # 干合
            shigo = is_shigo_y(meishiki.chishi, d_shi, shi)  # 支合

            if daiun[d_idx][6] == -1:
                hogo = is_hogo_y(meishiki.chishi, d_shi, shi)  # 方号
            else:
                hogo = -1
            if daiun[d_idx][7] == -1:
                sango = is_sango_y(meishiki.chishi, d_shi, shi)  # 三合
            else:
                sango = -1
            if sango == -1:
                hankai = is_hankai_y(meishiki.chishi, d_shi, shi)  # 半会
            else:
                hankai = -1

            tc1 = is_tensen_chichu(meishiki.nitchu[1], tsuhen, shi)  # 天戦地冲（命式）
            tc2 = is_tensen_chichu(d_shi, kd.kan_tsuhen[d_kan].index(kan), shi)  # 天戦地冲（大運）
            tc = 1 if tc1 == 1 else 2 if tc2 == 1 else -1

            if tc == -1:
                chu = is_chu_y(meishiki.chishi, d_shi, shi)  # 冲
            else:
                chu = -1
            kei = is_kei_y(meishiki.chishi, d_shi, shi)  # 刑
            gai = is_gai_y(meishiki.chishi, d_shi, shi)  # 害

            kansatsu = is_kansatsu(daiun[d_idx][3], tsuhen)  # 官殺混雑

            nenun.append([n, kan, shi, tsuhen, kango, shigo, hogo, sango, hankai, tc, chu, kei, gai, kansatsu])

        idx += 1
        if idx >= 60:
            idx = 0

    return nenun


def build_unsei(meishiki: Meishiki) -> Unsei:

    # 大運を得る
    daiun = append_daiun(meishiki)

    # 年運を得る
    nenun = append_nenun(meishiki, daiun)

    return Unsei(daiun, nenun)
