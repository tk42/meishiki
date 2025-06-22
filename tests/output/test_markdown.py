import pytest

from meishiki.output import output_markdown


@pytest.mark.parametrize(
    "table, include_unsei",
    [
        (True, True),
        (False, True),
        (True, False),
        (False, False),
    ],
)
def test_output_markdown_basic(sample, table, include_unsei):
    """table / unsei の組み合わせごとの Markdown 出力を簡易検証"""
    meishi, unsei = sample
    unsei_arg = unsei if include_unsei else None

    md = output_markdown(meishi, unsei_arg, table=table)

    # タイトルと基本情報
    assert "# 命式" in md
    assert "生年月日:" in md

    # 年運セクションの有無
    if include_unsei:
        assert "## 年運" in md
    else:
        assert "## 年運" not in md

    # テーブル or 箇条書き
    if table:
        assert "| 柱 | 天干 | 支干" in md  # テーブルヘッダー
    else:
        # テーブルは含まれず、箇条書きがある
        assert "| 柱 |" not in md
        assert "- 天干:" in md


# toki_bashira の有無によるテーブル行の出力分岐を確認
@pytest.mark.parametrize("toki_bashira, should_include", [(True, True), (False, False)])
def test_output_markdown_toki_bashira(sample, toki_bashira, should_include):
    meishi, unsei = sample

    md = output_markdown(meishi, unsei, table=True, toki_bashira=toki_bashira)

    if should_include:
        assert "| 時 |" in md
    else:
        assert "| 時 |" not in md
