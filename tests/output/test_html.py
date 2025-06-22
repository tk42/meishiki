import pytest

from meishiki.output import output_html
from meishiki.util import convert_to_wareki


@pytest.mark.parametrize(
    "include_unsei",
    [True, False],
)
def test_output_html_basic(sample, include_unsei):
    """HTML 出力が最低限の要素を含むことと、unsei 有無で文字列が一致するかを確認"""
    meishi, unsei = sample
    unsei_arg = unsei if include_unsei else None

    html = output_html(meishi, unsei_arg, save=False)

    # 基本構造の確認
    assert "<!DOCTYPE html>" in html
    assert "<title>御命式</title>" in html
    # 和暦表記（例: 平成12年）がテンプレートに含まれる
    assert convert_to_wareki(meishi.birthday) in html


def test_output_html_same_when_unsei_omitted(sample):
    """unsei を省略した場合と None を渡した場合で結果が同一であること"""
    meishi, unsei = sample

    html1 = output_html(meishi, save=False)
    html2 = output_html(meishi, None, save=False)

    assert html1 == html2
