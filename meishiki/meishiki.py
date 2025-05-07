from typing import List
from datetime import datetime, timedelta
from dataclasses import field, dataclass

from meishiki.consts import kd, Sex
from meishiki.errors import MeishikiException


@dataclass
class Meishiki:

    birthday: datetime
    sex: Sex

    tenkan: List[int] = field(default_factory=list)
    chishi: List[int] = field(default_factory=list)
    zokan: List[int] = field(default_factory=list)

    nenchu: List[int] = field(default_factory=list)
    getchu: List[int] = field(default_factory=list)
    nitchu: List[int] = field(default_factory=list)
    jichu: List[int] = field(default_factory=list)
    nikkan: int = 0

    gogyo: List[int] = field(default_factory=list)
    inyo: List[int] = field(default_factory=list)
    getsurei: int = 0

    tsuhen: List[int] = field(default_factory=list)
    twelve_fortune: List[int] = field(default_factory=list)

    kango: List[int] = field(default_factory=list)
    shigo: List[int] = field(default_factory=list)
    hogo: List[int] = field(default_factory=list)
    sango: List[int] = field(default_factory=list)
    hankai: List[int] = field(default_factory=list)
    hitsuchu: List[int] = field(default_factory=list)
    kei: List[int] = field(default_factory=list)
    gai: List[int] = field(default_factory=list)
    kubo: List[int] = field(default_factory=list)
    choko: str = ""

    youjin: int = 0
    kaigou: int = 0


def is_setsuiri(birthday, month):

    # ＜機能＞
    # birthday の年月日が、month で与えられた月に対して節入りしているか否かを判定する
    # ＜入力＞
    #   - birthday（datetime）：誕生日
    #   - month（int）：基準となる月
    # ＜出力＞
    #   - 節入りしている（0）またはしていない（-1）の二値
    # ＜異常検出＞
    # 判定不可能の場合はエラーメッセージを出力して強制終了する

    for s in kd.setsuiri:
        if (s[0] == birthday.year) and (s[1] == month):
            _setsuiri = datetime(year=s[0], month=s[1], day=s[2], hour=s[3], minute=s[4])
            if _setsuiri < birthday:
                return 0  # 節入りしている
            else:
                return -1  # 節入りしていない

    raise MeishikiException("節入りを判定できませんでした。")


def find_year_kanshi(birthday):

    # ＜機能＞
    # birthday の生年月日の年干支を取得する
    # ＜入力＞
    #   - birthday（datetime）：誕生日
    # ＜出力＞
    #   - y_kan（int）：年干の番号
    #   - y_shi（int）：年支の番号
    # ＜異常検出＞
    # 取得できなかった場合はエラーメッセージを出力して強制終了する

    sixty_kanshi_idx = (birthday.year - 3) % 60 - 1 + is_setsuiri(birthday, 2)
    try:
        y_kan, y_shi = kd.sixty_kanshi[sixty_kanshi_idx]
        return y_kan, y_shi
    except Exception as e:
        raise MeishikiException("年干支の計算で例外が送出されました。") from e


def find_month_kanshi(birthday, y_kan):

    # ＜機能＞
    # birthday の生年月日の月干支を取得する
    # ＜入力＞
    #   - birthday（datetime）：誕生日
    #   - y_kan（int）：年干の番号
    # ＜出力＞
    #   - m_kan（int）：月干の番号
    #   - m_shi（int）：月支の番号
    # ＜異常検出＞
    # 取得できなかった場合はエラーメッセージを出力して強制終了する

    month = birthday.month - 1 + is_setsuiri(birthday, birthday.month)
    try:
        m_kan, m_shi = kd.month_kanshi[y_kan][month]
        return m_kan, m_shi
    except Exception as e:
        raise MeishikiException("月干支の計算で例外が送出されました。") from e


def find_day_kanshi(birthday):

    # ＜機能＞
    # birthday で与えられた生年月日の日干支を取得する
    # ＜入力＞
    #   - birthday（daytime）：誕生日
    # ＜出力＞
    #   - d_kan（int）：日干の番号
    #   - d_shi（int）：日支の番号
    # ＜異常検出＞
    # 取得できなかった場合はエラーメッセージを出力して強制終了する

    try:
        d = birthday.day + kd.kisu_table[birthday.year - 1926][birthday.month - 1] - 1
    except Exception as e:
        raise MeishikiException("生年は1926年以降でなければなりません。") from e

    if d >= 60:
        d -= 60  # d が 60 を超えたら 60 を引く

    try:
        d_kan, d_shi = kd.sixty_kanshi[d]
        return d_kan, d_shi
    except Exception as e:
        raise MeishikiException("日干支の計算で例外が送出されました。") from e


def find_time_kanshi(birthday, d_kan):

    # ＜機能＞
    # birthday で与えられた生年月日の時干支を取得する
    # ＜入力＞
    #   - birthday（datetime）：誕生日
    #   - d_kan（int）：日干の番号
    # ＜出力＞
    #   - t_kan（int）：時干の番号
    #   - t_shi（int）：時支の番号
    # ＜異常検出＞
    # 取得できなかった場合はエラーメッセージを出力して強制終了する

    time_span = [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 24]

    for i in range(len(time_span) - 1):

        from_dt = datetime(year=birthday.year, month=birthday.month, day=birthday.day, hour=time_span[i], minute=0)

        if (i == 0) or (i == len(time_span)):
            to_dt = from_dt + timedelta(hours=0, minutes=59)
        else:
            to_dt = from_dt + timedelta(hours=1, minutes=59)

        if from_dt <= birthday <= to_dt:
            try:
                t_kan, t_shi = kd.time_kanshi[d_kan][i]
                return t_kan, t_shi
            except Exception as e:
                raise MeishikiException("時干支の計算で例外が送出されました。") from e

    raise MeishikiException("時干支を得られませんでした。")


def find_zokan(birthday, shi):

    # ＜機能＞
    # birthday で与えられた生年月日の shi に対応する蔵干を取得する
    # ＜入力＞
    #   - birthday（datetime）：誕生日
    #   - shi（int）：年支、月支、日支、時支の番号
    # ＜出力＞
    #   - z_kan（int）：蔵干の番号
    # ＜異常検出＞
    # 取得できなかった場合はエラーメッセージを出力して強制終了する

    p = is_setsuiri(birthday, birthday.month)
    for s in kd.setsuiri:
        if (s[0] == birthday.year) and (s[1] == birthday.month):
            if s[1] + p <= 0:
                y = s[0] - 1
                m = 12
            else:
                y = s[0]
                m = s[1] + p
            _setsuiri = datetime(year=y, month=m, day=s[2], hour=s[3], minute=s[4])
            break

    if shi == 6:
        delta1 = timedelta(days=kd.zokan_time[shi][0][0], hours=kd.zokan_time[shi][0][1])
        delta2 = timedelta(days=kd.zokan_time[shi][1][0], hours=kd.zokan_time[shi][1][1])
    else:
        delta = timedelta(days=kd.zokan_time[shi][0], hours=kd.zokan_time[shi][1])

    try:
        if shi == 6:
            if _setsuiri + delta1 >= birthday:
                zokan = kd.zokan[shi][0]
            elif _setsuiri + delta1 < birthday <= _setsuiri + delta2:
                zokan = kd.zokan[shi][1]
            else:
                zokan = kd.zokan[shi][2]
        else:
            if _setsuiri + delta >= birthday:
                zokan = kd.zokan[shi][0]
            else:
                zokan = kd.zokan[shi][1]
        return zokan
    except Exception as e:
        raise MeishikiException("蔵干の計算で例外が送出されました。") from e


def append_gogyo(tenkan, chishi):

    gogyo = [0] * 5
    for k in tenkan:
        gogyo[kd.gogyo_kan[k]] += 1
    for s in chishi:
        gogyo[kd.gogyo_shi[s]] += 1
    return gogyo


def append_inyo(tenkan, chishi):

    inyo = [0] * 2
    for k in tenkan:
        inyo[k % 2] += 1
    for s in chishi:
        inyo[s % 2] += 1
    return inyo


def append_getsurei(d_kan, m_shi):

    if m_shi in kd.getsurei_ou[d_kan]:
        return 1
    if m_shi in kd.getsurei_sou[d_kan]:
        return 2
    return 0


def append_kango(tenkan_zokan):

    # ＜機能＞
    # 干合を命式に追加する
    # ＜入力＞
    #   - 天干＋蔵干
    # ＜出力＞
    #   - 干合のリスト
    #     [[干合する干１, 干１の場所（0〜7）], [干合する干２, 干２の場所], 変化する五行]

    kango = []
    for i, tz1 in enumerate(tenkan_zokan):
        for j in list(range(i, len(tenkan_zokan))):
            if kd.kango[tz1] == tenkan_zokan[j] and i != j:
                kango.append([[tz1, i], [tenkan_zokan[j], j], kd.kango_henka[tz1]])
    return kango


def append_shigo(chishi):

    # ＜機能＞
    # 支合を命式に追加する
    # ＜入力＞
    #   - 地支
    # ＜出力＞
    #   - 支合のリスト
    #     [[支合する支１, 支１の場所（0〜3）], [支合する支２, 支２の場所]]

    shigo = []
    for i, s in enumerate(chishi):
        for j in list(range(i, len(chishi))):
            if kd.shigo[s] == chishi[j] and i != j:
                shigo.append([[s, i], [kd.shigo[s], j]])
    return shigo


def append_hogo(chishi):

    # ＜機能＞
    # 方合を命式に追加する
    # ＜入力＞
    #   - 地支
    # ＜出力＞
    #   - 方合のリスト

    for i, h in enumerate(kd.hogo):
        if (h[0][0] in chishi) and (h[0][1] in chishi) and (h[0][2] in chishi):
            return kd.hogo[i]
    return []


def append_sango(chishi):

    # ＜機能＞
    # 三合を命式に追加する
    # ＜入力＞
    #   - 地支
    # ＜出力＞
    #   - 三合のリスト

    for i, s in enumerate(kd.sango):
        if (s[0][0] in chishi) and (s[0][1] in chishi) and (s[0][2] in chishi):
            return kd.sango[i]
    return []


def append_hankai(chishi):

    # ＜機能＞
    # 半会を命式に追加する
    # ＜入力＞
    #   - 地支
    # ＜出力＞
    #   - 半会のリスト

    hankai = []
    for h in kd.hankai:
        if (h[0][0] in chishi) and (h[0][1] in chishi):
            hankai.append(h)
    return hankai


def append_hitsuchu(chishi):

    # ＜機能＞
    # 七冲を命式に追加する
    # ＜入力＞
    #   - 地支
    # ＜出力＞
    #   - 七冲のリスト

    hitsuchu = []
    for i, s in enumerate(chishi):
        for j in list(range(i, len(chishi))):
            if kd.hitsuchu[s] == chishi[j] and i != j:
                hitsuchu.append([[s, i], [kd.hitsuchu[s], j]])
    return hitsuchu


def append_kei(chishi):

    # ＜機能＞
    # 刑を命式に追加する
    # ＜入力＞
    #   - 地支
    # ＜出力＞
    #   - 刑のリスト

    kei = []
    for i, s in enumerate(chishi):
        for j in list(range(0, len(chishi))):
            if kd.kei[s] == chishi[j] and i != j:
                kei.append([[s, i], [kd.kei[s], j]])
    return kei


def append_gai(chishi):

    # ＜機能＞
    # 害を命式に追加する
    # ＜入力＞
    #   - 地支
    # ＜出力＞
    #   - 害のリスト

    gai = []
    for i, s in enumerate(chishi):
        for j in list(range(i, len(chishi))):
            if kd.gai[s] == chishi[j] and i != j:
                gai.append([[s, i], [kd.gai[s], j]])
    return gai


def append_kubo(birthday, chishi):

    # ＜機能＞
    # 空亡を命式に追加する
    # ＜入力＞
    #   - birthday（datetime）：誕生日
    #   - chishi（list）：地支
    # ＜出力＞
    #   - kubo（list）：空亡となる地支の番号と位置

    d = birthday.day + kd.kisu_table[birthday.year - 1926][birthday.month - 1] - 1
    if d >= 60:
        d -= 60  # d が 60 を超えたら 60 を引く

    try:
        kubo = kd.kubo[d // 10]
    except Exception as e:
        raise MeishikiException("空亡が計算できませんでした。") from e
    return kubo

    # k = []
    # for i, c in enumerate(chishi):
    #     if c in kubo:
    #         k.append([c, i])
    # return k


def append_choko(birthday, d_kan):

    return kd.choko[d_kan][birthday.month - 1]


def append_youjin(d_kan, d_shi):

    if d_kan == 2 and d_shi == 6:  # 丙午
        return 1
    elif d_kan == 4 and d_shi == 6:  # 戊午
        return 1
    elif d_kan == 8 and d_shi == 0:  # 壬子
        return 1
    else:
        return 0


def append_kaigou(d_kan, d_shi):

    if d_kan == 4 and d_shi == 10:  # 戊戌
        return 1
    elif d_kan == 6 and d_shi == 10:  # 庚戌
        return 1
    elif d_kan == 6 and d_shi == 4:  # 庚辰
        return 1
    elif d_kan == 8 and d_shi == 4:  # 壬辰
        return 1
    else:
        return 0


def build_meishiki(birthday: datetime, sex: Sex) -> Meishiki:

    # 天干・地支を得る
    y_kan, y_shi = find_year_kanshi(birthday)
    m_kan, m_shi = find_month_kanshi(birthday, y_kan)
    d_kan, d_shi = find_day_kanshi(birthday)
    t_kan, t_shi = find_time_kanshi(birthday, d_kan)

    # 蔵干を得る
    y_zkan = find_zokan(birthday, y_shi)
    m_zkan = find_zokan(birthday, m_shi)
    d_zkan = find_zokan(birthday, d_shi)
    t_zkan = find_zokan(birthday, t_shi)

    tenkan = [y_kan, m_kan, d_kan, t_kan]
    chishi = [y_shi, m_shi, d_shi, t_shi]
    zokan = [y_zkan, m_zkan, d_zkan, t_zkan]

    nenchu = [y_kan, y_shi, y_zkan]
    getchu = [m_kan, m_shi, m_zkan]
    nitchu = [d_kan, d_shi, d_zkan]
    jichu = [t_kan, t_shi, t_zkan]
    nikkan = d_kan

    # 五行（木火土金水）のそれぞれの数を得る
    gogyo = append_gogyo(tenkan, chishi)

    # 陰陽のそれぞれの数を得る
    inyo = append_inyo(tenkan, chishi)

    # 月令を得る
    getsurei = append_getsurei(d_kan, m_shi)

    # 通変を得る
    tsuhen = [kd.kan_tsuhen[tenkan[2]].index(i) for i in tenkan + zokan]

    # 十二運を得る
    twelve_fortune = [kd.twelve_table[tenkan[2]][i] for i in chishi]

    # 干合・支合を得る
    kango = append_kango(tenkan + zokan)
    shigo = append_shigo(chishi)

    # 方合・三合・半会を得る
    hogo = append_hogo(chishi)
    sango = append_sango(chishi)
    if not sango:
        hankai = append_hankai(chishi)
    else:
        hankai = []

    # 七冲・刑・害を得る
    hitsuchu = append_hitsuchu(chishi)
    kei = append_kei(chishi)
    gai = append_gai(chishi)

    # 空亡を得る
    kubo = append_kubo(birthday, chishi)

    # 調候を得る
    choko = append_choko(birthday, d_kan)

    # 陽刃・魁罡を得る
    youjin = append_youjin(d_kan, d_shi)
    kaigou = append_kaigou(d_kan, d_shi)

    # 命式を組成する
    meishiki = Meishiki(
        birthday,
        sex.value,
        tenkan,
        chishi,
        zokan,
        nenchu,
        getchu,
        nitchu,
        jichu,
        nikkan,
        gogyo,
        inyo,
        getsurei,
        tsuhen,
        twelve_fortune,
        kango,
        shigo,
        hogo,
        sango,
        hankai,
        hitsuchu,
        kei,
        gai,
        kubo,
        choko,
        youjin,
        kaigou,
    )
    return meishiki
