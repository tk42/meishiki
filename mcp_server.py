from datetime import datetime
from fastmcp import FastMCP
from meishiki import build_meishiki
from meishiki.errors import MeishikiException

mcp = FastMCP("Meishiki Server")


@mcp.tool()
def calculate_meishiki(birthday: str, sex: int) -> dict:
    """
    Args:
        birthday: ISO8601文字列 (例: "1990-01-23T15:30:00")
        sex: 1または2
    Returns:
        Meishiki.__dict__ をそのまま返却
    """
    # 文字列→datetime
    try:
        dt = datetime.fromisoformat(birthday)
    except ValueError:
        raise ValueError("birthday のフォーマットが不正です。")
    # 命式を構築
    try:
        m = build_meishiki(dt, sex)
        return m.__dict__
    except MeishikiException as e:
        # FastMCP側でエラーを整形
        raise RuntimeError(str(e))


if __name__ == "__main__":
    # JSON-RPC over stdio
    mcp.run(transport="stdio")
