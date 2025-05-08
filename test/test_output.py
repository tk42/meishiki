from datetime import datetime

import pytest

from meishiki.meishiki import build_meishiki
from meishiki.unsei import build_unsei
from meishiki.output import output_content, output_stdio, output_markdown, output_html
from meishiki.consts import Sex


@pytest.fixture
def sample():
    # 2000-01-01 12:00 男性
    birthday = datetime(2000, 1, 1, 12, 0)
    meishi = build_meishiki(birthday, sex=Sex.MALE)
    unsei = build_unsei(meishi)
    return meishi, unsei


# 1989-10-28 12:00 男性
@pytest.fixture
def sample2():
    birthday = datetime(1989, 10, 28, 12, 0)
    meishi = build_meishiki(birthday, sex=Sex.MALE)
    unsei = build_unsei(meishi)
    return meishi, unsei


def test_output_content(sample):
    meishi, unsei = sample
    result = output_content(meishi, unsei)
    assert result == {'birthday': '平成12年1月1日 12時0分生', 'sex': '男命', 'tenkan1': '己', 'chishi1': '卯', 'zokan1': '乙', 'fortune1': '沐', 'tsuhen_tenkan1': '劫財', 'tsuhen_zokan1': '正官', 'tenkan2': '丙', 'chishi2': '子', 'zokan2': '癸', 'fortune2': '胎', 'tsuhen_tenkan2': '偏印', 'tsuhen_zokan2': '正財', 'tenkan3': '戊', 'chishi3': '午', 'zokan3': '丁', 'fortune3': '帝', 'tsuhen_tenkan3': '比肩', 'tsuhen_zokan3': '印綬', 'tenkan4': '戊', 'chishi4': '午', 'zokan4': '丁', 'fortune4': '帝', 'tsuhen_tenkan4': '比肩', 'tsuhen_zokan4': '印綬', 'choko': '火土', 'kubo': '子丑', 'moku': 1, 'ka': 3, 'do': 3, 'gon': 0, 'sui': 1, 'p1': ' 8', 'p2': 18, 'p3': 28, 'p4': 38, 'p5': 48, 'p6': 58, 'p7': 68, 'p8': 78, 'p9': 88, 'p10': 98, 'p11': 108, 'd_tsuhen1': '正官', 'd_kan1': '乙', 'd_shi1': '亥', 'd_tsuhen2': '偏官', 'd_kan2': '甲', 'd_shi2': '戌', 'd_tsuhen3': '正財', 'd_kan3': '癸', 'd_shi3': '酉', 'd_tsuhen4': '偏財', 'd_kan4': '壬', 'd_shi4': '申', 'd_tsuhen5': '傷官', 'd_kan5': '辛', 'd_shi5': '未', 'd_tsuhen6': '食神', 'd_kan6': '庚', 'd_shi6': '午', 'd_tsuhen7': '劫財', 'd_kan7': '己', 'd_shi7': '巳', 'd_tsuhen8': '比肩', 'd_kan8': '戊', 'd_shi8': '辰', 'd_tsuhen9': '印綬', 'd_kan9': '丁', 'd_shi9': '卯', 'd_tsuhen10': '偏印', 'd_kan10': '丙', 'd_shi10': '寅', 'n1': '24', 'n2': '25', 'n3': '26', 'n4': '27', 'n5': '28', 'n6': '29', 'n7': '30', 'n8': '31', 'n9': '32', 'n10': '33', 'n11': '34', 'n_tsuhen1': '偏官', 'n_kan1': '甲', 'n_shi1': '辰', 'n_tsuhen2': '正官', 'n_kan2': '乙', 'n_shi2': '巳', 'n_tsuhen3': '偏印', 'n_kan3': '丙', 'n_shi3': '午', 'n_tsuhen4': '印綬', 'n_kan4': '丁', 'n_shi4': '未', 'n_tsuhen5': '比肩', 'n_kan5': '戊', 'n_shi5': '申', 'n_tsuhen6': '劫財', 'n_kan6': '己', 'n_shi6': '酉', 'n_tsuhen7': '食神', 'n_kan7': '庚', 'n_shi7': '戌', 'n_tsuhen8': '傷官', 'n_kan8': '辛', 'n_shi8': '亥', 'n_tsuhen9': '偏財', 'n_kan9': '壬', 'n_shi9': '子', 'n_tsuhen10': '正財', 'n_kan10': '癸', 'n_shi10': '丑'}


def test_output_content2(sample2):
    meishi, unsei = sample2
    result = output_content(meishi, unsei)
    assert result == {'birthday': '平成元年10月28日 12時0分生', 'sex': '男命', 'tenkan1': '己', 'chishi1': '巳', 'zokan1': '丙', 'fortune1': '死', 'tsuhen_tenkan1': '偏印', 'tsuhen_zokan1': '正官', 'tenkan2': '甲', 'chishi2': '戌', 'zokan2': '戊', 'fortune2': '冠', 'tsuhen_tenkan2': '正財', 'tsuhen_zokan2': '印綬', 'tenkan3': '辛', 'chishi3': '酉', 'zokan3': '辛', 'fortune3': '建', 'tsuhen_tenkan3': '比肩', 'tsuhen_zokan3': '比肩', 'tenkan4': '甲', 'chishi4': '午', 'zokan4': '己', 'fortune4': '病', 'tsuhen_tenkan4': '正財', 'tsuhen_zokan4': '偏印', 'choko': '火木', 'kubo': '子丑', 'moku': 2, 'ka': 2, 'do': 2, 'gon': 2, 'sui': 0, 'p1': ' 7', 'p2': 17, 'p3': 27, 'p4': 37, 'p5': 47, 'p6': 57, 'p7': 67, 'p8': 77, 'p9': 87, 'p10': 97, 'p11': 107, 'd_tsuhen1': '食神', 'd_kan1': '癸', 'd_shi1': '酉', 'd_tsuhen2': '傷官', 'd_kan2': '壬', 'd_shi2': '申', 'd_tsuhen3': '比肩', 'd_kan3': '辛', 'd_shi3': '未', 'd_tsuhen4': '劫財', 'd_kan4': '庚', 'd_shi4': '午', 'd_tsuhen5': '偏印', 'd_kan5': '己', 'd_shi5': '巳', 'd_tsuhen6': '印綬', 'd_kan6': '戊', 'd_shi6': '辰', 'd_tsuhen7': '偏官', 'd_kan7': '丁', 'd_shi7': '卯', 'd_tsuhen8': '正官', 'd_kan8': '丙', 'd_shi8': '寅', 'd_tsuhen9': '偏財', 'd_kan9': '乙', 'd_shi9': '丑', 'd_tsuhen10': '正財', 'd_kan10': '甲', 'd_shi10': '子', 'n1': '35', 'n2': '36', 'n3': '37', 'n4': '38', 'n5': '39', 'n6': '40', 'n7': '41', 'n8': '42', 'n9': '43', 'n10': '44', 'n11': '45', 'n_tsuhen1': '正財', 'n_kan1': '甲', 'n_shi1': '辰', 'n_tsuhen2': '偏財', 'n_kan2': '乙', 'n_shi2': '巳', 'n_tsuhen3': '正官', 'n_kan3': '丙', 'n_shi3': '午', 'n_tsuhen4': '偏官', 'n_kan4': '丁', 'n_shi4': '未', 'n_tsuhen5': '印綬', 'n_kan5': '戊', 'n_shi5': '申', 'n_tsuhen6': '偏印', 'n_kan6': '己', 'n_shi6': '酉', 'n_tsuhen7': '劫財', 'n_kan7': '庚', 'n_shi7': '戌', 'n_tsuhen8': '比肩', 'n_kan8': '辛', 'n_shi8': '亥', 'n_tsuhen9': '傷官', 'n_kan9': '壬', 'n_shi9': '子', 'n_tsuhen10': '食神', 'n_kan10': '癸', 'n_shi10': '丑'}


def test_output_html(sample):
    meishi, unsei = sample
    result = output_html(meishi, unsei, save=False)
    print(result)
    assert result == """
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>御命式</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="format-detection" content="telephone=no">
<meta name="author" content="">
<meta name="keywords" content="">
<meta name="description" content="">
<link rel="stylesheet" href="css/reset.css">
<link rel="stylesheet" href="css/lp.css">
</head>
<body>
<div class="wrap">

<div class="head">
<dl>
	<dt>平成12年1月1日 12時0分生 男命</dt>
	<dd>御命式</dd>
</dl>
</div>


<div class="cont">

<div class="cont_line cont_child_1">
<div class="tate">
<p>
	<div class="time">年</div>
	<div class="eto"><span>己</span><span>卯</span><span>乙</span></div>
	<div class="txt">沐</div>
</p>
</div>
<div class="furikana"><p class="item01">劫財</p><p class="item02">正官</p></div>
</div>

<div class="cont_line cont_child_2">
<div class="tate">
<p>
	<div class="time">月</div>
	<div class="eto"><span>丙</span><span>子</span><span>癸</span></div>
	<div class="txt">胎</div>
</p>
</div>
<div class="furikana"><p class="item01">偏印</p><p class="item02">正財</p></div>
</div>

<div class="cont_line cont_child_3">
<div class="tate">
<p>
	<div class="time">日</div>
	<div class="eto"><span>戊</span><span>午</span><span>丁</span></div>
	<div class="txt">帝</div>
</p>
</div>
<div class="furikana"><p class="item02">印綬</p></div>
</div>

<div class="cont_line cont_child_4">
<div class="tate">
<p>
	<div class="time">時</div>
	<div class="eto"><span>戊</span><span>午</span><span>丁</span></div>
	<div class="txt">帝</div>
</p>
</div>
<div class="furikana"><p class="item01">比肩</p><p class="item02">印綬</p></div>
</div>

</div>



<div class="line">
<div class="line_ttl">大運</div>
<ul class="line_num">
<li class="num_child_1"> 8</li> 
<li class="num_child_2">18</li>
<li class="num_child_3">28</li>
<li class="num_child_4">38</li>
<li class="num_child_5">48</li>
<li class="num_child_6">58</li>
<li class="num_child_7">68</li>
<li class="num_child_8">78</li>
<li class="num_child_9">88</li>
<li class="num_child_10">98</li>
<li class="num_child_11">108</li>  
</ul>

<div class="yaji">
	<img src="img/yaji.png">
</div>
<div class="line_content">
	<dl class="line_child_1">
		<dt>正官</dt>
		<dd>乙亥</dd>
	</dl>
	<dl class="line_child_2">
		<dt>偏官</dt>
		<dd>甲戌</dd>
	</dl>
	<dl class="line_child_3">
		<dt>正財</dt>
		<dd>癸酉</dd>
	</dl>
	<dl class="line_child_4">
		<dt>偏財</dt>
		<dd>壬申</dd>
	</dl>
	<dl class="line_child_5">
		<dt>傷官</dt>
		<dd>辛未</dd>
	</dl>
	<dl class="line_child_6">
		<dt>食神</dt>
		<dd>庚午</dd>
	</dl>
	<dl class="line_child_7">
		<dt>劫財</dt>
		<dd>己巳</dd>
	</dl>
	<dl class="line_child_8">
		<dt>比肩</dt>
		<dd>戊辰</dd>
	</dl>
	<dl class="line_child_9">
		<dt>印綬</dt>
		<dd>丁卯</dd>
	</dl>
	<dl class="line_child_10">
		<dt>偏印</dt>
		<dd>丙寅</dd>
	</dl>
</div>
</div>



<div class="line second">
<div class="line_ttl">年運</div>
<ul class="line_num">
<li class="num_child_1">24</li> 
<li class="num_child_2">25</li>
<li class="num_child_3">26</li>
<li class="num_child_4">27</li>
<li class="num_child_5">28</li>
<li class="num_child_6">29</li>
<li class="num_child_7">30</li>
<li class="num_child_8">31</li>
<li class="num_child_9">32</li>
<li class="num_child_10">33</li>
<li class="num_child_11">34</li>
</ul>

<div class="yaji">
	<img src="img/yaji.png">
</div>
<div class="line_content">
	<dl class="line_child_1">
		<dt>偏官</dt>
		<dd>甲辰</dd>
	</dl>
	<dl class="line_child_2">
		<dt>正官</dt>
		<dd>乙巳</dd>
	</dl>
	<dl class="line_child_3">
		<dt>偏印</dt>
		<dd>丙午</dd>
	</dl>
	<dl class="line_child_4">
		<dt>印綬</dt>
		<dd>丁未</dd>
	</dl>
	<dl class="line_child_5">
		<dt>比肩</dt>
		<dd>戊申</dd>
	</dl>
	<dl class="line_child_6">
		<dt>劫財</dt>
		<dd>己酉</dd>
	</dl>
	<dl class="line_child_7">
		<dt>食神</dt>
		<dd>庚戌</dd>
	</dl>
	<dl class="line_child_8">
		<dt>傷官</dt>
		<dd>辛亥</dd>
	</dl>
	<dl class="line_child_9">
		<dt>偏財</dt>
		<dd>壬子</dd>
	</dl>
	<dl class="line_child_10">
		<dt>正財</dt>
		<dd>癸丑</dd>
	</dl>
</div>
</div>

</div>
</body>
</html>"""


def test_output_markdown(sample):
    meishi, unsei = sample
    result = output_markdown(meishi, unsei)
    print(result)
    assert result == """# 命式

- 生年月日: 平成12年1月1日 12時0分生
- 性別: 男命

| 柱 | 天干 | 支干 | 蔵干 | 十二運 | 通変(天干) | 通変(蔵干) |
| --- | --- | --- | --- | --- | --- | --- |
| 年 | 己 | 卯 | 乙 | 沐 | 劫財 | 正官 |
| 月 | 丙 | 子 | 癸 | 胎 | 偏印 | 正財 |
| 日 | 戊 | 午 | 丁 | 帝 | 比肩 | 印綬 |
| 時 | 戊 | 午 | 丁 | 帝 | 比肩 | 印綬 |

## 大運

| 開始年齢 | 干支 | 通変 |
| --- | --- | --- |
|  8 | 乙亥 | 正官 |
| 18 | 甲戌 | 偏官 |
| 28 | 癸酉 | 正財 |
| 38 | 壬申 | 偏財 |
| 48 | 辛未 | 傷官 |
| 58 | 庚午 | 食神 |
| 68 | 己巳 | 劫財 |
| 78 | 戊辰 | 比肩 |
| 88 | 丁卯 | 印綬 |
| 98 | 丙寅 | 偏印 |

## 年運

| 年齢 | 干支 | 通変 |
| --- | --- | --- |
| 24 | 甲辰 | 偏官 |
| 25 | 乙巳 | 正官 |
| 26 | 丙午 | 偏印 |
| 27 | 丁未 | 印綬 |
| 28 | 戊申 | 比肩 |
| 29 | 己酉 | 劫財 |
| 30 | 庚戌 | 食神 |
| 31 | 辛亥 | 傷官 |
| 32 | 壬子 | 偏財 |
| 33 | 癸丑 | 正財 |"""


def test_output_stdio(sample, capsys):
    meishi, unsei = sample
    output_stdio(meishi, unsei)
    out = capsys.readouterr().out
    # print(out)
    assert out == """＜五行＞
木：1
火：3
土：3
金：0
水：1

＜陰陽のバランス＞
陰：2
陽：6

＜月令＞
月令得ず

＜干合＞
日柱天干の「戊」と月柱蔵干の「癸」とが干合
時柱天干の「戊」と月柱蔵干の「癸」とが干合

＜支合＞
支合なし

＜三合会局＞
三合会局なし

＜半会＞
半会なし

＜方合＞
方合なし

＜空亡＞
子丑

＜七冲＞
月柱地支の「子」が日柱地支の「午」を冲する
月柱地支の「子」が時柱地支の「午」を冲する

＜刑＞
年柱地支の「卯」が、月柱地支の「子」を刑する
日柱地支の「午」が、時柱地支の「午」を刑する
時柱地支の「午」が、日柱地支の「午」を刑する

＜害＞
害なし

＜特記＞
陽刃

乙亥 (正官)： 木半会
======
2008年（平成20年）|   8歳 | 戊子 (比肩) |  干合, 冲
2009年（平成21年）|   9歳 | 己丑 (劫財) |  支合, 水方合, 害
2010年（平成22年）|  10歳 | 庚寅 (食神) |  干合, 支合, 火半会
2011年（平成23年）|  11歳 | 辛卯 (傷官) |  干合, 木半会, 刑
2012年（平成24年）|  12歳 | 壬辰 (偏財) |  干合, 水半会, 害
2013年（平成25年）|  13歳 | 癸巳 (正財) |  干合, 冲
2014年（平成26年）|  14歳 | 甲午 (偏官) |  干合, 冲, 刑, 官殺混雑
2015年（平成27年）|  15歳 | 乙未 (正官) |  支合, 三合木局, 害
2016年（平成28年）|  16歳 | 丙申 (偏印) |  水半会, 害
2017年（平成29年）|  17歳 | 丁酉 (印綬) |  冲

甲戌 (偏官)： 干合, 支合, 火半会
======
2018年（平成30年）|  18歳 | 戊戌 (比肩) |  干合, 支合, 火半会
2019年（平成31年）|  19歳 | 己亥 (劫財) |  干合, 木半会
2020年（令和 2年）|  20歳 | 庚子 (食神) |  干合, 冲
2021年（令和 3年）|  21歳 | 辛丑 (傷官) |  干合, 支合, 刑, 害
2022年（令和 4年）|  22歳 | 壬寅 (偏財) |  干合, 三合火局
2023年（令和 5年）|  23歳 | 癸卯 (正財) |  干合, 支合, 刑
2024年（令和 6年）|  24歳 | 甲辰 (偏官) |  干合, 水半会, 冲, 害
2025年（令和 7年）|  25歳 | 乙巳 (正官) |  官殺混雑
2026年（令和 8年）|  26歳 | 丙午 (偏印) |  火半会, 冲, 刑
2027年（令和 9年）|  27歳 | 丁未 (印綬) |  支合, 木半会, 害

癸酉 (正財)： 干合, 冲
======
2028年（令和10年）|  28歳 | 戊申 (比肩) |  干合, 水半会
2029年（令和11年）|  29歳 | 己酉 (劫財) |  冲, 刑
2030年（令和12年）|  30歳 | 庚戌 (食神) |  干合, 支合, 火半会, 害
2031年（令和13年）|  31歳 | 辛亥 (傷官) |  干合, 木半会
2032年（令和14年）|  32歳 | 壬子 (偏財) |  干合, 冲
2033年（令和15年）|  33歳 | 癸丑 (正財) |  干合, 支合, 金半会, 害
2034年（令和16年）|  34歳 | 甲寅 (偏官) |  干合, 火半会
2035年（令和17年）|  35歳 | 乙卯 (正官) |  冲, 刑
2036年（令和18年）|  36歳 | 丙辰 (偏印) |  支合, 水半会, 害
2037年（令和19年）|  37歳 | 丁巳 (印綬) |  金半会

壬申 (偏財)： 干合, 水半会
======
2038年（令和20年）|  38歳 | 戊午 (比肩) |  干合, 冲, 刑
2039年（令和21年）|  39歳 | 己未 (劫財) |  支合, 木半会, 害
2040年（令和22年）|  40歳 | 庚申 (食神) |  干合, 水半会
2041年（令和23年）|  41歳 | 辛酉 (傷官) |  干合, 冲
2042年（令和24年）|  42歳 | 壬戌 (偏財) |  干合, 支合, 火半会
2043年（令和25年）|  43歳 | 癸亥 (正財) |  干合, 木半会, 害
2044年（令和26年）|  44歳 | 甲子 (偏官) |  干合, 水半会, 天戦地冲
2045年（令和27年）|  45歳 | 乙丑 (正官) |  支合, 害
2046年（令和28年）|  46歳 | 丙寅 (偏印) |  火半会, 冲
2047年（令和29年）|  47歳 | 丁卯 (印綬) |  干合, 刑

辛未 (傷官)： 干合, 支合, 木半会, 害, 
======
2048年（令和30年）|  48歳 | 戊辰 (比肩) |  干合, 水半会, 害
2049年（令和31年）|  49歳 | 己巳 (劫財) |  火方合
2050年（令和32年）|  50歳 | 庚午 (食神) |  干合, 支合, 冲, 刑
2051年（令和33年）|  51歳 | 辛未 (傷官) |  干合, 支合, 木半会, 害
2052年（令和34年）|  52歳 | 壬申 (偏財) |  干合, 水半会
2053年（令和35年）|  53歳 | 癸酉 (正財) |  干合, 冲
2054年（令和36年）|  54歳 | 甲戌 (偏官) |  干合, 支合, 火半会, 刑
2055年（令和37年）|  55歳 | 乙亥 (正官) |  三合木局
2056年（令和38年）|  56歳 | 丙子 (偏印) |  干合, 冲, 害
2057年（令和39年）|  57歳 | 丁丑 (印綬) |  支合, 天戦地冲, 害

庚午 (食神)： 干合, 刑
======
2058年（令和40年）|  58歳 | 戊寅 (比肩) |  干合, 火半会
2059年（令和41年）|  59歳 | 己卯 (劫財) |  刑
2060年（令和42年）|  60歳 | 庚辰 (食神) |  干合, 水半会, 害
2061年（令和43年）|  61歳 | 辛巳 (傷官) |  干合
2062年（令和44年）|  62歳 | 壬午 (偏財) |  干合, 冲, 刑
2063年（令和45年）|  63歳 | 癸未 (正財) |  干合, 支合, 木半会, 害
2064年（令和46年）|  64歳 | 甲申 (偏官) |  干合, 水半会
2065年（令和47年）|  65歳 | 乙酉 (正官) |  干合, 冲
2066年（令和48年）|  66歳 | 丙戌 (偏印) |  支合, 火半会
2067年（令和49年）|  67歳 | 丁亥 (印綬) |  木半会

己巳 (劫財)
======
2068年（令和50年）|  68歳 | 戊子 (比肩) |  干合, 冲
2069年（令和51年）|  69歳 | 己丑 (劫財) |  支合, 害
2070年（令和52年）|  70歳 | 庚寅 (食神) |  干合, 火半会, 刑, 害
2071年（令和53年）|  71歳 | 辛卯 (傷官) |  干合, 刑
2072年（令和54年）|  72歳 | 壬辰 (偏財) |  干合, 水半会, 害
2073年（令和55年）|  73歳 | 癸巳 (正財) |  干合
2074年（令和56年）|  74歳 | 甲午 (偏官) |  干合, 冲, 刑
2075年（令和57年）|  75歳 | 乙未 (正官) |  支合, 火方合, 木半会, 害
2076年（令和58年）|  76歳 | 丙申 (偏印) |  支合, 水半会
2077年（令和59年）|  77歳 | 丁酉 (印綬) |  金半会, 冲

戊辰 (比肩)： 干合, 水半会, 害, 
======
2078年（令和60年）|  78歳 | 戊戌 (比肩) |  干合, 支合, 火半会, 冲
2079年（令和61年）|  79歳 | 己亥 (劫財) |  木半会
2080年（令和62年）|  80歳 | 庚子 (食神) |  干合, 水半会, 冲
2081年（令和63年）|  81歳 | 辛丑 (傷官) |  干合, 支合, 害
2082年（令和64年）|  82歳 | 壬寅 (偏財) |  干合, 木方合, 火半会
2083年（令和65年）|  83歳 | 癸卯 (正財) |  干合, 刑, 害
2084年（令和66年）|  84歳 | 甲辰 (偏官) |  干合, 水半会, 刑, 害
2085年（令和67年）|  85歳 | 乙巳 (正官) |
2086年（令和68年）|  86歳 | 丙午 (偏印) |  冲, 刑
2087年（令和69年）|  87歳 | 丁未 (印綬) |  支合, 木半会, 害

丁卯 (印綬)： 刑
======
2088年（令和70年）|  88歳 | 戊申 (比肩) |  干合, 水半会
2089年（令和71年）|  89歳 | 己酉 (劫財) |  冲
2090年（令和72年）|  90歳 | 庚戌 (食神) |  干合, 支合, 火半会
2091年（令和73年）|  91歳 | 辛亥 (傷官) |  干合, 木半会
2092年（令和74年）|  92歳 | 壬子 (偏財) |  干合, 冲
2093年（令和75年）|  93歳 | 癸丑 (正財) |  干合, 支合, 害
2094年（令和76年）|  94歳 | 甲寅 (偏官) |  干合, 火半会
2095年（令和77年）|  95歳 | 乙卯 (正官) |  刑
2096年（令和78年）|  96歳 | 丙辰 (偏印) |  水半会, 害
2097年（令和79年）|  97歳 | 丁巳 (印綬) |

丙寅 (偏印)： 火半会
======
2098年（令和80年）|  98歳 | 戊午 (比肩) |  干合, 火半会, 冲, 刑
2099年（令和81年）|  99歳 | 己未 (劫財) |  支合, 木半会, 害
2100年（令和82年）| 100歳 | 庚申 (食神) |  干合, 水半会, 冲
2101年（令和83年）| 101歳 | 辛酉 (傷官) |  干合, 冲
2102年（令和84年）| 102歳 | 壬戌 (偏財) |  干合, 支合, 三合火局
2103年（令和85年）| 103歳 | 癸亥 (正財) |  干合, 支合, 木半会
2104年（令和86年）| 104歳 | 甲子 (偏官) |  干合, 天戦地冲
2105年（令和87年）| 105歳 | 乙丑 (正官) |  支合, 害
2106年（令和88年）| 106歳 | 丙寅 (偏印) |  火半会
2107年（令和89年）| 107歳 | 丁卯 (印綬) |  刑

乙丑 (正官)： 支合, 害, 
======
2108年（令和90年）| 108歳 | 戊辰 (比肩) |  干合, 水半会, 害
2109年（令和91年）| 109歳 | 己巳 (劫財) |
2110年（令和92年）| 110歳 | 庚午 (食神) |  干合, 冲, 刑, 害
2111年（令和93年）| 111歳 | 辛未 (傷官) |  干合, 支合, 木半会, 冲, 害
2112年（令和94年）| 112歳 | 壬申 (偏財) |  干合, 水半会
2113年（令和95年）| 113歳 | 癸酉 (正財) |  干合, 金半会, 冲
2114年（令和96年）| 114歳 | 甲戌 (偏官) |  干合, 支合, 火半会, 官殺混雑
2115年（令和97年）| 115歳 | 乙亥 (正官) |  水方合, 木半会
2116年（令和98年）| 116歳 | 丙子 (偏印) |  支合, 冲
2117年（令和99年）| 117歳 | 丁丑 (印綬) |  支合, 害

甲子 (偏官)： 干合, 天戦地冲
======
2118年（令和100年）| 118歳 | 戊寅 (比肩) |  干合, 火半会
2119年（令和101年）| 119歳 | 己卯 (劫財) |  干合, 刑
"""
