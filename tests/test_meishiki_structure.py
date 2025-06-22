import pytest

from meishiki.meishiki import append_hogo, append_sango
from meishiki.consts import kd


def _sample_chishi_for_hogo():
    """地支リストが必ず方合を含むよう，kd.hogo の先頭定義を利用"""
    triple = kd.hogo[0][0]  # (支支支)
    # 余分な支を加えても判定に影響しない
    return list(triple) + [99]  # 99 は存在しないダミー値だが条件には絡まない


def _sample_chishi_for_sango():
    """地支リストが必ず三合を含むよう，kd.sango の先頭定義を利用"""
    triple = kd.sango[0][0]
    return list(triple)


@pytest.mark.parametrize(
    "func,chishi_getter,expected_len",
    [
        (append_hogo, _sample_chishi_for_hogo, 2),  # (places, fortune)
        (append_sango, _sample_chishi_for_sango, 3),  # (places, fortune, idx)
    ],
)
def test_append_returns_list(func, chishi_getter, expected_len):
    chishi = chishi_getter()
    result = func(chishi)

    # 関数は必ず list を返すこと
    assert isinstance(result, list), f"{func.__name__} should return list, got {type(result)}"

    # 条件を満たしているので空ではないはず
    assert result, f"{func.__name__} should return non-empty list when chishi contains the corresponding combination"

    # 返却された各要素の構造を検査（方合=2要素, 三合=3要素）
    for elem in result:
        assert isinstance(elem, (list, tuple)), f"elements of {func.__name__} result must be list/tuple"
        assert len(elem) == expected_len, (
            f"elements of {func.__name__} should be length {expected_len}, got {len(elem)}"
        )
        # 2 番目は fortune(int) を期待
        assert isinstance(elem[1], int), "second item (fortune) should be int"
