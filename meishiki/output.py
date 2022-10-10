from jinja2 import Environment, FileSystemLoader
from datetime import datetime as dt

from meishiki.consts import kd, TemplateType
from meishiki.util import convert_to_wareki


base_dir = "./template/"
output_dir = "./output/"


def output_html(meishiki, unsei, template=TemplateType.TYPE_I):

    env = Environment(loader=FileSystemLoader(""))
    template = env.get_template(base_dir + str(template.value))

    wareki = convert_to_wareki(meishiki.birthday)
    birthday_str = meishiki.birthday.strftime(f"{wareki}%-m月%-d日 %-H時%-M分生")
    sex_str = "男命" if meishiki.sex == 0 else "女命"

    daiun = unsei.daiun
    nenun = unsei.nenun

    content = {
        "birthday": birthday_str,
        "sex": sex_str,
        "tenkan1": kd.kan[meishiki.tenkan[0]],
        "chishi1": kd.shi[meishiki.chishi[0]],
        "zokan1": kd.kan[meishiki.zokan[0]],
        "fortune1": kd.twelve_fortune[meishiki.twelve_fortune[0]],
        "tsuhen_tenkan1": kd.tsuhen[meishiki.tsuhen[0]],
        "tsuhen_zokan1": kd.tsuhen[meishiki.tsuhen[4]],
        "tenkan2": kd.kan[meishiki.tenkan[1]],
        "chishi2": kd.shi[meishiki.chishi[1]],
        "zokan2": kd.kan[meishiki.zokan[1]],
        "fortune2": kd.twelve_fortune[meishiki.twelve_fortune[1]],
        "tsuhen_tenkan2": kd.tsuhen[meishiki.tsuhen[1]],
        "tsuhen_zokan2": kd.tsuhen[meishiki.tsuhen[5]],
        "tenkan3": kd.kan[meishiki.tenkan[2]],
        "chishi3": kd.shi[meishiki.chishi[2]],
        "zokan3": kd.kan[meishiki.zokan[2]],
        "fortune3": kd.twelve_fortune[meishiki.twelve_fortune[2]],
        "tsuhen_tenkan3": kd.tsuhen[meishiki.tsuhen[2]],
        "tsuhen_zokan3": kd.tsuhen[meishiki.tsuhen[6]],
        "tenkan4": kd.kan[meishiki.tenkan[3]],
        "chishi4": kd.shi[meishiki.chishi[3]],
        "zokan4": kd.kan[meishiki.zokan[3]],
        "fortune4": kd.twelve_fortune[meishiki.twelve_fortune[3]],
        "tsuhen_tenkan4": kd.tsuhen[meishiki.tsuhen[3]],
        "tsuhen_zokan4": kd.tsuhen[meishiki.tsuhen[7]],
        "choko": meishiki.choko,
        "kubo": kd.shi[meishiki.kubo[0]] + kd.shi[meishiki.kubo[1]],
        "moku": meishiki.gogyo[0],
        "ka": meishiki.gogyo[1],
        "do": meishiki.gogyo[2],
        "gon": meishiki.gogyo[3],
        "sui": meishiki.gogyo[4],
    }

    p1 = "&nbsp;" + str(daiun[0][0]) if len(str(daiun[0][0])) == 1 else str(daiun[0][0])
    d_nen = {
        "p1": p1,
        "p2": daiun[1][0],
        "p3": daiun[2][0],
        "p4": daiun[3][0],
        "p5": daiun[4][0],
        "p6": daiun[5][0],
        "p7": daiun[6][0],
        "p8": daiun[7][0],
        "p9": daiun[8][0],
        "p10": daiun[9][0],
        "p11": daiun[10][0],
        "d_tsuhen1": kd.tsuhen[daiun[0][3]],
        "d_kan1": kd.kan[daiun[0][1]],
        "d_shi1": kd.shi[daiun[0][2]],
        "d_tsuhen2": kd.tsuhen[daiun[1][3]],
        "d_kan2": kd.kan[daiun[1][1]],
        "d_shi2": kd.shi[daiun[1][2]],
        "d_tsuhen3": kd.tsuhen[daiun[2][3]],
        "d_kan3": kd.kan[daiun[2][1]],
        "d_shi3": kd.shi[daiun[2][2]],
        "d_tsuhen4": kd.tsuhen[daiun[3][3]],
        "d_kan4": kd.kan[daiun[3][1]],
        "d_shi4": kd.shi[daiun[3][2]],
        "d_tsuhen5": kd.tsuhen[daiun[4][3]],
        "d_kan5": kd.kan[daiun[4][1]],
        "d_shi5": kd.shi[daiun[4][2]],
        "d_tsuhen6": kd.tsuhen[daiun[5][3]],
        "d_kan6": kd.kan[daiun[5][1]],
        "d_shi6": kd.shi[daiun[5][2]],
        "d_tsuhen7": kd.tsuhen[daiun[6][3]],
        "d_kan7": kd.kan[daiun[6][1]],
        "d_shi7": kd.shi[daiun[6][2]],
        "d_tsuhen8": kd.tsuhen[daiun[7][3]],
        "d_kan8": kd.kan[daiun[7][1]],
        "d_shi8": kd.shi[daiun[7][2]],
        "d_tsuhen9": kd.tsuhen[daiun[8][3]],
        "d_kan9": kd.kan[daiun[8][1]],
        "d_shi9": kd.shi[daiun[8][2]],
        "d_tsuhen10": kd.tsuhen[daiun[9][3]],
        "d_kan10": kd.kan[daiun[9][1]],
        "d_shi10": kd.shi[daiun[9][2]],
    }

    content.update(d_nen)

    age = dt.today().year - meishiki.birthday.year
    for i, n in enumerate(nenun):
        if age == n[0]:
            break
        n1 = "&nbsp;" + str(nenun[i][0]) if len(str(nenun[i][0])) == 1 else str(nenun[i][0])
        n2 = "&nbsp;" + str(nenun[i + 1][0]) if len(str(nenun[i + 1][0])) == 1 else str(nenun[i + 1][0])
        n3 = "&nbsp;" + str(nenun[i + 2][0]) if len(str(nenun[i + 2][0])) == 1 else str(nenun[i + 2][0])
        n4 = "&nbsp;" + str(nenun[i + 3][0]) if len(str(nenun[i + 3][0])) == 1 else str(nenun[i + 3][0])
        n5 = "&nbsp;" + str(nenun[i + 4][0]) if len(str(nenun[i + 4][0])) == 1 else str(nenun[i + 4][0])
        n6 = "&nbsp;" + str(nenun[i + 5][0]) if len(str(nenun[i + 5][0])) == 1 else str(nenun[i + 5][0])
        n7 = "&nbsp;" + str(nenun[i + 6][0]) if len(str(nenun[i + 6][0])) == 1 else str(nenun[i + 6][0])
        n8 = "&nbsp;" + str(nenun[i + 7][0]) if len(str(nenun[i + 7][0])) == 1 else str(nenun[i + 7][0])
        n9 = "&nbsp;" + str(nenun[i + 8][0]) if len(str(nenun[i + 8][0])) == 1 else str(nenun[i + 8][0])
        n10 = "&nbsp;" + str(nenun[i + 9][0]) if len(str(nenun[i + 9][0])) == 1 else str(nenun[i + 9][0])
        n11 = "&nbsp;" + str(nenun[i + 10][0]) if len(str(nenun[i + 10][0])) == 1 else str(nenun[i + 10][0])

        n_nen = {
            "n1": n1,
            "n2": n2,
            "n3": n3,
            "n4": n4,
            "n5": n5,
            "n6": n6,
            "n7": n7,
            "n8": n8,
            "n9": n9,
            "n10": n10,
            "n11": n11,
            "n_tsuhen1": kd.tsuhen[nenun[i][3]],
            "n_kan1": kd.kan[nenun[i][1]],
            "n_shi1": kd.shi[nenun[i][2]],
            "n_tsuhen2": kd.tsuhen[nenun[i + 1][3]],
            "n_kan2": kd.kan[nenun[i + 1][1]],
            "n_shi2": kd.shi[nenun[i + 1][2]],
            "n_tsuhen3": kd.tsuhen[nenun[i + 2][3]],
            "n_kan3": kd.kan[nenun[i + 2][1]],
            "n_shi3": kd.shi[nenun[i + 2][2]],
            "n_tsuhen4": kd.tsuhen[nenun[i + 3][3]],
            "n_kan4": kd.kan[nenun[i + 3][1]],
            "n_shi4": kd.shi[nenun[i + 3][2]],
            "n_tsuhen5": kd.tsuhen[nenun[i + 4][3]],
            "n_kan5": kd.kan[nenun[i + 4][1]],
            "n_shi5": kd.shi[nenun[i + 4][2]],
            "n_tsuhen6": kd.tsuhen[nenun[i + 5][3]],
            "n_kan6": kd.kan[nenun[i + 5][1]],
            "n_shi6": kd.shi[nenun[i + 5][2]],
            "n_tsuhen7": kd.tsuhen[nenun[i + 6][3]],
            "n_kan7": kd.kan[nenun[i + 6][1]],
            "n_shi7": kd.shi[nenun[i + 6][2]],
            "n_tsuhen8": kd.tsuhen[nenun[i + 7][3]],
            "n_kan8": kd.kan[nenun[i + 7][1]],
            "n_shi8": kd.shi[nenun[i + 7][2]],
            "n_tsuhen9": kd.tsuhen[nenun[i + 8][3]],
            "n_kan9": kd.kan[nenun[i + 8][1]],
            "n_shi9": kd.shi[nenun[i + 8][2]],
            "n_tsuhen10": kd.tsuhen[nenun[i + 9][3]],
            "n_kan10": kd.kan[nenun[i + 9][1]],
            "n_shi10": kd.shi[nenun[i + 9][2]],
        }

        content.update(n_nen)

    result = template.render(content)
    file_name = output_dir + meishiki.birthday.strftime("%Y_%m%d_%H%M_") + str(meishiki.sex) + ".html"
    with open(file_name, "w", encoding="utf8") as f:
        f.write(result)

    return file_name


def output_stdio(meishiki, unsei):

    print("＜五行＞")
    for i, g in enumerate(meishiki.gogyo):
        print(kd.gogyo[i] + "：" + str(g))

    print()

    print("＜陰陽のバランス＞")
    print("陰：" + str(meishiki.inyo[1]))
    print("陽：" + str(meishiki.inyo[0]))

    print()

    print("＜月令＞")
    print(kd.getsurei[meishiki.getsurei])

    print()

    print("＜干合＞")
    if not meishiki.kango:
        print("干合なし")
    else:
        for k in meishiki.kango:
            b1 = kd.kango_chu[k[0][1]]  # 干１の場所
            k1 = kd.kan[k[0][0]]  # 干１
            b2 = kd.kango_chu[k[1][1]]  # 干２の場所
            k2 = kd.kan[k[1][0]]  # 干２
            print(b1 + "の「" + k1 + "」と" + b2 + "の「" + k2 + "」とが干合")

    print()

    print("＜支合＞")
    if not meishiki.shigo:
        print("支合なし")
    else:
        for s in meishiki.shigo:
            b1 = kd.shigo_chu[s[0][1]]  # 支１の場所
            k1 = kd.shi[s[0][0]]  # 支１
            b2 = kd.shigo_chu[s[1][1]]  # 支２の場所
            k2 = kd.shi[s[1][0]]  # 支２
            print(b1 + "の「" + k1 + "」と" + b2 + "の「" + k2 + "」とが支合")

    print()

    print("＜三合会局＞")
    if not meishiki.sango:
        print("三合会局なし")
    else:
        sango = meishiki.sango
        print(
            kd.shi[sango[0][0]]
            + ", "
            + kd.shi[sango[0][1]]
            + ", "
            + kd.shi[sango[0][2]]
            + "の三合"
            + kd.gogyo[sango[1]]
            + "局"
        )

    print()

    print("＜半会＞")
    if not meishiki.hankai:
        print("半会なし")
    else:
        hankai = meishiki.hankai
        for h in hankai:
            print(kd.shi[h[0][0]] + ", " + kd.shi[h[0][1]] + "が" + kd.gogyo[h[2]] + "半会")

    print()

    print("＜方合＞")
    if not meishiki.hogo:
        print("方合なし")
    else:
        hogo = meishiki.hogo
        print(
            kd.shi[hogo[0][0]] + ", " + kd.shi[hogo[0][1]] + ", " + kd.shi[hogo[0][2]] + "で" + kd.gogyo[hogo[1]] + "方合"
        )

    print()

    print("＜空亡＞")
    print(kd.shi[meishiki.kubo[0]] + kd.shi[meishiki.kubo[1]])

    print()

    print("＜七冲＞")
    if not meishiki.hitsuchu:
        print("七冲なし")
    else:
        for h in meishiki.hitsuchu:
            b1 = kd.shigo_chu[h[0][1]]  # 支１の場所
            k1 = kd.shi[h[0][0]]  # 支１
            b2 = kd.shigo_chu[h[1][1]]  # 支２の場所
            k2 = kd.shi[h[1][0]]  # 支２
            print(b1 + "の「" + k1 + "」が" + b2 + "の「" + k2 + "」を冲する")

    print()

    print("＜刑＞")
    if not meishiki.kei:
        print("刑なし")
    else:
        for k in meishiki.kei:
            b1 = kd.shigo_chu[k[0][1]]  # 支１の場所
            k1 = kd.shi[k[0][0]]  # 支１
            b2 = kd.shigo_chu[k[1][1]]  # 支２の場所
            k2 = kd.shi[k[1][0]]  # 支２
            print(b1 + "の「" + k1 + "」が、" + b2 + "の「" + k2 + "」を刑する")

    print()

    print("＜害＞")
    if not meishiki.gai:
        print("害なし")
    else:
        for g in meishiki.gai:
            b1 = kd.shigo_chu[g[0][1]]  # 支１の場所
            k1 = kd.shi[g[0][0]]  # 支１
            b2 = kd.shigo_chu[g[1][1]]  # 支２の場所
            k2 = kd.shi[g[1][0]]  # 支２
            print(b1 + "の「" + k1 + "」と" + b2 + "の「" + k2 + "」とが害")

    print()

    print("＜特記＞")
    if not meishiki.youjin and not meishiki.kaigou:
        print("特記なし")
    else:
        if meishiki.youjin:
            print("陽刃")
        if meishiki.kaigou:
            print("魁罡")

    daiun = unsei.daiun
    nenun = unsei.nenun

    ry = daiun[0][0]
    d_idx = 0
    year = meishiki.birthday.year + ry

    for n, nen in enumerate(nenun):

        if (ry == 10) and (nen[0] != ry) and (nen[0] % 10 == 0):
            d_idx += 1
        if (ry != 10) and (nen[0] != ry) and (nen[0] % 10 == ry):
            d_idx += 1

        if nen[0] == daiun[d_idx][0]:
            print()
            d_kan = kd.kan[daiun[d_idx][1]]  # 大運の干
            d_shi = kd.shi[daiun[d_idx][2]]  # 大運の支
            d_tsuhen = kd.tsuhen[daiun[d_idx][3]]  # 大運の通変
            cont = "".join([d_kan, d_shi]) + " (" + d_tsuhen + ")： "
            if daiun[d_idx][4] != -1:
                cont += "干合, "
            if daiun[d_idx][5] != -1:
                cont += "支合, "
            if daiun[d_idx][6] != -1:
                cont += kd.gogyo[kd.hogo[daiun[d_idx][6]][1]] + "方合, "
            if daiun[d_idx][7] != -1:
                cont += "三合" + kd.gogyo[kd.sango[daiun[d_idx][7]][1]] + "局, "
            if daiun[d_idx][8] != -1:
                cont += kd.gogyo[kd.hankai[daiun[d_idx][8]][2]] + "半会, "
            if daiun[d_idx][9] != -1:
                cont += "天戦地冲, "
            if daiun[d_idx][10] != -1:
                cont += "冲, "
            if daiun[d_idx][11] != -1:
                cont += "刑, "
            if daiun[d_idx][12] != -1:
                cont += "害, "
            else:
                cont = cont[: len(cont) - 2]
            print(cont)
            print("======")

        wareki = convert_to_wareki(dt(year=year, month=meishiki.birthday.month, day=meishiki.birthday.day))
        if len(str(nen[0])) == 1:
            age = "  " + str(nen[0])
        elif len(str(nen[0])) == 2:
            age = " " + str(nen[0])
        else:
            age = str(nen[0])
        cont = str(year) + "年（" + wareki + "）| " + age + "歳 | "

        n_kan = kd.kan[nen[1]]  # 年運の干
        n_shi = kd.shi[nen[2]]  # 年運の支
        n_tsuhen = kd.tsuhen[nen[3]]  # 年運の通変
        cont += "".join([n_kan, n_shi]) + " (" + n_tsuhen + ") |  "
        if nen[4] != -1:
            cont += "干合, "
        if nen[5] != -1:
            cont += "支合, "
        if nen[6] != -1:
            cont += kd.gogyo[kd.hogo[nen[6]][1]] + "方合, "
        if nen[7] != -1:
            cont += "三合" + kd.gogyo[kd.sango[nen[7]][1]] + "局, "
        if nen[8] != -1:
            cont += kd.gogyo[kd.hankai[nen[8]][2]] + "半会, "
        if nen[9] != -1:
            cont += "天戦地冲, "
        if nen[10] != -1:
            cont += "冲, "
        if nen[11] != -1:
            cont += "刑, "
        if nen[12] != -1:
            cont += "害, "
        if nen[13] != -1:
            cont += "官殺混雑"
        else:
            cont = cont[: len(cont) - 2]
        print(cont)
        # breakpoint()
        year += 1

    return 1
