from datetime import datetime
from fastmcp import FastMCP
from meishiki import build_meishiki, build_unsei
from meishiki.consts import Sex
from meishiki.errors import MeishikiException
from meishiki.output import output_markdown

mcp = FastMCP("Meishiki Server")


@mcp.tool()
def calculate_meishiki(birthday: str, sex: Sex) -> str:
    """
    Args:
        birthday: ISO8601文字列 (例: "1990-01-23T15:30:00")
        sex: Sex.MALEまたはSex.FEMALE
    Returns:
        Markdown形式の命式
    """
    # 文字列→datetime
    try:
        dt = datetime.fromisoformat(birthday)
    except ValueError:
        raise ValueError("birthday のフォーマットが不正です。")

    # 命式を構築
    try:
        m = build_meishiki(dt, sex)
    except MeishikiException as e:
        # FastMCP側でエラーを整形
        raise RuntimeError(str(e))

    # 運勢を構築
    try:
        u = build_unsei(m)
    except MeishikiException as e:
        # FastMCP側でエラーを整形
        raise RuntimeError(str(e))

    # 命式および運勢を出力
    try:
        markdown = output_markdown(m, u)
    except MeishikiException as e:
        # FastMCP側でエラーを整形
        raise RuntimeError(str(e))
    
    return markdown


if __name__ == "__main__":
    # JSON-RPC over stdio
    mcp.run(transport="stdio")
