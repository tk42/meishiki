import sys
from datetime import datetime as dt

from meishiki.consts import TemplateType
from meishiki.meishiki import build_meishiki
from meishiki.unsei import build_unsei
from meishiki.output import output_html, output_stdio

if __name__ == "__main__":
    # Input as follows:
    # $ python3 ./generate_html.py 1978-09-26 13:51 0
    birthday = dt.strptime(sys.argv[1] + " " + sys.argv[2], "%Y-%m-%d %H:%M")
    sex = int(sys.argv[3])

    # 命式を組成する
    meishiki = build_meishiki(birthday, sex)

    # 運勢を組成する
    unsei = build_unsei(meishiki)

    # 命式・運勢を出力する
    f1 = output_html(meishiki, unsei, template=TemplateType.TYPE_II)
    f2 = output_stdio(meishiki, unsei)
