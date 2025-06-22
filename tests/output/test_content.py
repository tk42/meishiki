from typing import Optional

import pytest

from meishiki.output import output_content


@pytest.mark.parametrize(
    "fixture_name, include_unsei", [
        ("sample", True),
        ("sample", False),
        ("sample2", True),
        ("sample2", False),
        ("sample3", True),
        ("sample3", False),
    ],
)
def test_output_content_basic(request, fixture_name: str, include_unsei: bool):
    """`output_content` が想定したキーを含むことを確認する。重複テストを parametrize で整理。"""
    meishi, unsei = request.getfixturevalue(fixture_name)

    # unsei を渡す / 渡さないを切り替える
    unsei_arg: Optional[object] = unsei if include_unsei else None
    result = output_content(meishi, unsei_arg)

    # 主要キー
    assert result["birthday"].endswith("生")
    assert result["sex"] in {"男命", "女命"}

    # unsei 有無によるキー存在チェック
    has_unsei_keys = {"p1", "d_tsuhen1", "n1"}
    if include_unsei:
        for key in has_unsei_keys:
            assert key in result
    else:
        for key in has_unsei_keys:
            assert key not in result
