import pytest
from datetime import datetime

from meishiki.output import output_markdown, output_daily_fortune_markdown, output_weekly_fortune_markdown, output_monthly_fortune_markdown
from meishiki.output import format_fortune_interactions


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


@pytest.mark.parametrize("fixture_name", ["sample", "sample2", "sample3"])
def test_output_markdown_all(request, fixture_name):
    meishi, unsei = request.getfixturevalue(fixture_name)
    md = output_markdown(meishi, unsei)
    
    # 基本的なMarkdown構造の確認
    assert isinstance(md, str)
    assert len(md) > 0
    
    # 命式の基本要素が含まれているか
    assert "# 命式" in md
    assert "生年月日:" in md
    assert "性別:" in md
    
    # 四柱の要素が含まれているか
    assert "年" in md
    assert "月" in md  
    assert "日" in md
    
    # 五行・納音・陰陽の情報が含まれているか
    assert "五行" in md
    assert "納音" in md
    assert "陰陽" in md
    
    # 運勢情報が含まれているか（unseiがある場合）
    if unsei is not None:
        assert "大運" in md or "年運" in md
    
    # 空行や不正な文字列がないか基本チェック
    lines = md.split('\n')
    assert len(lines) > 10  # 最低限の行数があるか
    assert not any(line.strip() == "None" for line in lines)  # None文字列が含まれていないか


def test_output_daily_fortune_markdown(sample):
    meishi, unsei = sample
    
    target_date = datetime(2024, 1, 1)
    md = output_daily_fortune_markdown(meishi, target_date)
    
    assert "# 日運 - 2024年01月01日" in md
    assert "- **干支**:" in md
    assert "- **通変**:" in md
    assert "- **相互作用**:" in md
    assert isinstance(md, str)


def test_output_daily_fortune_markdown_string_date(sample):
    meishi, unsei = sample
    
    target_date = datetime.fromisoformat("2024-01-01")
    md = output_daily_fortune_markdown(meishi, target_date)
    
    assert "# 日運 - 2024年01月01日" in md
    assert "- **干支**:" in md
    assert "- **通変**:" in md
    assert "- **相互作用**:" in md


def test_output_weekly_fortune_markdown(sample):
    meishi, unsei = sample
    
    week_start = datetime(2024, 1, 1)  # 月曜日
    md = output_weekly_fortune_markdown(meishi, week_start)
    
    assert "# 週運 - 2024年01月01日〜01月07日" in md
    assert "## 01月01日（月）" in md
    assert "## 01月02日（火）" in md
    assert "## 01月07日（日）" in md
    assert "- **干支**:" in md
    assert "- **通変**:" in md
    assert "- **相互作用**:" in md
    assert isinstance(md, str)


def test_output_weekly_fortune_markdown_string_date(sample):
    meishi, unsei = sample
    
    week_start = datetime.fromisoformat("2024-01-01")
    md = output_weekly_fortune_markdown(meishi, week_start)
    
    assert "# 週運 - 2024年01月01日〜01月07日" in md
    assert "## 01月01日（月）" in md


def test_output_monthly_fortune_markdown(sample):
    meishi, unsei = sample
    
    target_date = datetime(2024, 1, 1)
    md = output_monthly_fortune_markdown(meishi, target_date)
    
    assert "# 月運 - " in md and "2024年01月" in md
    assert "- **干支**:" in md
    assert "- **通変**:" in md
    assert "- **相互作用**:" in md
    assert isinstance(md, str)


@pytest.mark.parametrize("fixture_name", ["sample", "sample2", "sample3"])
def test_output_daily_fortune_markdown_all_fixtures(request, fixture_name):
    meishi, unsei = request.getfixturevalue(fixture_name)
    
    target_date = datetime(2024, 6, 15)
    md = output_daily_fortune_markdown(meishi, target_date)
    
    assert "# 日運 - 2024年06月15日" in md
    assert "- **干支**:" in md
    assert "- **通変**:" in md
    assert "- **相互作用**:" in md


@pytest.mark.parametrize("fixture_name", ["sample", "sample2", "sample3"])
def test_output_monthly_fortune_markdown_all_fixtures(request, fixture_name):
    meishi, unsei = request.getfixturevalue(fixture_name)
    
    target_date = datetime(2024, 6, 1)
    md = output_monthly_fortune_markdown(meishi, target_date)
    
    assert "# 月運 - " in md and "2024年06月" in md
    assert "- **干支**:" in md
    assert "- **通変**:" in md
    assert "- **相互作用**:" in md


def test_format_fortune_interactions_with_interactions():
    """相互作用がある場合のテスト"""
    
    fortune_data = {
        'kango': 1,
        'shigo': -1,
        'hogo': 2,
        'sango': -1,
        'hankai': -1,
        'tensen_chichu': -1,
        'chu': -1,
        'kei': -1,
        'gai': -1
    }
    
    result = format_fortune_interactions(fortune_data)
    assert "干合" in result
    assert "方合" in result
    assert "支合" not in result


def test_format_fortune_interactions_no_interactions():
    """相互作用がない場合のテスト"""
    
    fortune_data = {
        'kango': -1,
        'shigo': -1,
        'hogo': -1,
        'sango': -1,
        'hankai': -1,
        'tensen_chichu': -1,
        'chu': -1,
        'kei': -1,
        'gai': -1
    }
    
    result = format_fortune_interactions(fortune_data)
    assert result == "なし"
